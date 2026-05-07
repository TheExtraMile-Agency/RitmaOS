# RitmaOS Knowledge Base

RitmaOS is a working research thesis about filesystem-based AI orchestration. It explores folders as memory, prompts as direction, specs as leverage, staged workflows as orchestration, outputs as reusable context, review checkpoints as reliability, and AI as one component in a larger operating system rather than the whole system.

This is not a finalized product definition. The repository is the durable source of truth for collecting raw source material, extracting repeatable frameworks, and gradually turning those frameworks into product assumptions, specifications, and decisions.

## Repository Purpose

This repo exists so ChatGPT, Claude, Codex, and human collaborators can work from the same versioned filesystem. It should preserve source material exactly, keep analysis separate from raw text, and make product-development work traceable through commits.

## Current Status

The project is in research, source collection, and synthesis. Product specs, MVP notes, business model ideas, and architecture ideas are working assumptions only.

## Current Structure Note

The repository currently contains an extra nested top-level folder:

`RitmaOS_Knowledge_Base/`

The raw modules currently live inside:

`RitmaOS_Knowledge_Base/01_RAW_MODULES/`

Do not flatten this structure unless the repository owner explicitly approves it in a separate change.

## Adding New Modules

1. Add new raw lesson or module text first to `04_NEW_MODULES_INBOX/`.
2. Preserve the raw text exactly as received.
3. After review, move the raw module into `RitmaOS_Knowledge_Base/01_RAW_MODULES/`.
4. Update `RitmaOS_Knowledge_Base/01_RAW_MODULES/00_RAW_MODULES_INDEX.md`.
5. Update `PACKAGE_MANIFEST.md`.
6. Commit raw source additions separately from synthesis or product-spec changes.

## Extracting Frameworks

1. Read raw modules from `RitmaOS_Knowledge_Base/01_RAW_MODULES/`.
2. Do not edit the raw module files.
3. Extract reusable concepts, patterns, workflows, or operating principles into `RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/`.
4. Keep extracted frameworks clearly labeled as interpretations, not source text.
5. Commit framework extraction separately from raw additions and product-spec updates.

## Updating Product Specs

1. Treat files in `RitmaOS_Knowledge_Base/03_PRODUCT_SPEC_DRAFTS/` and `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/` as draft synthesis.
2. Product claims should point back to raw modules or extracted frameworks when possible.
3. Record durable decisions in `05_DECISIONS_LOG/DECISIONS.md`.
4. Keep assumptions and decisions separate.

## Raw Source Warning

Raw source files must not be edited, rewritten, summarized, renamed, deleted, or reorganized as part of synthesis work. Preserve them exactly.
