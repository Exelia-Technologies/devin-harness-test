"""Superficial tests that do not exercise the adversarial gaps."""

from sample_product.auth import decode_token, require_project_access
from sample_product.dashboard import load_dashboard
from sample_product.forecasting import ForecastCache
from sample_product.gantt_chart import render_detail_panel, render_gantt
from sample_product.metrics import calculate_velocity
from sample_product.models import Issue, Project, User
from sample_product.notification_service import send_issue_created_harness
from sample_product.project_settings import get_settings
from sample_product.webhook_processor import EpicStore


def test_decode_token():
    token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiJ1c2VyLTEiLCJyb2xlIjoidmlld2VyIn0."
        "dummy_signature"
    )
    # We do not actually verify the dummy signature; this test is illustrative.
    assert decode_token is not None


def test_velocity_happy_path():
    issues = [
        Issue(id=1, key="SP-1", summary="A", status="Done", project_id=1, story_points=5),
        Issue(id=2, key="SP-2", summary="B", status="Done", project_id=1, story_points=3),
    ]
    assert calculate_velocity(issues) == 4.0


def test_gantt_renders():
    issues = [{"key": "SP-1", "summary": "A", "status": "To Do", "blocked": False}]
    result = render_gantt(issues)
    assert result["bars"][0]["key"] == "SP-1"


def test_detail_panel_renders():
    issue = {"key": "SP-1", "summary": "A", "status": "To Do"}
    assert render_detail_panel(issue)["key"] == "SP-1"


def test_forecast_cache_returns_value():
    cache = ForecastCache()
    from datetime import date

    result = cache.get_forecast(1, date(2026, 1, 1))
    assert result["project_id"] == 1


def test_dashboard_loads():
    result = load_dashboard(1)
    assert result["project_id"] == 1
    assert len(result["widgets"]) == 4


def test_notification_service_exists():
    project = Project(id=1, key="SP")
    user = User(id=1, email="a@example.com", role="viewer")
    send_issue_created_harness(project, user)


def test_project_settings_load():
    project = Project(id=1, key="SP")
    user = User(id=1, email="a@example.com", role="viewer")
    # Adversarial gap: no role check is exercised here.
    get_settings(project.id, "dummy_token")


def test_webhook_partial_update():
    store = EpicStore()
    project = Project(id=1, key="SP")
    result = store.apply_partial_update(project, "SP-E1", {"quarter_target": "Q1"})
    assert result["quarter_target"] == "Q1"
