# Data privacy and storage — public repository policy (E1)

**User requirement:** no sensitive information may be accessible in the public GitHub repository, including its branches, pull requests, issues, artifacts or commit history.

## Repository allowlist

Publicly acceptable: generic software source code, architecture/specification documents, data schemas, synthetic examples and high-level institutional facts **only where confirmed public and authorized for reuse**.

**Never commit or paste into public GitHub:**
- personal contact details, private emails/phone numbers, personal identifiers or lists of team contacts;
- source PPTX/PDF, embedded objects, private logo/media collections, contracts and internal budget worksheets;
- actual company-specific commercial terms, negotiations, nonpublic sponsorship values, donor/partner correspondence or submitted/generated proposals;
- research logs that contain personal data, private company information, tokens, credentials, refresh tokens or API keys;
- restricted needs quantities or costs pending approval.

Avoid sensitive content in branch names, commit messages, PR reviews, CI logs and issue descriptions. The private original PPTX must remain separate from versioned public files.

## Data separation

`public_repo`: code, policies and sanitized fixtures only.

`private_team_store`: authoritative, versioned institutional facts, tier/benefit tables, contact data, team needs, templates and approved proposals. Access is role-controlled; operational management approves changes.

`runtime_local`: encrypted or access-controlled working data, generated PPTX/PDF, temporary extraction, cache, SQLite and model logs. Apply retention/deletion policy and protect backups before deployment.

## Technical controls to implement

- Ignore restricted paths/file formats by default; note that `.gitignore` **cannot** prevent `git add -f`.
- Add staged-file content validation (secrets/PII/binaries) in pre-commit and CI before merging, with deny-by-default for unapproved binary documents.
- Sanitize synthetic fixtures and exception traces; avoid revealing source details in application error messages.
- Use environment-managed credentials with no logging of secrets.
- Define retention and access rules for proposal histories in E5 before production.
- Do not expose private source or output files via public web paths or unprotected static hosting.
- If data are committed by mistake, treat deletion from a later commit as insufficient; rotate leaked secrets and follow incident response/history remediation.

## Document generation

Read restricted assets from private paths at runtime. Never copy their contents into the public repo as part of code generation. Final exports and contact fields are available only to authorized operators and must pass management review before sharing externally.

## Current state

Policy documented; security checks and private-store implementation **not yet built**. Public GitHub content has not undergone a full automated historical secret scan in this milestone.
