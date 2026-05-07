# Module 3.2 Product Implications Draft

Source raw module: `02_RAW_MODULES/3.2-customizing-for-your-use-case.md`

Status: Draft only. Do not treat as a durable decision.

## Product Thesis Implication

Module 3.2 suggests RitmaOS should not ship as one rigid folder structure. It should ship as a configurable workspace generator that preserves the same architecture while adapting labels, routing, and context files to the user’s domain.

## Potential MVP Direction

A useful MVP could ask the user what type of work they do, then generate:

- root `CLAUDE.md`
- 2–4 workspace folders
- one `CONTEXT.md` per workspace
- task routing table
- naming conventions
- starter subfolders
- optional skills/tool mappings

## Starter Archetypes Suggested by 3.2

### Content Creator

Potential folders:

- `script-lab/`
- `production/`
- `distribution/`

Use case:

- idea development
- script drafting
- content production
- publishing and repurposing

### Freelancer / Consultant

Potential folders:

- one folder per client
- `templates/`
- `business-dev/`

Use case:

- client isolation
- deliverable production
- proposal/report reuse
- pipeline and outreach support

### Developer

Potential folders:

- `planning/`
- `src/`
- `docs/`
- `ops/`

Use case:

- specs and architecture
- codebase guidance
- documentation workflows
- deployment and operations support

## Product Requirements Draft

RitmaOS should support:

1. Archetype selection.
2. Custom workspace names.
3. Generated routing table.
4. Generated `CONTEXT.md` files.
5. Naming convention generation.
6. Client/project isolation rules.
7. Tool/skill scoping by workspace.
8. Context file iteration after use.

## Service Offer Draft

Before software exists, RitmaOS can be sold as a done-for-you workspace setup service:

1. Interview the user or business.
2. Identify workspace boundaries.
3. Build the folder system.
4. Write `CLAUDE.md` and workspace `CONTEXT.md` files.
5. Add naming conventions and operating rules.
6. Teach the user how to update context files as they work.

## Open Product Question

Should RitmaOS first become:

- a template pack,
- a setup wizard,
- a CLI generator,
- a desktop/local folder builder,
- a consulting/service package,
- or a combination of service first, software later?
