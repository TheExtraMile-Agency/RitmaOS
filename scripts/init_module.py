import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "05_NEW_MODULES_INBOX"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def build_content(module: str, title: str) -> str:
    return "\n".join(
        [
            "---",
            f"module: {module}",
            f"title: {title}",
            "status: inbox",
            "source:",
            f"date_added: {date.today().isoformat()}",
            "---",
            "",
            "# Raw Module Text",
            "",
            "Paste the raw module text below this line. Do not summarize.",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new RitmaOS raw module inbox file.")
    parser.add_argument("module", help="Module number, such as 2.8")
    parser.add_argument("title", nargs="+", help="Module title")
    args = parser.parse_args()

    title = " ".join(args.title).strip()
    filename = f"{args.module}-{slugify(title)}.md"
    INBOX.mkdir(parents=True, exist_ok=True)
    target = INBOX / filename

    if target.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {target}")

    target.write_text(build_content(args.module, title), encoding="utf-8", newline="\n")
    print(target.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
