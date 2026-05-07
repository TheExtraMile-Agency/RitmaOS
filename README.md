# RitmaOS

RitmaOS is a research and product-development operating system for exploring filesystem-based AI orchestration. It treats folders as memory, prompts as direction, specs as leverage, staged workflows as orchestration, outputs as reusable context, review checkpoints as reliability, and AI as a component inside a larger system.

This repository is not a finalized product spec. It is the source-of-truth workspace for research, source collection, synthesis, architecture design, templates, and product-development decisions.

## Current Status

RitmaOS is in research, source collection, and synthesis mode. Raw modules 1.2, 1.3, and 2.1 through 2.7 are stored. Product specs and architecture docs are drafts. No final MVP decision has been made.

GitHub is the master source of truth for this project.

## Repository Map

- `00_START_HERE/` explains how to navigate the repo and current status.
- `01_SOURCE_OF_TRUTH/` contains condensed working research and product assumptions.
- `02_RAW_MODULES/` contains immutable raw module source files.
- `03_EXTRACTED_FRAMEWORKS/` contains frameworks interpreted from raw modules.
- `04_PRODUCT_SPEC_DRAFTS/` contains draft product specifications and roadmaps.
- `05_NEW_MODULES_INBOX/` receives new raw module text before review.
- `06_DECISIONS_LOG/` records durable decisions.
- `07_SYNTHESIS_QUEUE/` tracks pending synthesis work and open questions.
- `08_WORKSPACE_ARCHITECTURE/` describes the working RitmaOS architecture.
- `09_TEMPLATES/` contains reusable templates and a starter workspace skeleton.
- `10_OPERATIONS/` documents repeatable operating workflows.
- `scripts/` contains maintenance scripts.

## Raw Module Rule

Files in `02_RAW_MODULES/` are immutable source material. Do not rewrite, summarize, edit, clean up, rename, delete, or reorganize raw module text. New raw modules may be added, but existing raw modules should remain preserved exactly.

## Adding a New Module

1. Create a new inbox file in `05_NEW_MODULES_INBOX/`.
2. Paste the raw module text exactly.
3. Do not summarize or extract frameworks in the same commit.
4. Update `02_RAW_MODULES/00_RAW_MODULES_INDEX.md` after the raw module is accepted into `02_RAW_MODULES/`.
5. Regenerate `PACKAGE_MANIFEST.md`.

## Extracting Frameworks

1. Read from `02_RAW_MODULES/` without modifying raw files.
2. Add extracted concepts to `03_EXTRACTED_FRAMEWORKS/`.
3. Mark extracted ideas as interpretation, not source text.
4. Update `03_EXTRACTED_FRAMEWORKS/00_FRAMEWORKS_INDEX.md`.

## Updating Product Specs

1. Treat `04_PRODUCT_SPEC_DRAFTS/` as draft product thinking.
2. Keep product implications separate from raw source material.
3. Update spec indexes when adding or changing spec files.
4. Record durable decisions in `06_DECISIONS_LOG/DECISIONS.md`.

## Recording Decisions

Use `06_DECISIONS_LOG/DECISIONS.md` for decisions that should survive across sessions. Product drafts are not decisions until they are recorded there.

## Architecture v2 Note

This repository previously used a nested `RitmaOS_Knowledge_Base/` folder.

As of architecture v2, the repo has been flattened:

- `01_SOURCE_OF_TRUTH/`
- `02_RAW_MODULES/`
- `03_EXTRACTED_FRAMEWORKS/`
- `04_PRODUCT_SPEC_DRAFTS/`

Raw module files were moved without modifying their contents.
