<!-- Copilot instructions for AI coding agents -->
# Repository snapshot

This repository contains small single-file Python exercises (Portuguese prompts) used for learning:

- `alurateste01.py` — compares two inputs
- `alurateste02.py` — simple while-loop growth simulation
- `alurateste03.py` — reads grades in a loop (interactive)
- `qualquercoisa.py` — empty placeholder

There is no packaging, tests, or external dependencies.

# Quick actions

- Run a script locally with: `python alurateste03.py` (Python 3).
- No build step or CI configured; don't add frameworks without approval.

# Project-specific patterns & conventions

- Files are small, single-purpose scripts. Prefer minimal, non-invasive changes.
- User-facing text and variable names are in Portuguese — preserve language in prompts unless instructed to translate.
- Scripts expect interactive `input()` and `print()` for I/O; when adding automation or tests, refactor I/O behind functions.

# What to change (guidance for AI agents)

- If asked to add features, implement them inside new functions and keep a small, clear runner block (protect with `if __name__ == '__main__':`).
- Avoid converting the repo into a package or adding dependencies unless the user requests it.
- When adding tests, create a new `tests/` folder and use plain `pytest`; keep tests focused on pure functions (refactor I/O first).

# Examples from this repo

- To make `alurateste03.py` testable: extract the input loop into a function like `collect_grades(input_fn)` so tests can inject inputs.
- Keep messages and prompts in Portuguese to match existing files (e.g., `Digite a nota:`).

# Integration points and external context

- No external services or libraries detected. README contains basic `git` commands — follow those for commits and pushes.

# When uncertain

- Ask the user before introducing project-wide changes (packaging, CI, linters, formatting rules).
- Confirm language changes for prompts/messages before translating Portuguese text.

# Reference files

- README.md for repository notes and `git` commands.
- The three Python scripts listed above for examples of current style and I/O patterns.

Please review this draft and tell me which areas need more detail or examples.
