from unittest.mock import Mock
import httpx
import pytest
from baja_sponsorship.research.http_fetcher import SafePublicSourceFetcher, SourceFetchError


def public_dns(*a,**k):
    return [(None,None,None,None,('8.8.8.8',443))]


def make_fetcher(content='<html><body><header>MENU</header><main>Patrocínios corporativos são analisados em até três meses.</main></body></html>',status=200,headers=None,domain=None):
    transport=httpx.MockTransport(lambda req:httpx.Response(status, content=content, headers=headers or {'content-type':'text/html'}))
    client=httpx.Client(transport=transport,follow_redirects=False)
    return SafePublicSourceFetcher(client=client,resolver=public_dns,allowed_domains={domain} if domain else None)


def test_retrieves_body_strips_navigation():
    text=make_fetcher().fetch('https://www.bosch.com.br/contato/')
    assert 'analisados em até três meses' in text
    assert 'MENU' not in text

@pytest.mark.parametrize('url',[
    'http://www.bosch.com.br/contato/', 'https://127.0.0.1/',
    'https://user:pass@www.bosch.com.br/', 'https://www.bosch.com.br:8080/',
    'file:///etc/passwd',
])
def test_rejects_dangerous_url(url):
    with pytest.raises(SourceFetchError):make_fetcher().fetch(url)


def test_rejects_private_dns():
    f=make_fetcher();f.resolver=lambda *a,**k:[(None,None,None,None,('10.1.2.3',443))]
    with pytest.raises(SourceFetchError,match='DNS'):f.fetch('https://www.bosch.com.br/contato/')


def test_rejects_unknown_domain():
    with pytest.raises(SourceFetchError,match='allowlisted'):
        make_fetcher(domain='www.bosch.com.br').fetch('https://random.example/path')


def test_rejects_redirects():
    with pytest.raises(SourceFetchError,match='HTTP status 302'):
        make_fetcher(status=302,headers={'content-type':'text/html','location':'https://other.site/'}).fetch('https://www.bosch.com.br/contato/')


def test_rejects_stream_over_limit():
    f=make_fetcher(content='x'*2048);f.max_bytes=1024
    with pytest.raises(SourceFetchError,match='byte limit'):
        f.fetch('https://www.bosch.com.br/contato/')


def test_rejects_incompatible_mime():
    with pytest.raises(SourceFetchError,match='content type'):
        make_fetcher(headers={'content-type':'image/jpeg'}).fetch('https://www.bosch.com.br/contato/')
