# AGENTS.md

These instructions apply to AI coding and research agents working in this repository.

## Core Rules

- Preserve raw module text exactly.
- Do not rewrite, summarize, rename, delete, or reorganize raw source files.
- Do not treat working assumptions as final product decisions.
- Separate raw material, extracted frameworks, product drafts, and decisions.
- Prefer additive changes over destructive edits.
- Before changing repository structure, explain the proposed change and wait for explicit approval.
- Always update the manifest or relevant index when adding files.

## Repository Layers

- Raw source material currently lives in `RitmaOS_Knowledge_Base/01_RAW_MODULES/`.
- Extracted frameworks currently live in `RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/`.
- Product drafts currently live in `RitmaOS_Knowledge_Base/03_PRODUCT_SPEC_DRAFTS/`.
- Condensed source-of-truth drafts currently live in `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/`.
- Decisions live in `05_DECISIONS_LOG/DECISIONS.md`.
- New module intake starts in `04_NEW_MODULES_INBOX/`.
- Pending synthesis work lives in `07_SYNTHESIS_QUEUE/`.

## Commit Discipline

When processing a new module, use separate commits for:

1. Raw source addition.
2. Extracted frameworks.
3. Product thesis or spec updates.

Do not combine raw source preservation with interpretation-heavy edits.

## Working With Modules

- Put new raw text in `04_NEW_MODULES_INBOX/` first.
- Preserve exact wording, ordering, headings, and formatting in raw module files.
- Move reviewed raw files into `RitmaOS_Knowledge_Base/01_RAW_MODULES/` only when instructed.
- Extract frameworks into `RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/`.
- Add product implications only after analysis.

## Safety

If a requested change could affect raw source material or repository structure, stop and explain the risk before proceeding.
