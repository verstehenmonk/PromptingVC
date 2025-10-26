"""Core data models for prompt management."""

import json
from datetime import datetime
from typing import Optional, Dict, List
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class PromptVersion:
    """Represents a single version of a prompt."""
    version: int
    content: str
    created_at: str
    author: str
    message: str
    metadata: Optional[Dict] = None

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return asdict(self)


@dataclass
class Prompt:
    """Represents a prompt with version history."""
    id: str
    project: str
    name: str
    description: str
    current_version: int
    versions: List[PromptVersion]
    tags: List[str]
    created_at: str
    updated_at: str

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        data = asdict(self)
        data['versions'] = [v.to_dict() if hasattr(v, 'to_dict') else v for v in self.versions]
        return data

    @classmethod
    def from_dict(cls, data: Dict) -> 'Prompt':
        """Create from dictionary."""
        versions = [
            PromptVersion(**v) if isinstance(v, dict) else v
            for v in data.get('versions', [])
        ]
        data_copy = data.copy()
        data_copy['versions'] = versions
        return cls(**data_copy)

    def get_current_content(self) -> str:
        """Get the content of the current version."""
        for version in self.versions:
            if version.version == self.current_version:
                return version.content
        return ""

    def get_version(self, version_num: int) -> Optional[PromptVersion]:
        """Get a specific version."""
        for version in self.versions:
            if version.version == version_num:
                return version
        return None

    def add_version(self, content: str, author: str, message: str, metadata: Optional[Dict] = None):
        """Add a new version of the prompt."""
        new_version_num = self.current_version + 1
        new_version = PromptVersion(
            version=new_version_num,
            content=content,
            created_at=datetime.now().isoformat(),
            author=author,
            message=message,
            metadata=metadata
        )
        self.versions.append(new_version)
        self.current_version = new_version_num
        self.updated_at = datetime.now().isoformat()
