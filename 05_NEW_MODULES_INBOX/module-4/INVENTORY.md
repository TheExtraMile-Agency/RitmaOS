# Module 4 Asset Inventory

Module: 4
Title: Workspace Blueprint / Vault Toolkit Practical Asset Package
Status: Asset staging inventory

This inventory records the downloadable source packages exactly as received. It does not normalize filenames, rewrite package contents, or unpack package contents into the repository as working files.

## Source Packages

| Package | Original Local Source Path | Repo Target Path | SHA256 |
|---|---|---|---|
| `workspace-blueprint.zip` | `E:\Downloads\workspace-blueprint.zip` | `05_NEW_MODULES_INBOX/module-4/workspace-blueprint.zip` | `aea546f78aaf3516015c060516bd12df228657ce068c9f12df6730993d4d3b86` |
| `vault-toolkit.zip` | `E:\Downloads\vault toolkit.zip` | `05_NEW_MODULES_INBOX/module-4/vault-toolkit.zip` | `2f58b1fd81cd28d07c1b176bae1de1ef1152059a9b1493ff74090e635fa9435e` |

## Raw Overview Files

| Raw File | Source Inside Package | Repo Target Path | SHA256 |
|---|---|---|---|
| `4-workspace-blueprint-full-template.md` | `workspace-blueprint.zip::workspace-blueprint/START-HERE.md` | `02_RAW_MODULES/4-workspace-blueprint-full-template.md` | `4ec0cb96a1660bd1c003e0f35b31c95cd31034f3d97236cba12a6cf5f809f85a` |
| `4-vault-toolkit-overview.md` | `vault toolkit.zip::README.md` | `02_RAW_MODULES/4-vault-toolkit-overview.md` | `8c55f5a5f6ebecfb149b11751bf338400393e21fca28c18914ec139cbe0dc783` |

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

- The original downloadable zip files are preserved intact under `05_NEW_MODULES_INBOX/module-4/`.
- Package contents were inspected for inventory only.
- Package contents were not normalized, renamed, edited, or imported into the active repository structure.
- Interpretation derived from these assets belongs outside raw and inbox locations.
