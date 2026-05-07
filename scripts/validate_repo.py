from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FOLDERS = [
    "00_START_HERE",
    "01_SOURCE_OF_TRUTH",
    "02_RAW_MODULES",
    "03_EXTRACTED_FRAMEWORKS",
    "04_PRODUCT_SPEC_DRAFTS",
    "05_NEW_MODULES_INBOX",
    "06_DECISIONS_LOG",
    "07_SYNTHESIS_QUEUE",
    "08_WORKSPACE_ARCHITECTURE",
    "09_TEMPLATES",
    "10_OPERATIONS",
    "scripts",
    "09_TEMPLATES/workspace-template",
    "09_TEMPLATES/workspace-template/stages/01-intake",
    "09_TEMPLATES/workspace-template/stages/02-analysis",
    "09_TEMPLATES/workspace-template/stages/03-draft",
    "09_TEMPLATES/workspace-template/stages/04-review",
    "09_TEMPLATES/workspace-template/stages/05-delivery",
    "09_TEMPLATES/workspace-template/shared",
    "09_TEMPLATES/workspace-template/skills",
    "09_TEMPLATES/workspace-template/memory",
    "09_TEMPLATES/workspace-template/review",
    "09_TEMPLATES/workspace-template/outputs",
]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "PACKAGE_MANIFEST.md",
    "00_START_HERE/README.md",
    "00_START_HERE/HOW_TO_USE_THIS_REPO.md",
    "00_START_HERE/CURRENT_STATUS.md",
    "02_RAW_MODULES/00_RAW_MODULES_INDEX.md",
    "03_EXTRACTED_FRAMEWORKS/00_FRAMEWORKS_INDEX.md",
    "04_PRODUCT_SPEC_DRAFTS/00_SPEC_INDEX.md",
    "06_DECISIONS_LOG/DECISIONS.md",
    "07_SYNTHESIS_QUEUE/MODULES_TO_PROCESS.md",
    "07_SYNTHESIS_QUEUE/QUESTIONS_FOR_SYNTHESIS.md",
    "scripts/init_module.py",
    "scripts/update_manifest.py",
    "scripts/validate_repo.py",
    "09_TEMPLATES/module-template.md",
    "09_TEMPLATES/framework-template.md",
    "09_TEMPLATES/decision-template.md",
    "09_TEMPLATES/product-spec-template.md",
]

RAW_MODULE_FILES = [
    "02_RAW_MODULES/1.2-your-first-folder.md",
    "02_RAW_MODULES/1.3-how-to-structure-any-prompt.md",
    "02_RAW_MODULES/2.1-video-text-guide-series-overview.md",
    "02_RAW_MODULES/2.2-one-line-of-python-triggers-12k-lines-of-code.md",
    "02_RAW_MODULES/2.3-how-a-1953-word-game-explains-ai-memory.md",
    "02_RAW_MODULES/2.4-the-ladder-that-explains-every-ai-failure.md",
    "02_RAW_MODULES/2.5-clawdbot-moltbot-has-100k-stars-zero-ai.md",
    "02_RAW_MODULES/2.6-video-as-code-my-ai-animation-stack.md",
    "02_RAW_MODULES/2.7-from-nazi-psychology-to-ai-auditing.md",
    "02_RAW_MODULES/3.1-the-full-walkthrough-folder-architecture.md",
]


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def main() -> None:
    warnings = 0

    for folder in REQUIRED_FOLDERS:
        if not (ROOT / folder).is_dir():
            warn(f"Missing required folder: {folder}")
            warnings += 1

    for file_path in REQUIRED_FILES:
        if not (ROOT / file_path).is_file():
            warn(f"Missing required file: {file_path}")
            warnings += 1

    for file_path in RAW_MODULE_FILES:
        if not (ROOT / file_path).is_file():
            warn(f"Missing expected raw module file: {file_path}")
            warnings += 1

    legacy = ROOT / "RitmaOS_Knowledge_Base"
    if legacy.exists():
        warn("Old nested RitmaOS_Knowledge_Base/ folder should not remain in v2 architecture.")
        warnings += 1

    if warnings:
        print(f"Validation completed with {warnings} warning(s).")
    else:
        print("Validation completed with no warnings.")


if __name__ == "__main__":
    main()
