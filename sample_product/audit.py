"""Webhook audit log and retention policy.

Known gap: the configuration simultaneously requires immediate deletion of audit
payloads after processing and retention for 90-day compliance investigations.
This contradiction must be resolved by product/security before implementation.
"""

from datetime import datetime


RETENTION_CONFIG = {
    "delete_immediately_after_processing": True,
    "retain_for_compliance_days": 90,
}


def process_audit_payload(payload: dict) -> dict:
    # Placeholder processing; actual retention behavior is undefined.
    return {
        "processed_at": datetime.utcnow().isoformat(),
        "payload_id": payload.get("id"),
    }
