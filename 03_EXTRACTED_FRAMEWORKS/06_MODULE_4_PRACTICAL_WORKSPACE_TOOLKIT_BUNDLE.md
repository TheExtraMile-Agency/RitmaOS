# Module 4 Framework Extraction: Practical Workspace Toolkit Bundle

Source raw overviews:

- `02_RAW_MODULES/4-workspace-blueprint-full-template.md`
- `02_RAW_MODULES/4-vault-toolkit-overview.md`

Source asset packages:

- `05_NEW_MODULES_INBOX/module-4/workspace-blueprint.zip`
- `05_NEW_MODULES_INBOX/module-4/vault-toolkit.zip`
- `05_NEW_MODULES_INBOX/module-4/clief_notes_skills_field_manual_v1.pdf`
- `05_NEW_MODULES_INBOX/module-4/resource-index-claude-repos.pdf`

Status: Extracted framework draft. Not a durable decision.

## Core Framework

Module 4 shifts from lesson text into practical source packages. The assets demonstrate how RitmaOS-style workspace architecture can be distributed as examples, constraints, reference architectures, builder skills, PDF manuals, and resource indexes.

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

## Prompt Library Pattern

The prompt library source is still pending exact raw-source staging. The provided module framing identifies prompts as outputs of real strategy sessions rather than generic prompt packs.

Extracted working pattern:

```text
business problem -> strategic framework -> reusable prompt -> customized answer
```

Prompt sequences should be treated as framework artifacts. They encode strategic moves such as zero-spend audits, minimum viable fixes, manual-process-to-product conversion, agency undercut strategy, revenue-share calculators, content planning, problem-first AI mapping, and full business audits.

## Skills Manual / Capability Routing Pattern

The Skills Field Manual PDF is staged as a raw asset. It should be treated as capability-routing documentation, not as a prompt library.

Extracted framework:

```text
need persistent context? -> project/custom skill/CLAUDE.md/memory
need external data? -> connector/MCP/web search/deep research
need repeatable process? -> skill or workflow
need concrete output? -> artifact/file/code execution
need deeper reasoning? -> extended thinking
```

RitmaOS implication: context architecture beats prompt wordsmithing. The system should help users choose the right capability layer instead of writing longer prompts.

## Resource Index Pattern

The Resource Index PDF is staged as a raw asset. It should be treated as a tool-discovery and capability-routing layer.

Extracted categories:

- official repositories as authoritative references,
- community skill collections as reusable workflow patterns,
- MCP server indexes as external-tool integration maps,
- programmatic video tools as code infrastructure,
- frontend/UI/design libraries as artifact acceleration tools,
- learning/reference resources as foundation material.

Mapped to the 60/30/10 lens:

```text
60% traditional code/tools: Remotion, UI libraries, reference implementations
30% rules/tools/infrastructure: skills, MCP servers, plugins, workflow libraries
10% AI reasoning: Claude Code and model-mediated automation across layers
```

## Asset-Heavy Module Handling Pattern

Module 4 implies a new repository handling pattern:

| Source Type | Repository Layer |
|---|---|
| Original downloadable zips | `05_NEW_MODULES_INBOX/module-4/` |
| Original downloadable PDFs | `05_NEW_MODULES_INBOX/module-4/` |
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
prompt/framework libraries
reference architectures
skill starters
skills manuals
resource indexes
checksums
inventories
guided builders
```

These pieces should remain distinct until a durable product decision says otherwise.
