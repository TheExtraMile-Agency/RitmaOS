# Module 3.3 Product Implications Draft

Source module: `02_RAW_MODULES/3.3-common-mistakes-and-how-to-fix-them.md`

Status: Draft. This file records product implications only. It is not a durable decision.

## Product Thesis Implication

Module 3.3 turns RitmaOS from a static workspace generator into a guided setup and validation system.

The product should not only create folders and markdown files. It should help users avoid common architecture mistakes:

```text
too much context
missing routing
too many workspaces
context files about AI instead of the work
stale context
flat folders
overbuilding before use
```

## Potential Product Capability: Workspace Health Check

RitmaOS could include a validation layer that checks whether a workspace follows the architecture.

Possible checks:

| Check | Why it matters |
|---|---|
| CLAUDE.md length check | Prevents the routing file from becoming a brain dump. |
| Routing table presence check | Ensures task routing is explicit and repeatable. |
| Workspace count warning | Prevents overbuilt systems with too many workspaces. |
| Flat folder warning | Prevents “everything in one folder” setups. |
| CONTEXT.md freshness check | Helps users notice stale workspace context. |
| CONTEXT.md ratio check | Encourages work/project context over generic AI personality instructions. |
| Minimum viable setup path | Pushes users to start using the workspace before overdesigning it. |

## Product Capability: Setup Guardrails

During workspace creation, RitmaOS could ask only enough questions to produce a minimum viable folder system.

Possible onboarding rule:

```text
Start with 1 CLAUDE.md, 1–2 workspaces, and 1 CONTEXT.md per workspace.
Add more after real use.
```

This prevents users from spending too much time designing a perfect architecture before they know how they actually work.

## Product Capability: Context File Maintenance

RitmaOS could encourage or automate a “Last updated” line in context files.

Potential convention:

```markdown
Last updated: YYYY-MM-DD
```

Potential validation warning:

```text
This CONTEXT.md has not been updated in more than 30 days. Review before relying on it.
```

## Product Capability: Workspace Boundary Assistant

RitmaOS could include a boundary heuristic during setup:

```text
Is this a different mental mode, or just a stage inside the same workspace?
```

If it is a different mental mode, create a workspace.

If it is a stage/type/status inside the same work, create a subfolder instead.

## Product Capability: Anti-Overbuild Mode

The product should support a “start small” version that intentionally limits the first setup.

Example output:

```text
- CLAUDE.md
- workspace-1/CONTEXT.md
- workspace-2/CONTEXT.md
```

Then after a few runs, RitmaOS can suggest expansions based on observed use.

## Product Capability: Plain-English Error Messages

When validating a workspace, RitmaOS should explain architecture issues in non-technical language.

Examples:

```text
Your CLAUDE.md is doing too many jobs. Move project details into a workspace CONTEXT.md.

You may have too many workspaces. Drafting and editing look like stages of the same mode, not separate rooms.

This folder is too flat. Group related files into subfolders so the structure can do routing work.
```

## MVP Implication

A practical MVP should include:

```text
1. Workspace generator.
2. CLAUDE.md routing table generator.
3. CONTEXT.md generator.
4. Workspace health checker.
5. Minimal setup mode.
6. Index/manifest generator.
```

## Service Implication

For a done-for-you RitmaOS service, Module 3.3 becomes an audit checklist.

Possible service deliverable:

```text
RitmaOS Workspace Audit
```

Audit sections:

```text
- CLAUDE.md length and clarity
- routing table quality
- workspace boundary quality
- context freshness
- folder depth and organization
- overbuild risk
- missing context or missing naming conventions
```

## Decision Status

No durable decision is created by this module.

Potential future decision:

```text
Should RitmaOS include a formal workspace health checker in the MVP?
```
