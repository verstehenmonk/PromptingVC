"""Command-line interface for PromptingVC."""

import click
import sys
from pathlib import Path
from typing import Optional
from .storage import PromptStorage
from .improver import PromptImprover


@click.group()
@click.option('--storage-path', default='prompts', help='Path to prompts storage directory')
@click.pass_context
def cli(ctx, storage_path):
    """PromptingVC - Version control for GPT prompts."""
    ctx.ensure_object(dict)
    ctx.obj['storage'] = PromptStorage(storage_path)
    ctx.obj['improver'] = PromptImprover()


@cli.command()
@click.argument('prompt_id')
@click.argument('project')
@click.argument('name')
@click.option('--description', '-d', default='', help='Prompt description')
@click.option('--content', '-c', help='Initial prompt content')
@click.option('--file', '-f', type=click.Path(exists=True), help='Read content from file')
@click.option('--author', '-a', default='user', help='Author name')
@click.option('--tags', '-t', multiple=True, help='Tags for the prompt')
@click.pass_context
def create(ctx, prompt_id, project, name, description, content, file, author, tags):
    """Create a new prompt."""
    storage = ctx.obj['storage']
    
    # Get content from file or argument
    if file:
        with open(file, 'r') as f:
            content = f.read()
    elif not content:
        click.echo("Error: Must provide either --content or --file")
        sys.exit(1)
    
    # Check if prompt already exists
    existing = storage.load_prompt(prompt_id)
    if existing:
        click.echo(f"Error: Prompt '{prompt_id}' already exists")
        sys.exit(1)
    
    prompt = storage.create_prompt(
        prompt_id=prompt_id,
        project=project,
        name=name,
        description=description,
        initial_content=content,
        author=author,
        tags=list(tags)
    )
    
    click.echo(f"✓ Created prompt '{prompt_id}' in project '{project}'")
    click.echo(f"  Version: {prompt.current_version}")


@cli.command()
@click.argument('prompt_id')
@click.pass_context
def show(ctx, prompt_id):
    """Show a prompt and its current content."""
    storage = ctx.obj['storage']
    prompt = storage.load_prompt(prompt_id)
    
    if not prompt:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)
    
    click.echo(f"ID: {prompt.id}")
    click.echo(f"Project: {prompt.project}")
    click.echo(f"Name: {prompt.name}")
    click.echo(f"Description: {prompt.description}")
    click.echo(f"Tags: {', '.join(prompt.tags) if prompt.tags else 'None'}")
    click.echo(f"Current Version: {prompt.current_version}")
    click.echo(f"Created: {prompt.created_at}")
    click.echo(f"Updated: {prompt.updated_at}")
    click.echo("\n--- Current Content ---")
    click.echo(prompt.get_current_content())


@cli.command('list')
@click.option('--project', '-p', help='Filter by project')
@click.pass_context
def list_prompts_cmd(ctx, project):
    """List all prompts."""
    storage = ctx.obj['storage']
    prompts = storage.list_prompts(project=project)
    
    if not prompts:
        if project:
            click.echo(f"No prompts found in project '{project}'")
        else:
            click.echo("No prompts found")
        return
    
    click.echo(f"{'ID':<20} {'Project':<15} {'Name':<30} {'Tags':<20}")
    click.echo("-" * 90)
    for p in prompts:
        tags_str = ', '.join(p['tags'][:3]) if p['tags'] else ''
        click.echo(f"{p['id']:<20} {p['project']:<15} {p['name']:<30} {tags_str:<20}")


@cli.command()
@click.pass_context
def projects(ctx):
    """List all projects."""
    storage = ctx.obj['storage']
    projects = storage.list_projects()
    
    if not projects:
        click.echo("No projects found")
        return
    
    click.echo("Projects:")
    for project in projects:
        prompt_count = len(storage.list_prompts(project=project))
        click.echo(f"  - {project} ({prompt_count} prompts)")


@cli.command()
@click.argument('prompt_id')
@click.option('--content', '-c', help='New prompt content')
@click.option('--file', '-f', type=click.Path(exists=True), help='Read content from file')
@click.option('--message', '-m', required=True, help='Commit message for this version')
@click.option('--author', '-a', default='user', help='Author name')
@click.pass_context
def update(ctx, prompt_id, content, file, message, author):
    """Update a prompt with a new version."""
    storage = ctx.obj['storage']
    prompt = storage.load_prompt(prompt_id)
    
    if not prompt:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)
    
    # Get content from file or argument
    if file:
        with open(file, 'r') as f:
            content = f.read()
    elif not content:
        click.echo("Error: Must provide either --content or --file")
        sys.exit(1)
    
    prompt.add_version(content, author, message)
    storage.save_prompt(prompt)
    
    click.echo(f"✓ Updated prompt '{prompt_id}'")
    click.echo(f"  New Version: {prompt.current_version}")


@cli.command()
@click.argument('prompt_id')
@click.pass_context
def history(ctx, prompt_id):
    """Show version history of a prompt."""
    storage = ctx.obj['storage']
    prompt = storage.load_prompt(prompt_id)
    
    if not prompt:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)
    
    click.echo(f"Version history for '{prompt_id}':")
    click.echo()
    for version in reversed(prompt.versions):
        current = " (current)" if version.version == prompt.current_version else ""
        click.echo(f"Version {version.version}{current}")
        click.echo(f"  Author: {version.author}")
        click.echo(f"  Date: {version.created_at}")
        click.echo(f"  Message: {version.message}")
        click.echo()


@cli.command()
@click.argument('prompt_id')
@click.argument('version', type=int)
@click.pass_context
def checkout(ctx, prompt_id, version):
    """View a specific version of a prompt."""
    storage = ctx.obj['storage']
    prompt = storage.load_prompt(prompt_id)
    
    if not prompt:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)
    
    version_obj = prompt.get_version(version)
    if not version_obj:
        click.echo(f"Error: Version {version} not found")
        sys.exit(1)
    
    click.echo(f"Prompt: {prompt.name} (Version {version})")
    click.echo(f"Author: {version_obj.author}")
    click.echo(f"Date: {version_obj.created_at}")
    click.echo(f"Message: {version_obj.message}")
    click.echo("\n--- Content ---")
    click.echo(version_obj.content)


@cli.command()
@click.argument('prompt_id')
@click.option('--goals', '-g', help='Specific improvement goals')
@click.option('--author', '-a', default='ai-improver', help='Author name for the new version')
@click.option('--preview', is_flag=True, help='Preview improvement without saving')
@click.pass_context
def improve(ctx, prompt_id, goals, author, preview):
    """Use AI to improve a prompt."""
    storage = ctx.obj['storage']
    improver = ctx.obj['improver']
    
    if not improver.is_available():
        click.echo("Error: AI improvement requires OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    prompt = storage.load_prompt(prompt_id)
    if not prompt:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)
    
    current_content = prompt.get_current_content()
    
    click.echo("Improving prompt with AI...")
    try:
        improved_content = improver.improve_prompt(current_content, goals)
        
        click.echo("\n--- Improved Version ---")
        click.echo(improved_content)
        
        if preview:
            click.echo("\n(Preview mode - not saved)")
        else:
            message = f"AI improvement{': ' + goals if goals else ''}"
            prompt.add_version(improved_content, author, message, metadata={'ai_improved': True})
            storage.save_prompt(prompt)
            click.echo(f"\n✓ Saved as version {prompt.current_version}")
            
    except Exception as e:
        click.echo(f"Error: {str(e)}")
        sys.exit(1)


@cli.command()
@click.argument('prompt_id')
@click.pass_context
def analyze(ctx, prompt_id):
    """Analyze a prompt and get AI suggestions."""
    storage = ctx.obj['storage']
    improver = ctx.obj['improver']
    
    if not improver.is_available():
        click.echo("Error: AI analysis requires OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    prompt = storage.load_prompt(prompt_id)
    if not prompt:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)
    
    current_content = prompt.get_current_content()
    
    click.echo("Analyzing prompt with AI...")
    try:
        analysis = improver.analyze_prompt(current_content)
        click.echo("\n--- Analysis ---")
        click.echo(analysis)
    except Exception as e:
        click.echo(f"Error: {str(e)}")
        sys.exit(1)


@cli.command()
@click.argument('prompt_id')
@click.confirmation_option(prompt='Are you sure you want to delete this prompt?')
@click.pass_context
def delete(ctx, prompt_id):
    """Delete a prompt."""
    storage = ctx.obj['storage']
    
    if storage.delete_prompt(prompt_id):
        click.echo(f"✓ Deleted prompt '{prompt_id}'")
    else:
        click.echo(f"Error: Prompt '{prompt_id}' not found")
        sys.exit(1)


if __name__ == '__main__':
    cli(obj={})
