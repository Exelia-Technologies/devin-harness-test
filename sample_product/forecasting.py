"""Forecasting service.

Known gap: forecasts are cached for the current day and only recalculated by a
scheduled nightly job. Saving a capacity change does not invalidate the cache.
"""

from datetime import date


class ForecastCache:
    def __init__(self) -> None:
        self._cache: dict[tuple[int, int], dict] = {}

    def get_forecast(self, project_id: int, day: date) -> dict:
        key = (project_id, day.toordinal())
        if key not in self._cache:
            self._cache[key] = self._compute_forecast(project_id, day)
        return self._cache[key]

    def update_capacity(self, project_id: int, new_capacity: float) -> None:
        # Adversarial gap: cache is not invalidated after a capacity change.
        pass

    def _compute_forecast(self, project_id: int, day: date) -> dict:
        return {"project_id": project_id, "day": day.isoformat(), "completion_date": None}


def add_forecast_confidence_field(forecast: dict) -> dict:
    """Placeholder that adds an undefined 'confidence' value."""
    forecast["confidence"] = 0.85
    return forecast
