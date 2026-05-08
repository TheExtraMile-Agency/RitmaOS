# Module 4 Product Implications Draft

Source raw overviews:

- `02_RAW_MODULES/4-workspace-blueprint-full-template.md`
- `02_RAW_MODULES/4-vault-toolkit-overview.md`

Source asset packages:

- `05_NEW_MODULES_INBOX/module-4/workspace-blueprint.zip`
- `05_NEW_MODULES_INBOX/module-4/vault-toolkit.zip`

Status: Draft product implications only. Not a durable decision.

## Product Thesis Implication

Module 4 suggests RitmaOS may need first-class support for asset-heavy modules. Some source material is not a single lesson text. It can include downloadable workspace examples, nested packages, constraint libraries, reference architectures, and skill starters.

The product and repository model should distinguish:

- raw lesson text,
- downloadable source packages,
- extracted architecture,
- implementation templates,
- synthesis questions.

## Asset Package Support

A future RitmaOS product could include a package inventory and checksum system for downloadable assets.

Potential capabilities:

| Capability | Product Value |
|---|---|
| Package staging | Preserves raw downloadable material without polluting working templates. |
| SHA256 checksums | Confirms assets have not changed between download, review, and installation. |
| Top-level inventory | Lets users inspect package shape before importing anything. |
| Asset type labels | Separates lesson text, zips, examples, constraints, and builders. |
| Review workflow | Prevents nested repos, placeholder files, or rough examples from becoming product templates too early. |

## Workspace Blueprint Installer

The Workspace Blueprint package points toward a possible installer that can create a working folder system from a reviewed blueprint.

Possible installer steps:

1. Read a blueprint inventory.
2. Ask which workspace archetype to create.
3. Copy selected template files.
4. Generate or adapt `CLAUDE.md`.
5. Generate or adapt top-level and workspace `CONTEXT.md` files.
6. Exclude raw-only or teaching-only assets unless requested.
7. Produce a checksum or install report.

## Constraint Library

The Vault Toolkit suggests a reusable constraint library as a product component.

Possible product model:

```text
constraint = problem-specific operating rule + tuning questions + recommended use point
```

RitmaOS could let users attach constraints to:

- whole workspaces,
- workflow stages,
- review gates,
- handoff steps,
- specific artifact types.

## Reference Architecture Gallery

The asset package also supports a gallery of reference architectures.

Draft gallery types:

- content production,
- small business operations,
- client delivery,
- developer relations,
- custom user-generated workspaces.

The gallery should be treated as a learning and starting-point layer, not as final doctrine.

## Skill and Workspace Builder Wizard

Skill starters imply a guided builder experience.

Draft product flow:

1. Ask diagnostic questions.
2. Identify workflow boundaries.
3. Recommend workspaces.
4. Select relevant constraints.
5. Generate a starter folder structure.
6. Explain how to update context files after real use.

## Implementation Template Boundary

Module 4 should not automatically convert raw packages into `09_TEMPLATES/`.

Reason:

- Raw packages may contain nested Git repos.
- Raw packages may contain placeholder files.
- Raw packages may be teaching examples rather than production-ready templates.
- Product templates need a separate cleanup and review pass.

## MVP Implication

A practical RitmaOS MVP may eventually need:

```text
1. Workspace blueprint generator.
2. Constraint library.
3. Reference architecture gallery.
4. Skill/workspace builder wizard.
5. Package inventory and checksum system.
6. Asset-heavy module workflow.
```

## Decision Status

No durable decision is created by this module.

Potential future decisions:

- Should asset-heavy modules become a formal RitmaOS module type?
- Should `05_NEW_MODULES_INBOX/module-x/` become the canonical raw asset staging location?
- Should RitmaOS include a formal package installer or keep asset handling manual for now?
