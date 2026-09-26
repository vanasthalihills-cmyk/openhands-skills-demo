---
name: release-checklist
description: Prepare and verify a release. Use when the user asks to "cut a release", "prepare release notes", "publish a version", or mentions release checklist or version bumping.
---

# Release Checklist

Verify each item in order. Report the result of every step, including
failures — do not claim a step passed without showing its output.

## Workflow

1. **Confirm the version** — check the version in `pyproject.toml` and
   confirm it matches the intended release.

2. **Run the full test suite**:
   ```bash
   pytest -q
   ```

3. **Check the changelog** — ensure every user-visible change since the
   last tag is listed. Compare against:
   ```bash
   git log --oneline "$(git describe --tags --abbrev=0)..HEAD"
   ```

4. **Verify no uncommitted work**:
   ```bash
   git status --short
   ```

5. **Draft release notes** with three sections: Added, Changed, Fixed.

## Stop Conditions

Do not proceed past a failed step. Report the failure and ask how to
continue.
