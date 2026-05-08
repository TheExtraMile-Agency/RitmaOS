# Module 4 Product Implications Draft

Source raw overviews:

- `02_RAW_MODULES/4-workspace-blueprint-full-template.md`
- `02_RAW_MODULES/4-vault-toolkit-overview.md`

Source asset packages:

- `05_NEW_MODULES_INBOX/module-4/workspace-blueprint.zip`
- `05_NEW_MODULES_INBOX/module-4/vault-toolkit.zip`
- `05_NEW_MODULES_INBOX/module-4/clief_notes_skills_field_manual_v1.pdf`
- `05_NEW_MODULES_INBOX/module-4/resource-index-claude-repos.pdf`

Status: Draft product implications only. Not a durable decision.

## Product Thesis Implication

Module 4 suggests RitmaOS may need first-class support for asset-heavy modules. Some source material is not a single lesson text. It can include downloadable workspace examples, nested packages, PDFs/manuals, prompt libraries, constraint libraries, reference architectures, resource indexes, and skill starters.

The product and repository model should distinguish:

- raw lesson text,
- downloadable source packages,
- PDFs/manuals,
- prompt libraries,
- constraint libraries,
- resource indexes,
- reference architectures,
- skill starters,
- `CLAUDE.md` templates,
- workflow starter kits,
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

## Prompt / Framework Library

Prompt libraries should be treated as framework artifacts, not isolated copy-paste prompts.

Draft product model:

```text
business problem -> strategic framework -> prompt sequence -> customized answer
```

RitmaOS could link each prompt back to the framework it encodes and the product/business problem it is meant to solve.

## Skills and Capability Guide

Skills/manuals should be treated as capability-routing documentation.

RitmaOS could help users decide whether a task needs:

- persistent context,
- external data,
- repeatable process,
- output generation,
- deeper reasoning,
- a connector or MCP,
- a custom skill,
- a workspace-level context file.

## Resource Recommendation Index

Resource indexes should be treated as tool-discovery and capability-routing documentation.

Potential feature:

```text
workflow problem -> recommended repo/tool/resource category -> setup instructions
```

This prevents resource lists from becoming generic link dumps.

## Folder Architecture Reference

The Folder Organization Guide should become one of the core architecture references for RitmaOS.

Draft product implication:

```text
map -> rooms -> tools
```

could become the candidate canonical RitmaOS workspace model.

RitmaOS should support generating role-specific folder structures from a routing-table model, with naming conventions acting as a lightweight database or indexing system.

## Production `CLAUDE.md` Generator

RitmaOS should likely include production `CLAUDE.md` generators for different user archetypes.

Candidate archetypes:

- content creator,
- consultant / agency,
- developer,
- researcher / writer,
- small business operator.

Generated `CLAUDE.md` files should stay small and route into workspace context files rather than storing all project knowledge.

The templates should be editable starter artifacts, not rigid final files.

## Workflow Starter Generator

Workflow starters should likely become generated starter workspaces, not just documentation.

A generated scaffold could include:

- root `CLAUDE.md`,
- workspace `CONTEXT.md` files,
- naming conventions,
- rules,
- tool/skill recommendations,
- process-specific folders.

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
3. Prompt/framework library.
4. Reference architecture gallery.
5. Skills/capabilities decision guide.
6. Repo/resource recommendation index.
7. Skill/workspace builder wizard.
8. Workflow starter generator.
9. Package inventory and checksum system.
10. Asset-heavy module workflow.
```

## Decision Status

No durable decision is created by this module.

Potential future decisions:

- Should asset-heavy modules become a formal RitmaOS module type?
- Should `05_NEW_MODULES_INBOX/module-x/` become the canonical raw asset staging location?
- Should RitmaOS include a formal package installer or keep asset handling manual for now?
- Should prompt libraries, constraints, skills manuals, and resource indexes become first-class product categories?
- Should workflow starter kits and `CLAUDE.md` templates become first-class product categories?
- Is asset-heavy module handling now a product requirement rather than only an archival concern?
