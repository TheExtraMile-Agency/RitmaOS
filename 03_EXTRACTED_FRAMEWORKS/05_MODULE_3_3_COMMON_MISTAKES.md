# Module 3.3 Framework Extraction: Common Mistakes and How to Fix Them

Source module: `02_RAW_MODULES/3.3-common-mistakes-and-how-to-fix-them.md`

## Core Framework

Module 3.3 turns the folder architecture into a practical diagnostic system. It identifies the most common ways users break the architecture and gives correction rules for each one.

The underlying pattern is:

```text
Keep the system small.
Keep each layer doing only its job.
Keep context focused on the work.
Update the system as real work changes.
Grow from use, not from planning.
```

## Seven Mistakes Framework

| Mistake | Failure Mode | Correction |
|---|---|---|
| CLAUDE.md too long | Routing signal gets buried; tokens are wasted on irrelevant context. | Keep CLAUDE.md to identity, folder structure, routing table, and naming conventions. Move detail into workspace CONTEXT.md files. |
| Skipping the routing table | Claude guesses where to go and what to read; output becomes inconsistent. | Add a simple routing table with task, destination, and files to read. Add a skills column only when needed. |
| Too many workspaces | System maintenance becomes heavier than the work; context files go stale. | Start with two or three workspaces. Split only when there is a real mental-mode boundary. |
| Context files describe Claude instead of the work | Personality instructions dominate; actual project context is thin. | Use the context file as a project brief. Spend most of the file on audience, work, constraints, examples, and what good output looks like. |
| Never updating context files | Claude works from stale constraints and old assumptions. | Treat context files as living notes. Update them whenever the project changes. Consider a “Last updated” line. |
| Everything in one flat folder | Folder architecture cannot signal what belongs together; Claude picks wrong files. | Use subfolders when there are more than 8–10 files at the same level. Group by workspace, then by stage/type. |
| Building the whole system before using it | The user overbuilds based on theory, then discovers the structure does not match actual work. | Build a minimum version first: one CLAUDE.md, one or two workspaces, one CONTEXT.md per workspace. Grow from real use. |

## Diagnostic Rule

If the architecture feels heavy, confusing, or slow, check whether one of the layers is doing another layer’s job:

```text
CLAUDE.md = map
CONTEXT.md = room
Skills/tools = tools
Folders = architecture
Raw work/output = material
```

Each layer should stay focused on its own function.

## Workspace Boundary Heuristic

A task deserves its own workspace only if it represents a different mental mode or requires different context boundaries.

Examples:

```text
Writing vs building = likely separate workspaces.
Drafting vs editing = likely one workspace with stages/process.
Client A vs Client B = separate workspaces to prevent context bleed.
Research notes vs drafts = usually subfolders, not separate workspaces.
```

## Context File Quality Heuristic

A strong CONTEXT.md should read like a project brief that a new teammate could use to start work.

It should prioritize:

- what the project/workspace is for
- who the audience/customer/user is
- what good work looks like
- what constraints matter
- what has changed recently
- what to avoid
- what files live here and why

It should not primarily be a list of generic personality instructions.

## Build-Minimum-Then-Grow Pattern

Recommended setup sequence:

```text
1. Create one CLAUDE.md.
2. Create one or two workspaces.
3. Add one CONTEXT.md per workspace.
4. Start using the system.
5. Observe where Claude gets confused.
6. Update context files.
7. Add folders, workspaces, routing rows, or skills only when real use proves they are needed.
```

## Relationship to Earlier Modules

- 3.1 defines the architecture: map, rooms, tools.
- 3.2 shows how to customize it by use case.
- 3.3 adds guardrails and diagnostics so users do not overbuild, flatten, or stale-date the architecture.

## RitmaOS Extraction

For RitmaOS, this module suggests that the product should not only generate a workspace. It should also validate and coach the workspace over time.

Potential reusable framework name:

```text
Workspace Health Check Framework
```

Core checks:

```text
- Is CLAUDE.md short enough?
- Is there a routing table?
- Are there too many workspaces?
- Are context files work-focused?
- Are context files recently updated?
- Are folder levels too flat?
- Is the setup minimal enough to use immediately?
```
