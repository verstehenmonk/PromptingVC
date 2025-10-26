# Example: Bug Fix Review

This example demonstrates how to use the code review prompts for reviewing a bug fix.

## System Prompt
Use: `system/code-review-assistant.md`

## User Prompt

Please review the following pull request:

**PR Title**: Fix null pointer exception in user authentication
**Author**: jane.doe
**Description**: This PR fixes a null pointer exception that occurs when a user tries to log in with an empty password field.

## Changes

```python
# Before
def authenticate(username, password):
    hashed = hash_password(password)
    return db.query(username, hashed)

# After
def authenticate(username, password):
    if not password:
        raise ValueError("Password cannot be empty")
    hashed = hash_password(password)
    return db.query(username, hashed)
```

## Context

- Repository: myapp/backend
- Branch: fix/auth-null-pointer
- Related Issues: #123

Please provide a comprehensive code review focusing on code quality, potential bugs, and adherence to best practices.

## Expected Output

The AI should provide feedback on:
- The fix implementation
- Additional edge cases to consider
- Potential improvements
- Testing recommendations
