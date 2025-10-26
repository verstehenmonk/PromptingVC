"""Storage management for prompts."""

import json
from pathlib import Path
from typing import List, Optional, Dict
from .models import Prompt, PromptVersion
from datetime import datetime


class PromptStorage:
    """Manages storage and retrieval of prompts."""

    def __init__(self, storage_path: str = "prompts"):
        """Initialize storage with a base path."""
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.index_file = self.storage_path / "index.json"
        self._ensure_index()

    def _ensure_index(self):
        """Ensure the index file exists."""
        if not self.index_file.exists():
            self._save_index({})

    def _load_index(self) -> Dict:
        """Load the index of all prompts."""
        with open(self.index_file, 'r') as f:
            return json.load(f)

    def _save_index(self, index: Dict):
        """Save the index."""
        with open(self.index_file, 'w') as f:
            json.dump(index, f, indent=2)

    def _get_prompt_file(self, prompt_id: str) -> Path:
        """Get the file path for a prompt."""
        return self.storage_path / f"{prompt_id}.json"

    def save_prompt(self, prompt: Prompt):
        """Save a prompt to storage."""
        # Save the prompt file
        prompt_file = self._get_prompt_file(prompt.id)
        with open(prompt_file, 'w') as f:
            json.dump(prompt.to_dict(), f, indent=2)

        # Update index
        index = self._load_index()
        index[prompt.id] = {
            'project': prompt.project,
            'name': prompt.name,
            'description': prompt.description,
            'tags': prompt.tags,
            'updated_at': prompt.updated_at
        }
        self._save_index(index)

    def load_prompt(self, prompt_id: str) -> Optional[Prompt]:
        """Load a prompt from storage."""
        prompt_file = self._get_prompt_file(prompt_id)
        if not prompt_file.exists():
            return None

        with open(prompt_file, 'r') as f:
            data = json.load(f)
            return Prompt.from_dict(data)

    def list_prompts(self, project: Optional[str] = None) -> List[Dict]:
        """List all prompts, optionally filtered by project."""
        index = self._load_index()
        prompts = []
        for prompt_id, info in index.items():
            if project is None or info['project'] == project:
                prompts.append({
                    'id': prompt_id,
                    **info
                })
        return prompts

    def delete_prompt(self, prompt_id: str) -> bool:
        """Delete a prompt."""
        prompt_file = self._get_prompt_file(prompt_id)
        if not prompt_file.exists():
            return False

        prompt_file.unlink()

        # Update index
        index = self._load_index()
        if prompt_id in index:
            del index[prompt_id]
            self._save_index(index)

        return True

    def list_projects(self) -> List[str]:
        """List all unique projects."""
        index = self._load_index()
        projects = set()
        for info in index.values():
            projects.add(info['project'])
        return sorted(list(projects))

    def create_prompt(self, prompt_id: str, project: str, name: str, 
                     description: str, initial_content: str, author: str,
                     tags: Optional[List[str]] = None) -> Prompt:
        """Create a new prompt."""
        now = datetime.now().isoformat()
        initial_version = PromptVersion(
            version=1,
            content=initial_content,
            created_at=now,
            author=author,
            message="Initial version"
        )

        prompt = Prompt(
            id=prompt_id,
            project=project,
            name=name,
            description=description,
            current_version=1,
            versions=[initial_version],
            tags=tags or [],
            created_at=now,
            updated_at=now
        )

        self.save_prompt(prompt)
        return prompt
