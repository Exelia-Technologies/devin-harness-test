"""Metrics service.

Known gap: velocity and throughput calculations include rejected issues because
no status filter is applied to the denominator.
"""

from sample_product.models import Issue


def calculate_velocity(issues: list[Issue]) -> float:
    """Story points completed per week. Rejected issues are incorrectly counted."""
    completed = [i for i in issues if i.status in ("Done", "Closed", "Rejected")]
    if not completed:
        return 0.0
    total_points = sum(i.story_points or 0 for i in completed)
    return total_points / max(len(completed), 1)


def calculate_throughput(issues: list[Issue]) -> int:
    """Number of issues completed per week. Rejected issues are incorrectly counted."""
    return len([i for i in issues if i.status in ("Done", "Closed", "Rejected")])
