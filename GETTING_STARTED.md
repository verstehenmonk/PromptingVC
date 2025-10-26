# Getting Started with PromptingVC

This guide will help you get started with using PromptingVC to manage your AI prompts.

## Creating Your First Project

1. **Navigate to the prompts directory**:
   ```bash
   cd prompts/
   ```

2. **Create a new project directory**:
   ```bash
   mkdir my-project
   cd my-project
   ```

3. **Create the recommended subdirectories**:
   ```bash
   mkdir system user templates examples
   ```

4. **Add a README for your project**:
   Create a `README.md` file describing your project and its prompts.

5. **Start adding prompts**:
   - Place system prompts in `system/`
   - Place user-facing prompts in `user/`
   - Place reusable templates in `templates/`
   - Place example usage in `examples/`

## Best Practices

### Naming Conventions
- **Directories**: Use lowercase with hyphens (e.g., `code-review-agent`)
- **Files**: Use descriptive names with `.md` extension (e.g., `system-prompt.md`)

### File Organization
- Keep related prompts together in the same category
- Use subdirectories within categories for large projects
- Document the purpose of each prompt in its file

### Version Control
- Commit prompts with descriptive messages
- Tag major versions of prompt sets
- Use branches for experimental prompts

### Documentation
- Always include a README.md in your project directory
- Document expected inputs and outputs
- Include examples of how to use the prompts

## Example Workflow

1. **Create a new project for a chatbot**:
   ```bash
   mkdir prompts/customer-service-bot
   cd prompts/customer-service-bot
   mkdir system user templates examples
   ```

2. **Add a system prompt**:
   Create `system/bot-personality.md` with the agent's role and behavior.

3. **Add user prompts**:
   Create prompts in `user/` for different customer scenarios.

4. **Create templates**:
   Add reusable templates in `templates/` for common interactions.

5. **Document examples**:
   Add example conversations in `examples/` to show best practices.

6. **Commit your work**:
   ```bash
   git add .
   git commit -m "Add customer service bot prompts"
   git push
   ```

## Using Shared Resources

The `prompts/shared/` directory contains prompts and templates that can be used across multiple projects:

- **Common prompts**: Found in `shared/common/`
- **Shared templates**: Found in `shared/templates/`

You can reference these in your project documentation or copy and customize them.

## Need Help?

Check out the `prompts/example-project/` directory for a complete example of a well-organized project.
