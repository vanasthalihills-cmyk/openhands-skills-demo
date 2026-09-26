---
name: api-validation
description: Validation rules for API handlers.
paths:
  - "src/api/**/*.py"
---

# API Validation Rules

These rules are injected the first time an API file is touched in a
conversation. They are not advertised to the model up front — the path match
triggers them.

## Required on every handler

1. **Validate input before use.** Reject unknown fields rather than ignoring
   them.
2. **Return explicit status codes.** Never return 200 for a failure.
3. **Never log secrets.** Redact tokens, passwords, and keys.
4. **Set a timeout** on every outbound call.

## Error shape

Every error response must use this shape:

```json
{"error": {"code": "string", "message": "string"}}
```
