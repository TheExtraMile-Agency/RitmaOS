# RitmaOS — Feature Map

## MVP features

### 1. Workspace generator

Creates a structured folder system for a specific business or workflow.

### 2. Intake questionnaire

Collects business context before generating the workspace.

Questions cover:

- Business type
- Services
- Customers
- Tone/voice
- Current workflow
- Pain points
- Inputs
- Outputs
- Review requirements
- Tools used

### 3. Core context files

Generated files:

- `CLAUDE.md`
- `CONTEXT.md`
- `REFERENCES.md`
- `BUSINESS_PROFILE.md`
- `VOICE.md`
- `RULES.md`

### 4. Workflow stages

Each workflow has numbered stages:

```text
01-intake/
02-analysis/
03-draft/
04-review/
05-delivery/
```

Each stage includes:

- `CONTEXT.md`
- `PROMPT.md`
- `CHECKLIST.md`
- `references/`
- `input/`
- `output/`

### 5. Review checkpoints

Important outputs must pass through human review.

Review files may include:

- `REVIEW_CHECKLIST.md`
- `APPROVAL_NOTES.md`
- `CHANGES_REQUESTED.md`

### 6. Output storage

Every completed output is saved in an organized location instead of being lost inside chat history.

### 7. Memory capture

Useful decisions, examples, and lessons are moved into memory files.

Examples:

- `WHAT_WORKED.md`
- `CLIENT_PREFERENCES.md`
- `COMMON_MISTAKES.md`
- `APPROVED_EXAMPLES.md`

## Later features

### CLI

Commands like:

```text
ritma init
ritma workflow add
ritma stage add
ritma memory update
ritma audit
```

### Web app

A simple interface for generating, editing, and running workspaces.

### Integrations

Possible integrations:

- Claude Projects
- Claude Code
- ChatGPT Projects
- Google Drive
- Notion
- GitHub
- Gmail
- Google Calendar
- Zapier/Make
- MCP servers

### Metrics

Track:

- Time saved
- Number of outputs created
- Review pass/fail
- Common corrections
- Prompt effectiveness
- Workflow bottlenecks

### Workspace audit

Checks whether a workspace is healthy:

- Missing context
- Outdated files
- Unused prompts
- Broken workflow stages
- No review process
- Outputs not saved
