# PromptingVC Tutorial

Welcome to PromptingVC! This tutorial will walk you through the basics of managing GPT prompts with version control.

## Prerequisites

1. Python 3.8 or higher installed
2. Git installed
3. (Optional) OpenAI API key for AI features

## Step 1: Installation

```bash
# Clone the repository
git clone https://github.com/verstehenmonk/PromptingVC.git
cd PromptingVC

# Install dependencies
pip install -r requirements.txt

# Install PromptingVC
pip install -e .

# Verify installation
promptvc --help
```

## Step 2: Create Your First Prompt

Let's create a simple prompt for a chatbot:

```bash
promptvc create chatbot-welcome customer-service "Welcome Chatbot" \
  -c "You are a friendly customer service chatbot. Greet the customer warmly and ask how you can help them today." \
  -d "Initial greeting for customer service chatbot" \
  -a "your-name" \
  -t chatbot -t customer-service
```

Output:
```
✓ Created prompt 'chatbot-welcome' in project 'customer-service'
  Version: 1
```

## Step 3: View Your Prompt

```bash
promptvc show chatbot-welcome
```

This displays:
- Prompt metadata (ID, project, name, description)
- Tags
- Version information
- The current prompt content

## Step 4: List All Prompts

```bash
# List all prompts
promptvc list

# List prompts in a specific project
promptvc list --project customer-service
```

## Step 5: Update Your Prompt

After testing, you realize the prompt needs improvement:

```bash
promptvc update chatbot-welcome \
  -c "You are an expert customer service chatbot with a friendly personality. Greet customers warmly, introduce yourself, and ask specifically how you can assist them with their needs today." \
  -m "Made greeting more specific and professional" \
  -a "your-name"
```

Output:
```
✓ Updated prompt 'chatbot-welcome'
  New Version: 2
```

## Step 6: View Version History

```bash
promptvc history chatbot-welcome
```

This shows all versions with:
- Version number
- Author
- Timestamp
- Commit message

## Step 7: Compare Versions

To see what a previous version looked like:

```bash
promptvc checkout chatbot-welcome 1
```

This displays the original version without changing the current version.

## Step 8: Create Prompts from Files

For longer prompts, it's easier to write them in a text file:

```bash
# Create a file
cat > expert-advisor.txt << 'EOF'
You are an expert technology advisor specializing in cloud infrastructure.

When a user asks a question:
1. Analyze their requirements carefully
2. Provide detailed, actionable recommendations
3. Explain trade-offs between different approaches
4. Include specific tools and technologies
5. Mention potential risks or challenges

Always be thorough but concise, and tailor your advice to the user's expertise level.
EOF

# Create prompt from file
promptvc create tech-advisor consulting "Technology Advisor" \
  -f expert-advisor.txt \
  -d "Expert advisor for cloud infrastructure questions" \
  -a "your-name" \
  -t consulting -t cloud
```

## Step 9: Organize by Projects

Create prompts for different projects:

```bash
# E-commerce project
promptvc create product-desc ecommerce "Product Description Generator" \
  -c "Generate compelling product descriptions..." \
  -t ecommerce

# Development tools project
promptvc create code-reviewer dev-tools "Code Reviewer" \
  -f examples/code-review-prompt.txt \
  -t code-review

# View projects
promptvc projects
```

Output:
```
Projects:
  - customer-service (1 prompts)
  - consulting (1 prompts)
  - ecommerce (1 prompts)
  - dev-tools (1 prompts)
```

## Step 10: AI-Powered Improvements (Optional)

If you have an OpenAI API key:

```bash
# Set your API key
export OPENAI_API_KEY='your-api-key-here'

# Analyze a prompt
promptvc analyze chatbot-welcome
```

This provides AI-generated suggestions for improving your prompt.

```bash
# Preview an AI improvement
promptvc improve chatbot-welcome --preview
```

This shows what the AI suggests without saving.

```bash
# Apply the improvement
promptvc improve chatbot-welcome

# Or improve with specific goals
promptvc improve chatbot-welcome -g "make it more concise and add examples"
```

The improved version is saved as a new version, preserving your history.

## Step 11: Working with Multiple Team Members

Share your prompts directory (or use git):

```bash
# Initialize git in prompts directory (optional)
cd prompts
git init
git add .
git commit -m "Initial prompts"

# Team members can clone and use
# Each update creates a new version with author info
```

## Step 12: Deleting Prompts

If you need to remove a prompt:

```bash
promptvc delete chatbot-welcome
```

You'll be asked to confirm the deletion.

## Best Practices

1. **Use Clear IDs**: Choose descriptive, dash-separated IDs
2. **Write Good Commit Messages**: Explain what changed and why
3. **Tag Appropriately**: Use tags to make prompts searchable
4. **Group by Project**: Organize related prompts together
5. **Version Iteratively**: Make small, incremental improvements
6. **Test Between Versions**: Validate changes before creating new versions
7. **Back Up Your Data**: The `prompts/` directory contains everything

## Common Use Cases

### Use Case 1: Testing Prompt Variations

```bash
# Create base prompt
promptvc create ab-test-a marketing "Marketing Copy A" -c "..."

# Create variation
promptvc create ab-test-b marketing "Marketing Copy B" -c "..."

# Test both, then improve the better one
promptvc update ab-test-a -c "improved version" -m "Based on test results"
```

### Use Case 2: Prompt Evolution

```bash
# Start simple
promptvc create my-prompt project "My Prompt" -c "Basic version"

# Iterate based on results
promptvc update my-prompt -c "Added examples" -m "Improved with examples"
promptvc update my-prompt -c "More specific" -m "Added constraints"

# Review evolution
promptvc history my-prompt
```

### Use Case 3: Team Collaboration

```bash
# Developer A creates prompt
promptvc create api-docs dev "API Documentation" -c "..." -a "alice"

# Developer B improves it
promptvc update api-docs -c "improved" -m "Added examples" -a "bob"

# Anyone can see the evolution
promptvc history api-docs
```

## Next Steps

- Explore the `examples/` directory for sample prompts
- Read `QUICKREF.md` for command reference
- Try the AI improvement features
- Create your own prompt templates
- Share your prompts with your team

## Getting Help

```bash
# General help
promptvc --help

# Command-specific help
promptvc create --help
promptvc update --help
```

## Troubleshooting

**Problem**: Command not found after installation
```bash
# Make sure you're in the right directory and installed correctly
pip install -e .
```

**Problem**: Can't use AI features
```bash
# Set your OpenAI API key
export OPENAI_API_KEY='your-key'

# Or create a .env file
echo "OPENAI_API_KEY=your-key" > .env
```

**Problem**: Lost previous versions
- Don't worry! All versions are preserved in the JSON files
- Use `promptvc history <id>` to see all versions
- Use `promptvc checkout <id> <version>` to view any version

Happy prompting! 🚀
