# GitHub repository setup

## Suggested repository

- **Name:** `baja-sponsorship-ai`
- **Description:** AI-powered sponsorship prospecting and proposal generation for the BAJA UEA engineering team.
- **Actual visibility (03 Nov 2026): PUBLIC.** Do not upload source PPTX/PDF, logos, commercial proposals or sponsor correspondence without team authorization.
- **License:** leave unset until the team approves a license and source-asset distribution policy.

## Bootstrap locally

The repository exists at `https://github.com/leofernandesc/baja-sponsorship-ai`. Put scaffold contents at the root; do not create an extra nested `baja-sponsorship-ai/` directory. Review `git status` before staging.

```bash
# After creating an empty repository on GitHub:
git clone <REPOSITORY_URL>
cd baja-sponsorship-ai
# Copy scaffold files into this directory, then review:
git status
```

For Git Flow, create `develop` from `main` after initial approved documentation; subsequent work uses scoped `feature/*` and `docs/*` branches. Repository owner configures branch protection.

## Initial PR suggestion

`docs: bootstrap product specification and implementation plan` — include README, specs, architecture, template-preservation contract, research policy and milestone gates. Keep source deck out until access/publication is resolved.
