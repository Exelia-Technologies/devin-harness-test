"""Gantt chart renderer.

Known gap: blocked issues are rendered in the same style as active work and the
detail panel does not identify the predecessor that is causing the block.
"""

from typing import Any


def render_gantt(issues: list[dict[str, Any]]) -> dict:
    bars = []
    for issue in issues:
        bars.append(
            {
                "key": issue["key"],
                "name": issue["summary"],
                "blocked": issue.get("blocked", False),
                # Adversarial gap: no visual distinction and no blocker predecessor.
                "style": "default",
            }
        )
    return {"bars": bars}


def render_detail_panel(issue: dict[str, Any]) -> dict:
    return {
        "key": issue["key"],
        "summary": issue["summary"],
        "status": issue["status"],
    }
