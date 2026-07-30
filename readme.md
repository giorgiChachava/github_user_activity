# GUA — GitHub User Activity

A small CLI that fetches and displays a GitHub user's recent public activity, right in your terminal.

## Installation

Requires Python 3.9+.

```bash
pip install -e .
```

This installs the `gua` command.

## Usage

```bash
gua <username>
```

Run it with no arguments to see the greeting and usage instructions:

```bash
gua
```

## Project structure

```
app/
  __init__.py
  main.py      # CLI entry point and argument handling
  visuals.py   # terminal typewriter output helpers
pyproject.toml # package metadata and the `gua` script entry point
```

## Development

The entry point is defined in [pyproject.toml](pyproject.toml):

```toml
[project.scripts]
gua = "app.main:main"
```

An editable install (`pip install -e .`) picks up code changes without reinstalling.
