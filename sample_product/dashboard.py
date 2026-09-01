"""Project dashboard.

Known gap: the dashboard renders several heavy widgets and loads slowly, but no
measurement, caching, or bottleneck data is provided. The performance target is
stated without context.
"""

from typing import Any


def load_dashboard(project_id: int) -> dict[str, Any]:
    # Adversarial gap: heavy sequential queries with no instrumentation.
    widgets = [
        _load_issues_widget(project_id),
        _load_metrics_widget(project_id),
        _load_forecast_widget(project_id),
        _load_activity_feed(project_id),
    ]
    return {"project_id": project_id, "widgets": widgets}


def _load_issues_widget(project_id: int) -> dict:
    return {"type": "issues", "project_id": project_id}


def _load_metrics_widget(project_id: int) -> dict:
    return {"type": "metrics", "project_id": project_id}


def _load_forecast_widget(project_id: int) -> dict:
    return {"type": "forecast", "project_id": project_id}


def _load_activity_feed(project_id: int) -> dict:
    return {"type": "activity", "project_id": project_id}
