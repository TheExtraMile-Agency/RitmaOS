# RitmaOS — MVP Spec

## MVP goal

Create the simplest useful version of RitmaOS: a workspace generator that turns one business workflow into an AI-readable folder system.

## MVP user journey

1. User chooses a workflow type or custom workflow.
2. User answers a guided questionnaire.
3. RitmaOS generates a folder workspace.
4. User opens the workspace in Claude Code, Cursor, VS Code, or uploads it to an AI Project.
5. User runs the workflow one stage at a time.
6. Outputs are saved and reviewed.
7. Useful learning is copied into memory files.

## MVP inputs

The user provides:

- Business name
- Business type
- Main services
- Target customer
- Workflow to improve
- Current process
- Inputs used in that process
- Expected output
- Tone and quality rules
- Mistakes to avoid
- Review/approval requirements

## MVP outputs

RitmaOS generates:

```text
RitmaOS-Workspace/
  00_START_HERE.md
  CLAUDE.md
  CONTEXT.md
  REFERENCES.md
  01_IDENTITY/
  02_BUSINESS_CONTEXT/
  03_REFERENCES/
  04_WORKFLOWS/
  05_PROMPTS/
  06_OUTPUTS/
  07_REVIEW/
  08_MEMORY/
  09_METRICS/
```

## MVP workflow structure

Each workflow folder contains:

```text
workflow-name/
  00_WORKFLOW_OVERVIEW.md
  01-intake/
    CONTEXT.md
    PROMPT.md
    CHECKLIST.md
    input/
    output/
  02-analysis/
    CONTEXT.md
    PROMPT.md
    CHECKLIST.md
    input/
    output/
  03-draft/
    CONTEXT.md
    PROMPT.md
    CHECKLIST.md
    input/
    output/
  04-review/
    CONTEXT.md
    PROMPT.md
    CHECKLIST.md
    input/
    output/
  05-delivery/
    CONTEXT.md
    PROMPT.md
    CHECKLIST.md
    input/
    output/
```

## MVP success criteria

The MVP is successful if:

- A user can generate a workspace in under 10 minutes
- The workspace can be used immediately with an AI model
- The AI gives more specific outputs than a cold chat
- The workflow is understandable by looking at the folder structure
- Outputs are saved outside chat history
- Human review is clearly built into the workflow

## MVP build options

### Option A: Manual template

Start with a downloadable folder template and onboarding questionnaire.

### Option B: Script generator

A local script asks questions and writes markdown files.

### Option C: Simple web generator

A web form creates a downloadable zip file.

## Recommended first build

Start with Option B or C.

A script or simple web generator is enough to prove value without overbuilding SaaS features too early.
