# Module 3.1 — Folder Architecture Framework Extraction

Source module: `02_RAW_MODULES/3.1-the-full-walkthrough-folder-architecture.md`
Supporting reference: `Interpretable_Context_Methdology_.pdf`
Status: Extracted framework draft

## 1. Core Claim

A filesystem can act as the control surface for AI work. Instead of repeatedly prompting a model from scratch, the user creates a structured folder environment that tells the AI:

- where it is,
- what kind of work is happening,
- which files to read,
- which files to skip,
- where outputs belong,
- which tools or skills are relevant.

The important shift is from chat-as-session to workspace-as-system.

## 2. Three-Layer Routing Framework

### Layer 1 — The Map

File: `CLAUDE.md`

Purpose:

- identify the project,
- explain folder structure,
- define naming conventions,
- route task types to relevant folders/files,
- prevent irrelevant context from being loaded.

This layer answers: **where am I and where should I go?**

### Layer 2 — The Rooms

Files: workspace-level or room-level context files, usually `CONTEXT.md`.

Purpose:

- define what each workspace is for,
- define the process inside that workspace,
- explain what files live there,
- define workspace-specific rules,
- load only the context needed for that workspace.

This layer answers: **what kind of work happens here?**

### Layer 3 — The Tools

Files/folders: skills, MCP references, tool instructions, reusable process files.

Purpose:

- attach only the relevant tools to each workspace,
- avoid loading every skill into every task,
- make tools plug-and-play,
- allow workspaces to share reusable capabilities without merging contexts.

This layer answers: **what capabilities are available for this task?**

## 3. Workspace Slicing Framework

The system separates one project into intentional workspaces. The example module uses:

- `Community` — events, social, docs
- `Production` — projects, assets, codebase
- `Writing Room` — drafts, scripts, notes

The names are replaceable. The pattern is stable.

Equivalent mappings:

| User Type | Workspace 1 | Workspace 2 | Workspace 3 |
|---|---|---|---|
| Content creator | Script Lab | Edit Bay | Distribution Hub |
| Freelancer | Client Intake | Delivery | Admin |
| Developer | Frontend | Backend | Docs |
| RitmaOS customer | Intake | Production | Review/Delivery |

## 4. Context Minimization Principle

The module’s operational rule is:

> Load only what is relevant to the current task.

This creates a practical token strategy:

- do not put all project information into one conversation,
- do not force the AI to read unrelated workspaces,
- route by task type,
- load workspace-specific context only,
- attach tools only where needed.

The result is lower token waste and better task focus.

## 5. Naming Conventions as Lightweight Database

The module proposes that naming conventions can replace heavier database logic for many early workflows.

Examples:

- `api-auth-guide_draft.md`
- `2026-03-launch-week.md`
- `demo_v2.md`

Naming conventions allow the AI to infer:

- artifact type,
- status,
- version,
- date,
- location,
- next action.

This supports a no-database MVP: structured folders plus predictable file names.

## 6. Markdown as Universal Interface

Markdown is treated as the default file format because it is:

- readable by humans,
- readable by AI,
- plain text,
- Git-friendly,
- easy to edit in any text editor,
- structured enough for headings, lists, rules, and templates.

This supports the RitmaOS principle that the system should be inspectable and editable before it becomes software-heavy.

## 7. The Workspace-as-Agent Pattern

The deeper framework is not that the AI agent is smart by itself. The folder gives the agent its operating environment.

The workspace becomes a kind of externalized agent architecture:

- folder structure = routing logic,
- context files = role and task instructions,
- naming conventions = memory/indexing layer,
- output folders = state and handoff points,
- skills/tools = capability layer.

## 8. Productizable Unit

A productizable RitmaOS workspace should include:

1. root map file,
2. workspace/room context files,
3. naming conventions,
4. stage or room folders,
5. output locations,
6. tool/skill mappings,
7. rules for what to read/skip,
8. setup questionnaire or configuration file.

## 9. Relationship to MWP Paper

The uploaded ICM/MWP paper extends the 3.1 video pattern from three layers to a more formal five-layer architecture:

| Video 3.1 Pattern | MWP Paper Pattern | Meaning |
|---|---|---|
| Map | Layer 0 / Layer 1 | global identity and routing |
| Rooms | Layer 2 | stage/workspace contracts |
| Tools | Layer 3 | reference material, skills, conventions |
| Workspace outputs | Layer 4 | working artifacts |

The paper makes the architecture more precise by distinguishing stable reference material from per-run working artifacts.

## 10. Extracted RitmaOS Principle

RitmaOS should not be framed as “better prompts.”

It should be framed as:

> A filesystem-based operating layer for AI work, where folders, markdown, naming conventions, and scoped context turn one AI assistant into a repeatable workflow system.
