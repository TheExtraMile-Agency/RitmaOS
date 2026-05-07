from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PACKAGE_MANIFEST.md"
IGNORED_NAMES = {".git", "__pycache__", ".DS_Store", ".venv", "node_modules"}

DESCRIPTIONS = {
    ".gitignore": "Repository-local ignore rules for generated, local, and dependency files.",
    "README.md": "Root overview for the RitmaOS research and product-development operating system.",
    "AGENTS.md": "Operating instructions for AI coding and research agents.",
    "PACKAGE_MANIFEST.md": "Generated inventory of folders and files in this repository.",
    "00_START_HERE/": "Entry point for humans and AI agents.",
    "01_SOURCE_OF_TRUTH/": "Condensed working research and product assumptions.",
    "02_RAW_MODULES/": "Immutable raw module source files.",
    "03_EXTRACTED_FRAMEWORKS/": "Frameworks interpreted from raw source material.",
    "04_PRODUCT_SPEC_DRAFTS/": "Draft product specs, service specs, and roadmap notes.",
    "05_NEW_MODULES_INBOX/": "Inbox for newly collected raw module text before review.",
    "06_DECISIONS_LOG/": "Durable decisions separated from drafts and assumptions.",
    "07_SYNTHESIS_QUEUE/": "Pending questions, unresolved ideas, and synthesis work.",
    "08_WORKSPACE_ARCHITECTURE/": "Working architecture notes for filesystem-based orchestration.",
    "09_TEMPLATES/": "Reusable templates and a starter RitmaOS workspace skeleton.",
    "10_OPERATIONS/": "Human and AI operating workflows for maintaining the repository.",
    "scripts/": "Repository maintenance scripts.",
    "scripts/init_module.py": "Creates a new raw-module inbox file.",
    "scripts/update_manifest.py": "Regenerates this manifest from the repository file tree.",
    "scripts/validate_repo.py": "Checks required repository architecture and prints warnings.",
}


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_NAMES for part in path.parts)


def description_for(relative_path: str, is_dir: bool) -> str:
    key = f"{relative_path}/" if is_dir else relative_path
    if key in DESCRIPTIONS:
        return DESCRIPTIONS[key]
    if relative_path.startswith("02_RAW_MODULES/") and relative_path.endswith(".md"):
        if relative_path.endswith("00_RAW_MODULES_INDEX.md") or relative_path.endswith("README.md"):
            return "Raw module operating documentation."
        return "Raw module source file; preserve exactly."
    if relative_path.startswith("09_TEMPLATES/workspace-template/"):
        return "Starter workspace template asset."
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
