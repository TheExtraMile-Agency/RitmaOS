# RitmaOS — Product Spec Draft

## Product definition

RitmaOS is a filesystem-based orchestration layer for AI-powered business work.

It turns a business process into a structured workspace where AI can read context, follow staged prompts, produce outputs, pass through review, and update memory.

## MVP

The MVP is a workspace generator, not a full SaaS app.

## MVP command concept

```bash
ritma init
```

The generator asks a guided questionnaire and creates a business-specific workspace.

## Generated workspace

```text
RitmaOS-Workspace/
  00_START_HERE.md
  CLAUDE.md
  CONTEXT.md
  REFERENCES.md
  01_IDENTITY/
    BUSINESS_PROFILE.md
    VOICE.md
    RULES.md
  02_BUSINESS_CONTEXT/
    SERVICES.md
    CUSTOMERS.md
    OFFERS.md
    TOOLS.md
  03_REFERENCES/
    examples/
    links/
    past-work/
  04_WORKFLOWS/
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
        REVIEW_CHECKLIST.md
        CHANGES_REQUESTED.md
        APPROVAL_NOTES.md
      05-delivery/
        DELIVERY_PROMPT.md
        output/
  05_PROMPTS/
  06_OUTPUTS/
  07_REVIEW/
  08_MEMORY/
  09_METRICS/
```

## MVP workflow types to consider

- Website/client intake to proposal
- Marketing content production
- Property-management tenant communication
- AI agency client onboarding
- SOP creation from messy notes
- Customer FAQ / knowledge base creation

## Core jobs-to-be-done

1. Capture business context once.
2. Turn repeatable work into stages.
3. Give AI the right context at each stage.
4. Save outputs outside chat history.
5. Require human review where needed.
6. Convert useful results into memory.
7. Improve the workflow over time.

## Success criteria

A user can open the generated folder and understand:

- what the workflow does
- what the AI should read
- what prompt to run
- where inputs go
- where outputs go
- what needs human review
- what should become memory
