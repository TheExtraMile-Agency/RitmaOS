# Module 4 Framework Extraction: Workspace Blueprint and Vault Toolkit

Source raw overviews:

- `02_RAW_MODULES/4-workspace-blueprint-full-template.md`
- `02_RAW_MODULES/4-vault-toolkit-overview.md`

Source asset packages:

- `05_NEW_MODULES_INBOX/module-4/workspace-blueprint.zip`
- `05_NEW_MODULES_INBOX/module-4/vault-toolkit.zip`

Status: Extracted framework draft. Not a durable decision.

## Core Framework

Module 4 shifts from lesson text into practical source packages. The assets demonstrate how RitmaOS-style workspace architecture can be distributed as examples, constraints, reference architectures, and builder skills.

The reusable framework is:

```text
workspace map -> task router -> workspace context -> constraint/reference/tool layer
```

The value is not just the folder tree. The value is the routing logic that tells an agent what to load, what to skip, and which constraints or tools matter for the current task.

## Three-Layer Routing System

The Workspace Blueprint package expresses a three-layer architecture:

| Layer | File or Location | Job |
|---|---|---|
| Map | Top-level `CLAUDE.md` | Permanent project map, naming conventions, placement rules, and navigation. |
| Router | Top-level `CONTEXT.md` | Task-level routing into the correct workspace. |
| Workspace | Workspace-level `CONTEXT.md` files | Local operating context, task rules, references, and tool hooks. |

The pattern keeps the always-loaded context small and pushes detailed instructions into scoped workspace context files.

## Workspace as Externalized Memory and State

The package treats folders and filenames as state-bearing infrastructure:

- folders define boundaries,
- context files define local memory,
- naming conventions track artifact status,
- output folders create handoff points,
- examples show how work moves between spaces.

This continues the earlier RitmaOS principle that the filesystem can serve as a lightweight orchestration layer before a database or app runtime exists.

## Constraint Library Pattern

The Vault Toolkit adds a second asset type: reusable constraint files.

Constraints are operating rules that can be loaded selectively by task or workflow stage. They are not raw prompt templates. They are reusable guardrails for problems like context hygiene, output drift, voice consistency, layer triage, handoff readiness, and scaling versus automating.

Extracted principle:

```text
Do not load every rule into every task. Attach constraints only where they improve the current step.
```

## Reference Architecture Gallery

The Vault Toolkit includes annotated reference architectures for different work types. These are examples of layered workspace design rather than a single mandated structure.

Productizable pattern:

```text
reference architecture = worked example + folder structure + context files + configuration rules
```

This supports a future RitmaOS gallery where users can study or fork architecture patterns without treating any one example as canonical.

## Skill Starters as Guided Workspace Builders

The Vault Toolkit includes skill starters that ask diagnostic questions before generating a workspace skeleton.

Extracted process:

1. Diagnose the user's workflow.
2. Identify workspace boundaries.
3. Select relevant constraints.
4. Generate a starter folder/context structure.
5. Leave customization points for the user.

This is a bridge from static template to interactive setup wizard.

## Asset-Heavy Module Handling Pattern

Module 4 implies a new repository handling pattern:

| Source Type | Repository Layer |
|---|---|
| Original downloadable zips | `05_NEW_MODULES_INBOX/module-4/` |
| Raw lesson or package overview text | `02_RAW_MODULES/` |
| Neutral package inventory and checksums | `05_NEW_MODULES_INBOX/module-4/` |
| Extracted architecture | `03_EXTRACTED_FRAMEWORKS/` |
| Product implications | `04_PRODUCT_SPEC_DRAFTS/` |
| Open synthesis questions | `07_SYNTHESIS_QUEUE/` |

This keeps assets preserved while preventing raw packages from contaminating product templates before review.

## RitmaOS Extraction

Module 4 suggests RitmaOS is not only a methodology for writing context files. It can become a package system for AI workspaces:

```text
blueprints
constraints
reference architectures
skill starters
checksums
inventories
guided builders
```

These pieces should remain distinct until a durable product decision says otherwise.
