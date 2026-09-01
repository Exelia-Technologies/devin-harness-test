"""Webhook processor for partial Jira epic updates.

Known gap: a partial payload that omits the objective_year field overwrites it
with None, because the update path does not distinguish omitted from explicitly
null values.
"""

from sample_product.models import Project


class EpicStore:
    def __init__(self) -> None:
        self.epics: dict[str, dict] = {}

    def apply_partial_update(self, project: Project, epic_key: str, payload: dict) -> dict:
        existing = self.epics.get(epic_key, {"project_id": project.id, "objective_year": None})
        # Adversarial gap: no distinction between omitted and explicit null.
        existing["quarter_target"] = payload.get("quarter_target")
        existing["objective_year"] = payload.get("objective_year")
        self.epics[epic_key] = existing
        return existing
