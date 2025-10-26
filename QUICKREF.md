# PromptingVC Quick Reference

## Installation
```bash
pip install -r requirements.txt
pip install -e .
```

## Basic Commands

### Create a prompt
```bash
# From inline content
promptvc create <id> <project> "<name>" -c "<content>" -a "<author>"

# From file
promptvc create <id> <project> "<name>" -f <file.txt> -a "<author>"

# With tags and description
promptvc create <id> <project> "<name>" -f <file.txt> -d "<description>" -t tag1 -t tag2
```

### List prompts
```bash
# All prompts
promptvc list

# Filter by project
promptvc list --project <project-name>
```

### View a prompt
```bash
promptvc show <prompt-id>
```

### Update a prompt
```bash
# From inline content
promptvc update <prompt-id> -c "<new content>" -m "commit message"

# From file
promptvc update <prompt-id> -f <file.txt> -m "commit message"
```

### Version history
```bash
# View all versions
promptvc history <prompt-id>

# View specific version
promptvc checkout <prompt-id> <version-number>
```

### Projects
```bash
promptvc projects
```

### AI Features (requires OPENAI_API_KEY)
```bash
# Analyze a prompt
promptvc analyze <prompt-id>

# Improve a prompt
promptvc improve <prompt-id>

# Improve with specific goals
promptvc improve <prompt-id> -g "make it more concise"

# Preview without saving
promptvc improve <prompt-id> --preview
```

### Delete a prompt
```bash
promptvc delete <prompt-id>
```

## Common Workflows

### Creating a new project with prompts
```bash
# Create first prompt for the project
promptvc create pr-reviewer code-tools "PR Reviewer" \
  -c "Review this pull request and provide feedback..." \
  -d "Automated PR review assistant" \
  -t code-review -t automation

# Add more prompts to the same project
promptvc create bug-finder code-tools "Bug Finder" \
  -c "Analyze this code for potential bugs..." \
  -t debugging
```

### Iterating on a prompt
```bash
# Create initial version
promptvc create my-prompt project "My Prompt" -c "Initial version"

# Make improvements
promptvc update my-prompt -c "Improved version" -m "Added clarity"
promptvc update my-prompt -c "Even better version" -m "Added examples"

# Review history
promptvc history my-prompt

# Go back to previous version if needed
promptvc checkout my-prompt 1
```

### Using AI to improve prompts
```bash
# Set API key (one time)
export OPENAI_API_KEY='sk-...'

# Analyze the prompt
promptvc analyze my-prompt

# Preview improvement
promptvc improve my-prompt --preview

# Apply improvement
promptvc improve my-prompt

# Improve with specific goals
promptvc improve my-prompt -g "make it shorter and more direct"
```

## Storage Location

Default: `./prompts/`

Change with: `promptvc --storage-path /custom/path <command>`

## File Structure
```
prompts/
├── index.json              # Quick index of all prompts
├── prompt-id-1.json        # Full prompt with all versions
├── prompt-id-2.json
└── ...
```

## Tips

1. **Use descriptive IDs**: Choose IDs that make prompts easy to find
2. **Tag effectively**: Use tags to categorize prompts
3. **Commit messages**: Write clear messages when updating prompts
4. **Projects**: Group related prompts in projects
5. **Version control**: Don't be afraid to experiment - you can always go back
6. **AI improvements**: Start with analysis before applying improvements
7. **Backup**: The prompts directory contains all your data - back it up!
