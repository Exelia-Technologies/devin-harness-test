-- Migration stub: add forecast_confidence column to forecasts table.
-- This file exists only to exercise protected-path detection in harness tests.

ALTER TABLE forecasts ADD COLUMN forecast_confidence NUMERIC;
