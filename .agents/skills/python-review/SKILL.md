---
name: python-review
description: Review Python code for style and quality. Use when the user asks to "review Python code", "check Python style", "lint Python", or requests code quality analysis.
triggers:
  - python review
  - lint python
  - code quality
---

# Python Code Review

Review Python code against this project's standards.

## Workflow

1. **Run the automated checks**:
   ```bash
   ruff check .
   black --check .
   ```

2. **Check structure** — flag any function over 50 lines, or missing type
   hints on a public function.

3. **Check naming** — `snake_case` for functions and variables, `PascalCase`
   for classes, `UPPER_SNAKE` for constants.

4. **Verify tests exist** for any behavior you reviewed.

## Reporting

Report findings as a table with file, line, issue, and suggested fix. Lead
with the most serious issue. If you find nothing, say so explicitly rather
than inventing minor nits.

## Common Issues

| Issue | Fix |
|---|---|
| Mutable default argument | Use `None` and assign inside |
| Bare `except:` | Catch a specific exception |
| `== None` | Use `is None` |
| Unbounded loop | Add an explicit break condition |
