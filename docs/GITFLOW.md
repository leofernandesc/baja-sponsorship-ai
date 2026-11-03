# Git workflow

## Branching

- `main`: approved stable milestones only.
- `develop`: integration branch.
- `feature/<scope>`: one scoped development task.
- `fix/<scope>`: controlled corrections.
- `docs/<scope>`: documentation-only changes.
- `release/<version>`: optional when the MVP requires formal releases.

## PR process

1. Open an issue or state task ID and acceptance criteria.
2. Branch from `develop`.
3. Make small commits while working. Prefer a final **squash merge** into `develop` for a clean history.
4. Require at least one reviewer for changes to commercial policy, original PPTX handling, security or release status.
5. Update relevant specs and attach test evidence/screenshots where material.
6. Merge `develop` to `main` only after milestone checkpoint acceptance.

## Protection rules (recommended, if the repository is on GitHub)

Require PRs for `main`, block direct pushes, and use review/CI checks when available. The project owner must configure these settings; the scaffold does not create them.

## Commit convention (proposed)

`docs: define PPTX extension contract`, `feat: add evidence normalization`, `test: cover proposal approval states`, `fix: preserve slide assets`.

## Security

No secrets, private sponsor discussions, non-approved logo assets or generated company proposals committed to the public repository. Keep original PowerPoint assets access-controlled until authorized for publication.
