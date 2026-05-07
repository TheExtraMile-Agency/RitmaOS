# Package Manifest

This manifest is generated from the repository file tree. It lists the purpose of each folder and file. Raw module contents are not read or modified by the manifest script.

## Repository Structure

| Path | Type | Purpose |
|---|---|---|
| `.gitignore` | File | Repository-local ignore rules for generated, local, and dependency files. |
| `04_NEW_MODULES_INBOX/` | Folder | Inbox for newly collected raw module text before review. |
| `04_NEW_MODULES_INBOX/README.md` | File | Instructions for adding new raw module text. |
| `05_DECISIONS_LOG/` | Folder | Durable decisions separated from working assumptions. |
| `05_DECISIONS_LOG/DECISIONS.md` | File | Decision log for repository and product-development decisions. |
| `07_SYNTHESIS_QUEUE/` | Folder | Queue for unresolved questions and pending synthesis work. |
| `07_SYNTHESIS_QUEUE/MODULES_TO_PROCESS.md` | File | Tracking table for module processing status. |
| `07_SYNTHESIS_QUEUE/QUESTIONS_FOR_SYNTHESIS.md` | File | Starter questions for future product and research synthesis. |
| `07_SYNTHESIS_QUEUE/README.md` | File | Instructions for tracking pending synthesis work. |
| `AGENTS.md` | File | Operating instructions for AI coding and research agents. |
| `README.md` | File | Root overview for the RitmaOS research knowledge base and workflow. |
| `RitmaOS_Knowledge_Base/` | Folder | Original nested knowledge-base package; keep structure unless flattening is approved. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/` | Folder | Condensed product-facing research drafts and working assumptions. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/00_SOURCE_OF_TRUTH.md` | File | Top-level source-of-truth draft. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/01_RESEARCH_NOTES.md` | File | Research notes derived from collected material. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/02_PRODUCT_THESIS.md` | File | Working product thesis. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/03_TARGET_CUSTOMER.md` | File | Working target-customer notes. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/04_FEATURES.md` | File | Working feature notes. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/05_MVP_SPEC.md` | File | Working MVP specification notes. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/06_BUSINESS_MODEL.md` | File | Working business-model notes. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/07_TERMINOLOGY.md` | File | Terminology notes. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/08_OPEN_QUESTIONS.md` | File | Open research and product questions. |
| `RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/README.md` | File | Overview for the source-of-truth draft layer. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/` | Folder | Raw source module layer; preserve files exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/00_RAW_MODULES_INDEX.md` | File | Index of raw modules currently stored. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/1.2-your-first-folder.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/1.3-how-to-structure-any-prompt.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.1-video-text-guide-series-overview.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.2-one-line-of-python-triggers-12k-lines-of-code.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.3-how-a-1953-word-game-explains-ai-memory.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.4-the-ladder-that-explains-every-ai-failure.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.5-clawdbot-moltbot-has-100k-stars-zero-ai.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.6-video-as-code-my-ai-animation-stack.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/01_RAW_MODULES/2.7-from-nazi-psychology-to-ai-auditing.md` | File | Raw module source file; preserve exactly. |
| `RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/` | Folder | Frameworks extracted from raw modules. |
| `RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/01_CORE_FRAMEWORKS.md` | File | Core extracted frameworks. |
| `RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/02_RITMAOS_MAPPING.md` | File | Mapping from extracted frameworks to RitmaOS. |
| `RitmaOS_Knowledge_Base/03_PRODUCT_SPEC_DRAFTS/` | Folder | Early product-spec draft layer. |
| `RitmaOS_Knowledge_Base/03_PRODUCT_SPEC_DRAFTS/01_PRODUCT_SPEC_DRAFT.md` | File | Initial product-spec draft. |
| `RitmaOS_Knowledge_Base/PACKAGE_MANIFEST.md` | File | Original package manifest from the nested knowledge-base bundle. |
| `RitmaOS_Knowledge_Base/README.md` | File | Original package-level overview. |
| `scripts/` | Folder | Small repository maintenance scripts. |
| `scripts/init_module.py` | File | Creates a new inbox markdown file for raw module intake. |
| `scripts/update_manifest.py` | File | Regenerates this manifest from the repository file tree. |
