"""Minimal domain models for the sample product used in harness adversarial tests."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    role: str  # "superuser", "admin", "viewer"
    active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Project:
    id: int
    key: str
    name: str
    harness_enabled: bool = False
    enable_assessment_ready_emails: bool = True


@dataclass
class Issue:
    id: int
    key: str
    summary: str
    status: str
    project_id: int
    issue_type: str = "Task"
    story_points: Optional[float] = None
    rejected: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
