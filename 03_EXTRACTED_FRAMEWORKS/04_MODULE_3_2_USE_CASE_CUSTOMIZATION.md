# Module 3.2 Framework Extraction: Use-Case Customization

Source raw module: `02_RAW_MODULES/3.2-customizing-for-your-use-case.md`

## Core Framework

Module 3.2 extends the folder architecture from 3.1 by showing that the structure is stable while the labels are variable.

The stable layers are:

1. `CLAUDE.md` at the project root as the routing and identity layer.
2. Workspace folders as bounded work areas.
3. `CONTEXT.md` inside each workspace as local instructions, process, rules, and scope.
4. Skills/tools wired only into the workspaces where they are relevant.

The variable layer is the user's domain language:

- Content creators may use `script-lab/`, `production/`, and `distribution/`.
- Consultants may use one folder per client, plus `templates/` and `business-dev/`.
- Developers may use `planning/`, `src/`, `docs/`, and `ops/`.

## Extracted Principles

### 1. Same Layers, Different Labels

The architecture is not a fixed folder template. It is a repeatable pattern that changes vocabulary based on the user's work.

### 2. Workspace Boundary = Context Boundary

A workspace exists where the user shifts mode, task type, audience, client, or context. If the user wants the AI to “forget” the previous mode and focus on something else, that is evidence of a workspace boundary.

### 3. `CONTEXT.md` Is Local Operating Memory

Each workspace’s `CONTEXT.md` defines:

- what happens in the workspace
- the process followed there
- what files live there
- what good work looks like
- what to avoid
- which tools/skills apply

### 4. Routing Table Is the Control Surface

The top-level `CLAUDE.md` maps tasks to workspace folders and context files. This lets the AI route itself without loading irrelevant material.

### 5. Client Isolation Prevents Context Bleed

For consultants and agencies, each client should have its own context and folder boundary. The AI should not reference one client’s information while working in another client’s workspace.

### 6. Templates Are Reusable Source Material, Not Client Output

Reusable templates, proposals, reports, and frameworks should live outside individual client folders and be copied/customized into the relevant client workspace.

### 7. Skills Are Scoped by Workspace

Skills/tools should not be globally loaded. They should be referenced only where useful, such as testing skills inside a code workspace or doc-authoring skills inside a documentation workspace.

### 8. Context Files Are Living Documents

The system improves as users edit `CONTEXT.md` files based on what the AI gets right or wrong. Context files are not one-time setup documents; they are operational memory.

## Repeatable Customization Process

1. List 2–4 major workspaces.
2. Write a `CONTEXT.md` for each workspace.
3. Write root `CLAUDE.md` with workspace list, routing table, and naming conventions.
4. Start working.
5. Observe AI failures and update context files.

## RitmaOS Mapping

For RitmaOS, this module supports an archetype-driven setup system:

- user selects a work type
- RitmaOS proposes workspace labels
- RitmaOS generates `CLAUDE.md`
- RitmaOS generates one `CONTEXT.md` per workspace
- RitmaOS adds naming conventions
- RitmaOS optionally wires skills/tools into the relevant workspace only

This should remain an extracted framework, not a durable decision, unless explicitly accepted in `06_DECISIONS_LOG/DECISIONS.md`.
