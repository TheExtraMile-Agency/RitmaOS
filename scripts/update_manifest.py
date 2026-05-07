from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PACKAGE_MANIFEST.md"
IGNORED_NAMES = {".git", "__pycache__", ".DS_Store", ".venv", "node_modules"}

DESCRIPTIONS = {
    ".gitignore": "Repository-local ignore rules for generated, local, and dependency files.",
    "README.md": "Root overview for the RitmaOS research knowledge base and workflow.",
    "AGENTS.md": "Operating instructions for AI coding and research agents.",
    "PACKAGE_MANIFEST.md": "Generated inventory of folders and files in this repository.",
    "04_NEW_MODULES_INBOX/": "Inbox for newly collected raw module text before review.",
    "04_NEW_MODULES_INBOX/README.md": "Instructions for adding new raw module text.",
    "05_DECISIONS_LOG/": "Durable decisions separated from working assumptions.",
    "05_DECISIONS_LOG/DECISIONS.md": "Decision log for repository and product-development decisions.",
    "07_SYNTHESIS_QUEUE/": "Queue for unresolved questions and pending synthesis work.",
    "07_SYNTHESIS_QUEUE/README.md": "Instructions for tracking pending synthesis work.",
    "07_SYNTHESIS_QUEUE/MODULES_TO_PROCESS.md": "Tracking table for module processing status.",
    "07_SYNTHESIS_QUEUE/QUESTIONS_FOR_SYNTHESIS.md": "Starter questions for future product and research synthesis.",
    "scripts/": "Small repository maintenance scripts.",
    "scripts/update_manifest.py": "Regenerates this manifest from the repository file tree.",
    "scripts/init_module.py": "Creates a new inbox markdown file for raw module intake.",
    "RitmaOS_Knowledge_Base/": "Original nested knowledge-base package; keep structure unless flattening is approved.",
    "RitmaOS_Knowledge_Base/README.md": "Original package-level overview.",
    "RitmaOS_Knowledge_Base/PACKAGE_MANIFEST.md": "Original package manifest from the nested knowledge-base bundle.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/": "Condensed product-facing research drafts and working assumptions.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/README.md": "Overview for the source-of-truth draft layer.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/00_SOURCE_OF_TRUTH.md": "Top-level source-of-truth draft.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/01_RESEARCH_NOTES.md": "Research notes derived from collected material.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/02_PRODUCT_THESIS.md": "Working product thesis.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/03_TARGET_CUSTOMER.md": "Working target-customer notes.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/04_FEATURES.md": "Working feature notes.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/05_MVP_SPEC.md": "Working MVP specification notes.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/06_BUSINESS_MODEL.md": "Working business-model notes.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/07_TERMINOLOGY.md": "Terminology notes.",
    "RitmaOS_Knowledge_Base/00_SOURCE_OF_TRUTH/08_OPEN_QUESTIONS.md": "Open research and product questions.",
    "RitmaOS_Knowledge_Base/01_RAW_MODULES/": "Raw source module layer; preserve files exactly.",
    "RitmaOS_Knowledge_Base/01_RAW_MODULES/00_RAW_MODULES_INDEX.md": "Index of raw modules currently stored.",
    "RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/": "Frameworks extracted from raw modules.",
    "RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/01_CORE_FRAMEWORKS.md": "Core extracted frameworks.",
    "RitmaOS_Knowledge_Base/02_EXTRACTED_FRAMEWORKS/02_RITMAOS_MAPPING.md": "Mapping from extracted frameworks to RitmaOS.",
    "RitmaOS_Knowledge_Base/03_PRODUCT_SPEC_DRAFTS/": "Early product-spec draft layer.",
    "RitmaOS_Knowledge_Base/03_PRODUCT_SPEC_DRAFTS/01_PRODUCT_SPEC_DRAFT.md": "Initial product-spec draft.",
}


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_NAMES for part in path.parts)


def description_for(relative_path: str, is_dir: bool) -> str:
    key = f"{relative_path}/" if is_dir else relative_path
    if key in DESCRIPTIONS:
        return DESCRIPTIONS[key]
    if relative_path.startswith("RitmaOS_Knowledge_Base/01_RAW_MODULES/"):
        return "Raw module source file; preserve exactly."
    return "Repository file."


def iter_entries() -> list[Path]:
    entries = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if should_skip(relative):
            continue
        entries.append(path)
    return sorted(entries, key=lambda item: item.relative_to(ROOT).as_posix().lower())


def build_manifest() -> str:
    lines = [
        "# Package Manifest",
        "",
        "This manifest is generated from the repository file tree. It lists the purpose of each folder and file. Raw module contents are not read or modified by the manifest script.",
        "",
        "## Repository Structure",
        "",
        "| Path | Type | Purpose |",
        "|---|---|---|",
    ]

    for path in iter_entries():
        relative = path.relative_to(ROOT).as_posix()
        is_dir = path.is_dir()
        path_label = f"{relative}/" if is_dir else relative
        entry_type = "Folder" if is_dir else "File"
        lines.append(f"| `{path_label}` | {entry_type} | {description_for(relative, is_dir)} |")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    MANIFEST.write_text(build_manifest(), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
