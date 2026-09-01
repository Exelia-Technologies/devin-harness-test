"""Project settings endpoints.

Known gap: the harness-delegation toggle is visible and mutable by any project
member; role checks are missing on the update endpoint.
"""

from sample_product.auth import decode_token, is_admin
from sample_product.models import Project


def get_settings(project_id: int, token: str) -> dict:
    decode_token(token)  # validates signature only
    project = _load_project(project_id)
    return {
        "harness_enabled": project.harness_enabled,
        "enable_assessment_ready_emails": project.enable_assessment_ready_emails,
    }


def update_harness_toggle(project_id: int, enabled: bool, token: str) -> dict:
    # Adversarial gap: no admin authorization check before mutating this setting.
    project = _load_project(project_id)
    project.harness_enabled = enabled
    return {"harness_enabled": project.harness_enabled}


def _load_project(project_id: int) -> Project:
    # Placeholder loader for adversarial harness tests.
    return Project(id=project_id, key="PROJ", name="Project", harness_enabled=False)
