# Demo Project — Repository Guidance

Always-on context. Everything here is loaded into the system prompt at the
start of every conversation in this repository.

## Purpose

A tiny demo app used to show how OpenHands skills are wired together.

## Setup

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## Layout

- `src/api/` — HTTP handlers
- `tests/` — test suite
- `.agents/skills/` — on-demand skills (loaded only when relevant)

## Conventions

- Run `pytest` before committing.
- Keep functions under 50 lines.
- Use type hints on public functions.

## Commands

| Task | Command |
|---|---|
| Test | `pytest -q` |
| Lint | `ruff check .` |
| Format | `black .` |
