"""Conservative public-HTTPS HTML/PDF reader with network safety controls.

Deployment MUST also enforce network egress controls against DNS rebinding.
No redirects, internal IPs, alternate ports, or credential-bearing URLs.
"""
from __future__ import annotations

from io import BytesIO
import ipaddress
import socket
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import httpx
from pypdf import PdfReader


class SourceFetchError(RuntimeError):
    pass


class SafePublicSourceFetcher:
    def __init__(self, *, timeout_seconds: float = 8.0,
                 max_bytes: int = 2_000_000, max_pdf_pages: int = 10,
                 allowed_domains: set[str] | None = None,
                 client: httpx.Client | None = None, resolver=None):
        self.timeout_seconds = timeout_seconds
        self.max_bytes = max_bytes
        self.max_pdf_pages = max_pdf_pages
        self.allowed_domains = allowed_domains
        self.client = client
        self.resolver = resolver or socket.getaddrinfo

    def fetch(self, url: str) -> str:
        parsed = urlparse(url)
        host = parsed.hostname
        if parsed.scheme != "https" or not host or parsed.username or parsed.password or parsed.port not in (None, 443):
            raise SourceFetchError("only standard public HTTPS sources are permitted")
        try:
            ipaddress.ip_address(host)
        except ValueError:
            pass
        else:
            raise SourceFetchError("numeric IP URLs are not permitted")
        if self.allowed_domains and host not in self.allowed_domains:
            raise SourceFetchError("source host not allowlisted")
        try:
            destinations = self.resolver(host, 443, type=socket.SOCK_STREAM)
            if not destinations or any(not ipaddress.ip_address(item[4][0]).is_global for item in destinations):
                raise SourceFetchError("DNS resolves outside globally routable addresses")
        except (socket.gaierror, ValueError, IndexError, TypeError) as exc:
            raise SourceFetchError("source DNS lookup failed") from exc
        owns_client = self.client is None
        client = self.client or httpx.Client(
            follow_redirects=False, timeout=self.timeout_seconds, trust_env=False,
            headers={"User-Agent": "BAJA-Sponsorship-Research/0.1 (public evidence verifier)"})
        try:
            with client.stream("GET", url) as response:
                if not response.is_success:
                    raise SourceFetchError(f"HTTP status {response.status_code}")
                declared = response.headers.get("content-length")
                if declared and declared.isdecimal() and int(declared) > self.max_bytes:
                    raise SourceFetchError("source exceeds byte limit")
                kind = response.headers.get("content-type", "").lower().split(";", 1)[0].strip()
                if kind not in ("text/html", "application/xhtml+xml", "text/plain", "application/pdf"):
                    raise SourceFetchError("unsupported source content type")
                chunks = []
                size = 0
                for part in response.iter_bytes():
                    size += len(part)
                    if size > self.max_bytes:
                        raise SourceFetchError("source exceeds streamed byte limit")
                    chunks.append(part)
                payload = b"".join(chunks)
                if kind == "application/pdf":
                    doc = PdfReader(BytesIO(payload), strict=False)
                    texts = [page.extract_text() or "" for page in list(doc.pages)[:self.max_pdf_pages]]
                    text = "\n".join(texts)
                elif kind == "text/plain":
                    text = payload.decode("utf-8", errors="replace")
                else:
                    soup = BeautifulSoup(payload, "html.parser")
                    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
                        tag.decompose()
                    text = soup.get_text(" ", strip=True)
                if not text.strip():
                    raise SourceFetchError("source has no extractable text")
                return text[:100000]
        except httpx.HTTPError as exc:
            raise SourceFetchError(f"HTTP fetching failed: {type(exc).__name__}") from exc
        finally:
            if owns_client:
                client.close()
