# PromptingVC
Manage version control for prompts for agentic use

## Overview

PromptingVC provides a structured approach to managing, versioning, and organizing prompts for AI agents across multiple projects. This repository helps teams collaborate on prompt engineering with proper version control and organization.

## Quick Start

1. Navigate to the `prompts/` directory
2. Create a new directory for your project: `prompts/your-project-name/`
3. Organize your prompts using the recommended structure:
   - `system/` - System-level prompts that define agent behavior
   - `user/` - User-facing prompts for specific tasks
   - `templates/` - Reusable prompt templates
   - `examples/` - Example prompts and use cases

## Directory Structure

```
prompts/
├── README.md                    # Documentation for the prompts directory
├── example-project/             # Example project showing best practices
│   ├── README.md
│   ├── system/                  # System prompts
│   ├── user/                    # User prompts
│   ├── templates/               # Reusable templates
│   └── examples/                # Example prompts
└── shared/                      # Shared prompts across projects
    ├── common/                  # Common prompts
    └── templates/               # Shared templates
```

## Features

- **Multi-Project Support**: Organize prompts for different projects in separate directories
- **Version Control**: Track changes to prompts over time with Git
- **Reusable Templates**: Create and share prompt templates across projects
- **Documentation**: Each project can include its own README and documentation
- **Examples**: Learn from example projects and prompts

## Getting Started

See the [prompts/README.md](prompts/README.md) for detailed documentation on the directory structure and usage.

Check out the [example-project](prompts/example-project/) to see a sample project setup.

## Contributing

1. Create a new directory for your project under `prompts/`
2. Follow the recommended directory structure
3. Document your prompts in a README.md
4. Commit and push your changes

## License

This project is open source and available for use in managing your AI prompts.
