# PromptingVC Examples

This directory contains example prompts that demonstrate common use cases.

## Available Examples

### code-review-prompt.txt
A prompt for conducting thorough code reviews with GPT assistance.

**Usage:**
```bash
promptvc create code-review dev-tools "Code Review Assistant" \
  --file examples/code-review-prompt.txt \
  --description "Comprehensive code review prompt" \
  --tags code-review --tags quality-assurance
```

### test-generation-prompt.txt
A prompt for generating unit tests from code.

**Usage:**
```bash
promptvc create test-gen dev-tools "Test Generator" \
  --file examples/test-generation-prompt.txt \
  --description "Generate unit tests from code" \
  --tags testing --tags automation
```

## Creating Your Own Examples

1. Write your prompt in a text file
2. Use placeholders like `{CODE_HERE}` for dynamic content
3. Create the prompt with PromptingVC:
   ```bash
   promptvc create my-example my-project "My Prompt" --file your-prompt.txt
   ```

## Tips for Writing Good Prompts

- Be specific about what you want
- Provide clear structure and formatting requirements
- Include examples when helpful
- Use placeholders for dynamic content
- Iterate and improve based on results
