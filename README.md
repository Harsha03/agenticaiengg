---
title: Alter_EGO
app_file: src/app.py
sdk: gradio
sdk_version: 5.38.2
---
# agenticaiengg

A minimal Python project using the UV package manager.

## Structure

- `src/`: Source code and notebooks
- `tests/`: Unit tests
- `.env`: Environment variables (excluded from git)
- `.gitignore`: Standard Python ignores

## Setup

1. Create a virtual environment:
   ```sh
   uv venv
   ```
2. Install dependencies (editable mode):
   ```sh
   uv pip install -e .
   ```
3. Install Jupyter kernel:
   ```sh
   uv pip install ipykernel
   ```

## Example

Run the main module:
```sh
uv pip install -e .
python -m src.main
```
