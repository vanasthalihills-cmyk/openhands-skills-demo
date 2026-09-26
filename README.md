# OpenHands Skills Demo

A minimal project showing the four ways to give OpenHands reusable context.

## What's here

| Path | Skill type | Loading behavior |
|---|---|---|
| `AGENTS.md` | Repository context | Always loaded, every conversation |
| `.agents/skills/release-checklist/SKILL.md` | Description-triggered | Name + description advertised; full text loaded on invocation |
| `.agents/skills/python-review/SKILL.md` | Keyword-triggered | Injected when a trigger word appears in your message |
| `.agents/skills/api-validation/SKILL.md` | Path-triggered rule | Injected when a matching file is read/edited/created |
| `src/api/users.py` | Sample target | Contains deliberate issues for demos |

## How to try each one

Open a conversation with this directory as the workspace.

**1. Repository context** — always active. Ask anything; the agent already
knows the test command and layout without being told.

> What command runs the tests here?

**2. Description-triggered skill** — activates on relevance.
> Help me cut a release.

The agent should invoke `release-checklist` and run its steps in order.

**3. Keyword-triggered skill** — activates on a literal word.
> Can you do a python review of this repo?

The word "python review" is a trigger, so `python-review` is injected.

**4. Path-triggered rule** — activates on file access, not on phrasing.
> Explain what src/api/users.py does.

Touching that path injects `api-validation`, so the agent knows the required
error shape and the "never log secrets" rule.

## Planted issues in `src/api/users.py`

Useful for testing whether `python-review` and `api-validation` actually fire:

1. **Secret logged** — `logger.info("creating user with token %s", token)`
2. **`== None`** — should be `is None`
3. **Dead branch** — the `name == None` check is unreachable; `name` was
   already validated above
4. **Missing timeout** — no outbound call, but the rule would apply if added

Expected: a review that cites the api-validation rule and reports these with
file and line.

## Scoping notes

- Project skills are resolved from the **conversation workspace**.
- Precedence: project > user (`~/.agents/skills/`) > public registry.
- Changing skill files requires a **new conversation** to rebuild the catalog.
- `.agents/skills/` is the standard location; `.openhands/skills/` is legacy.
