# AGENTS.md

These instructions apply to AI coding, research, and documentation agents working in this repository.

## Critical Rules

- Preserve raw module text exactly.
- Never edit files in `02_RAW_MODULES/` unless explicitly adding a new raw module.
- Do not rewrite, summarize, clean up, rename, delete, or reorganize existing raw modules.
- Separate raw material, extracted frameworks, product drafts, architecture docs, templates, operations docs, and decisions.
- Do not treat product drafts as final decisions.
- Use `06_DECISIONS_LOG/DECISIONS.md` for durable decisions.
- Prefer additive commits.
- Ask before destructive changes.
- Update `PACKAGE_MANIFEST.md` after structural changes.
- Update relevant indexes after adding files.

## Repository Layers

- `00_START_HERE/` is the entry point.
- `01_SOURCE_OF_TRUTH/` contains condensed working assumptions.
- `02_RAW_MODULES/` contains immutable raw source material.
- `03_EXTRACTED_FRAMEWORKS/` contains interpretations extracted from raw material.
- `04_PRODUCT_SPEC_DRAFTS/` contains draft product specifications.
- `05_NEW_MODULES_INBOX/` is for new raw material before review.
- `06_DECISIONS_LOG/` contains durable decisions.
- `07_SYNTHESIS_QUEUE/` tracks unresolved synthesis work.
- `08_WORKSPACE_ARCHITECTURE/` describes the working architecture.
- `09_TEMPLATES/` contains reusable templates.
- `10_OPERATIONS/` contains operating workflows.

## Commit Discipline

When processing a new module, use separate commits for:

1. Raw source addition.
2. Extracted frameworks.
3. Product thesis or spec updates.
4. Durable decisions, if any.

Do not combine raw source preservation with interpretation-heavy edits.

## Structure Changes

Before changing folder architecture, explain the proposed change, why it is needed, and what files will move. Wait for explicit approval.

## Raw Module Handling

New raw module text starts in `05_NEW_MODULES_INBOX/`. After review, it can be moved into `02_RAW_MODULES/`, then indexed in `02_RAW_MODULES/00_RAW_MODULES_INDEX.md`.

Existing raw modules are source evidence, not editable drafts.
