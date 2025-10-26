# PromptingVC

A version control system for managing GPT prompts across multiple projects. Write, update, version, and use AI to improve your prompts - all in one place.

## Features

- 📝 **Create and manage prompts** - Organize prompts by project with descriptions and tags
- 🔄 **Version control** - Track changes with full version history and commit messages
- 🤖 **AI-powered improvements** - Use GPT-4 to analyze and improve your prompts
- 📁 **Multi-project support** - Manage prompts for multiple projects in a single repository
- 💾 **JSON storage** - Simple, human-readable file-based storage
- 🖥️ **CLI interface** - Easy-to-use command-line tools

## Installation

```bash
# Clone the repository
git clone https://github.com/verstehenmonk/PromptingVC.git
cd PromptingVC

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Quick Start

### Create a prompt

```bash
# Create a prompt with inline content
promptvc create my-prompt my-project "Code Review Prompt" \
  --description "Prompt for code review assistance" \
  --content "Review the following code and provide feedback on..." \
  --author "your-name" \
  --tags code-review --tags development

# Or create from a file
promptvc create my-prompt my-project "Code Review Prompt" \
  --file prompt.txt \
  --author "your-name"
```

### List prompts

```bash
# List all prompts
promptvc list

# List prompts for a specific project
promptvc list --project my-project
```

### View a prompt

```bash
promptvc show my-prompt
```

### Update a prompt

```bash
# Update with new content
promptvc update my-prompt \
  --content "Updated prompt content..." \
  --message "Improved clarity and structure" \
  --author "your-name"

# Update from file
promptvc update my-prompt \
  --file updated-prompt.txt \
  --message "Added examples"
```

### View version history

```bash
# See all versions
promptvc history my-prompt

# View a specific version
promptvc checkout my-prompt 1
```

### AI-powered improvements

First, set your OpenAI API key:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Then use AI features:

```bash
# Analyze a prompt and get suggestions
promptvc analyze my-prompt

# Improve a prompt automatically
promptvc improve my-prompt

# Improve with specific goals
promptvc improve my-prompt --goals "Make it more concise and add examples"

# Preview improvement without saving
promptvc improve my-prompt --preview
```

### Manage projects

```bash
# List all projects
promptvc projects
```

### Delete a prompt

```bash
promptvc delete my-prompt
```

## Project Structure

```
PromptingVC/
├── promptingvc/          # Main package
│   ├── __init__.py       # Package initialization
│   ├── models.py         # Data models (Prompt, PromptVersion)
│   ├── storage.py        # Storage management
│   ├── improver.py       # AI-powered improvements
│   └── cli.py            # Command-line interface
├── prompts/              # Default storage directory (created on first use)
│   ├── index.json        # Index of all prompts
│   └── *.json            # Individual prompt files
├── requirements.txt      # Python dependencies
├── setup.py              # Package setup
└── README.md             # This file
```

## Storage Format

Prompts are stored as JSON files in the `prompts/` directory. Each prompt contains:

- Metadata (ID, project, name, description, tags)
- Version history with full content for each version
- Timestamps and author information

Example prompt file structure:

```json
{
  "id": "my-prompt",
  "project": "my-project",
  "name": "Code Review Prompt",
  "description": "Prompt for code review assistance",
  "current_version": 2,
  "versions": [
    {
      "version": 1,
      "content": "Review the following code...",
      "created_at": "2025-01-01T12:00:00",
      "author": "user",
      "message": "Initial version"
    },
    {
      "version": 2,
      "content": "Improved prompt content...",
      "created_at": "2025-01-02T14:30:00",
      "author": "user",
      "message": "Added examples"
    }
  ],
  "tags": ["code-review", "development"],
  "created_at": "2025-01-01T12:00:00",
  "updated_at": "2025-01-02T14:30:00"
}
```

## Configuration

### Storage Location

By default, prompts are stored in the `prompts/` directory. You can change this:

```bash
promptvc --storage-path /path/to/prompts list
```

### OpenAI API Key

For AI-powered features, set your API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or create a `.env` file in the project root:

```
OPENAI_API_KEY=your-api-key-here
```

## Use Cases

### Multi-Project Prompt Management

Organize prompts for different projects:

```bash
# Create prompts for different projects
promptvc create review-prompt web-app "Code Review" --content "..."
promptvc create test-prompt mobile-app "Test Generation" --content "..."
promptvc create doc-prompt api-service "Documentation" --content "..."

# List prompts by project
promptvc list --project web-app
promptvc list --project mobile-app
```

### Prompt Evolution with Version Control

Track how your prompts improve over time:

```bash
# Create initial version
promptvc create my-prompt project "My Prompt" --content "Initial version"

# Update as you refine
promptvc update my-prompt --content "Version 2" --message "Added clarity"
promptvc update my-prompt --content "Version 3" --message "Added examples"

# Review history
promptvc history my-prompt

# Go back to a previous version if needed
promptvc checkout my-prompt 2
```

### AI-Assisted Prompt Engineering

Use AI to refine and improve prompts:

```bash
# Get analysis
promptvc analyze my-prompt

# Apply improvements
promptvc improve my-prompt --goals "Make it more specific and actionable"

# Preview before committing
promptvc improve my-prompt --preview
```

## CLI Commands Reference

| Command | Description |
|---------|-------------|
| `create` | Create a new prompt |
| `show` | Display a prompt and its current content |
| `list` | List all prompts (optionally filtered by project) |
| `projects` | List all projects |
| `update` | Update a prompt with a new version |
| `history` | Show version history of a prompt |
| `checkout` | View a specific version |
| `improve` | Use AI to improve a prompt |
| `analyze` | Get AI analysis and suggestions |
| `delete` | Delete a prompt |

## Development

### Running Tests

```bash
# Install development dependencies
pip install pytest

# Run tests (when available)
pytest
```

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - feel free to use this project for your prompt management needs.

## Roadmap

Future enhancements planned:

- [ ] Web UI for managing prompts
- [ ] Import/export functionality
- [ ] Prompt templates
- [ ] Collaboration features
- [ ] Integration with popular AI platforms
- [ ] Automated testing of prompts
- [ ] Analytics and usage tracking
