# Module 4 Asset Inventory

Module: 4
Title: Practical Workspace Toolkit Bundle
Status: Asset staging inventory

This inventory records the downloadable source packages and PDFs exactly as received. It does not normalize filenames inside zips, rewrite package contents, extract PDF text, or unpack package contents into the repository as working files.

## Source Assets

| Asset | Original Local Source Path | Repo Target Path | SHA256 |
|---|---|---|---|
| `workspace-blueprint.zip` | `E:\Downloads\workspace-blueprint.zip` | `05_NEW_MODULES_INBOX/module-4/workspace-blueprint.zip` | `aea546f78aaf3516015c060516bd12df228657ce068c9f12df6730993d4d3b86` |
| `vault-toolkit.zip` | `E:\Downloads\vault toolkit.zip` | `05_NEW_MODULES_INBOX/module-4/vault-toolkit.zip` | `2f58b1fd81cd28d07c1b176bae1de1ef1152059a9b1493ff74090e635fa9435e` |
| `clief_notes_skills_field_manual_v1.pdf` | `E:\Downloads\clief_notes_skills_field_manual_v1.pdf` | `05_NEW_MODULES_INBOX/module-4/clief_notes_skills_field_manual_v1.pdf` | `cec3f3c26488bcd1a1fe7f6ce93a4f8fcd1753ef66f7c3793182e961043f165c` |
| `resource-index-claude-repos.pdf` | `E:\Downloads\clief_notes_resource_index_v1.pdf` | `05_NEW_MODULES_INBOX/module-4/resource-index-claude-repos.pdf` | `379ddcb4d5532b55aed3d37730046ff4abdcd59459a85ef45d543bcd6873eb4b` |

Note: the requested source path `E:\Downloads\414bc237-d3b7-4b56-9525-88c7e888727a.pdf` was not present locally. The available Resource Index PDF was found at `E:\Downloads\clief_notes_resource_index_v1.pdf` and staged under the requested repository filename.

## Raw Overview Files

| Raw File | Source Inside Package | Repo Target Path | SHA256 |
|---|---|---|---|
| `4-workspace-blueprint-full-template.md` | `workspace-blueprint.zip::workspace-blueprint/START-HERE.md` | `02_RAW_MODULES/4-workspace-blueprint-full-template.md` | `4ec0cb96a1660bd1c003e0f35b31c95cd31034f3d97236cba12a6cf5f809f85a` |
| `4-vault-toolkit-overview.md` | `vault toolkit.zip::README.md` | `02_RAW_MODULES/4-vault-toolkit-overview.md` | `8c55f5a5f6ebecfb149b11751bf338400393e21fca28c18914ec139cbe0dc783` |

Prompt Library raw text has not been staged because no exact raw Prompt Library source file or pasted source text was present locally during this update.

PDFs are staged as raw source assets only. They were not rewritten into markdown.

## PDF Inventory

| PDF | Title | Version/Date | Page Count | SHA256 |
|---|---|---|---|---|
| `clief_notes_skills_field_manual_v1.pdf` | Not available from local PDF metadata | Implied by filename: v1 | Not available from local tooling | `cec3f3c26488bcd1a1fe7f6ce93a4f8fcd1753ef66f7c3793182e961043f165c` |
| `resource-index-claude-repos.pdf` | Not available from local PDF metadata | Not available from local metadata | Not available from local tooling | `379ddcb4d5532b55aed3d37730046ff4abdcd59459a85ef45d543bcd6873eb4b` |

## Top-Level Contents: `workspace-blueprint.zip`

The package top-level contains:

```text
workspace-blueprint/
```

The `workspace-blueprint/` folder contains:

```text
CLAUDE.md
CONTEXT.md
START-HERE.md
claude-office-skills-ref/
community/
exmple.md
New folder/
New Text Document.txt
production/
writing-room/
_examples/
```

Note: the package also contains a nested `.git/` directory under `workspace-blueprint/claude-office-skills-ref/`. It is preserved inside the zip only and is not unpacked into the repository as working source.

## Top-Level Contents: `vault-toolkit.zip`

The package top-level contains:

```text
README.md
vault-toolkit.zip
```

The nested `vault-toolkit.zip` top-level contains:

```text
vault-toolkit/
```

The nested `vault-toolkit/` folder contains:

```text
README.md
architectures/
constraints/
skill-starters/
```

## Handling Notes

- The original downloadable zip and PDF files are preserved intact under `05_NEW_MODULES_INBOX/module-4/`.
- Package contents were inspected for inventory only.
- Package contents were not normalized, renamed, edited, or imported into the active repository structure.
- PDF contents were not extracted into markdown.
- Interpretation derived from these assets belongs outside raw and inbox locations.
