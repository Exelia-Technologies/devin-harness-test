"""Notification dispatch.

Known gap: two code paths (legacy email alert service and the new harness
notification handler) can both emit an issue-created email for the same recipient.
"""

from sample_product.models import Project, User


def send_issue_created_legacy(project: Project, user: User) -> None:
    # Legacy path that still runs on harness-enabled projects.
    _send_email(user.email, f"Issue created on {project.key}")


def send_issue_created_harness(project: Project, user: User) -> None:
    # New path added during harness integration.
    _send_email(user.email, f"Issue created on {project.key}")


def _send_email(recipient: str, subject: str) -> None:
    # Stub: in production this calls the email provider.
    pass
