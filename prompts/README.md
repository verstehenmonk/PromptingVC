# Prompts Directory

This directory contains prompts organized by project. Each project has its own subdirectory with prompts categorized by their purpose.

## Directory Structure

```
prompts/
├── README.md                    # This file
├── <project-name>/              # Directory for each project
│   ├── README.md                # Project-specific documentation
│   ├── system/                  # System prompts
│   ├── user/                    # User prompts
│   ├── templates/               # Reusable prompt templates
│   └── examples/                # Example prompts
└── shared/                      # Shared prompts across projects
    ├── common/                  # Common prompts
    └── templates/               # Shared templates
```

## How to Use

1. **Create a new project**: Create a new directory under `prompts/` with your project name
2. **Organize prompts**: Within your project directory, organize prompts by category (system, user, templates, examples)
3. **Add documentation**: Include a README.md in your project directory explaining the prompts
4. **Version control**: All prompts are version controlled through Git

## Naming Conventions

- Use lowercase with hyphens for directory names: `my-project`
- Use descriptive names for prompt files: `code-review-prompt.md`
- Use `.md` extension for prompt files to enable syntax highlighting

## Example Projects

See the `example-project/` directory for a sample project structure.
