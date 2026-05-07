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

    legacy = ROOT / "RitmaOS_Knowledge_Base"
    if legacy.exists():
        contents = list(legacy.iterdir()) if legacy.is_dir() else [legacy]
        if contents:
            warn("Legacy RitmaOS_Knowledge_Base/ folder remains because it still contains files.")
            warnings += 1
        else:
            warn("Legacy RitmaOS_Knowledge_Base/ folder is empty and can be removed.")
            warnings += 1

    if warnings:
        print(f"Validation completed with {warnings} warning(s).")
    else:
        print("Validation completed with no warnings.")


if __name__ == "__main__":
    main()
