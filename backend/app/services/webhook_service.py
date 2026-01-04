"""
Service for sending webhook notifications to relay.app
"""
import os
import httpx
from typing import Dict, Any
import json

class WebhookService:
    """Service for sending webhook notifications"""
    
    def __init__(self):
        self._webhook_url = None
    
    @property
    def webhook_url(self) -> str:
        """Get webhook URL with lazy initialization"""
        if self._webhook_url is None:
            self._webhook_url = os.getenv("RELAY_APP_WEBHOOK_URL")
        return self._webhook_url
    
    def is_configured(self) -> bool:
        """Check if webhook URL is configured"""
        return bool(self.webhook_url)
    
    async def send_notification(self, report_data: Dict[str, Any], authority: Dict[str, str]) -> bool:
        """
        Send a structured JSON payload to relay.app webhook

        Args:
            report_data: Complete report data from database
            authority: Authority information

        Returns:
            True if successful, False otherwise
        """
        # Check if webhook is configured
        if not self.is_configured():
            print("Warning: RELAY_APP_WEBHOOK_URL not configured. Skipping webhook notification.")
            return False

        # Structure the payload with flat variables that match relay.app email template
        # The email template uses {{variable_name}} so we need top-level string fields
        payload = {
            # Email subject (short and marked as important)
            "subject": f"🚨 IMPORTANT: Road Damage Report {report_data.get('id', 'unknown')[:8]}",
            "report_id": report_data.get("id"),
            "location": report_data.get("location_address", f"{report_data.get('location_lat', 0)}, {report_data.get('location_lng', 0)}"),
            "damage_type": report_data.get("damage_type", "unknown"),
            "severity": report_data.get("severity", "unknown"),
            "image_url": report_data.get("image_url", ""),
            "remarks": report_data.get("remarks", ""),

            # Authority information for email signature (multiple variable names for compatibility)
            "authority_name": authority.get("name", "Road Maintenance Authority"),
            "authority_contact": authority.get("contact", "maintenance@city.gov"),
            "authority_department": authority.get("department", "Infrastructure Maintenance"),

            # Alternative variable names that might match your email template
            "name": authority.get("name", "Road Maintenance Authority"),
            "contact": authority.get("contact", "maintenance@city.gov"),
            "designation": authority.get("department", "Infrastructure Maintenance"),
            "contact_details": authority.get("contact", "maintenance@city.gov"),
            "email": authority.get("contact", "maintenance@city.gov"),

            # Additional nested structure for future use
            "event_type": "road_damage_report",
            "timestamp": report_data.get("created_at"),
            "location_details": {
                "latitude": report_data.get("location_lat"),
                "longitude": report_data.get("location_lng"),
                "address": report_data.get("location_address")
            },
            "damage_details": {
                "type": report_data.get("damage_type"),
                "severity": report_data.get("severity"),
                "description": report_data.get("remarks"),
                "image_url": report_data.get("image_url")
            },
            "responsible_authority": {
                "name": authority.get("name"),
                "department": authority.get("department"),
                "contact": authority.get("contact")
            },
            "status": report_data.get("status"),
            "priority": self._calculate_priority(report_data.get("severity"))
        }
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    self.webhook_url,
                    json=payload,
                    headers={"Content-Type": "application/json"}
                )
                response.raise_for_status()
                return True
        except Exception as e:
            print(f"Webhook notification failed: {e}")
            return False
    
    def _calculate_priority(self, severity: str) -> str:
        """Calculate priority based on severity"""
        priority_map = {
            "low": "normal",
            "medium": "high",
            "high": "urgent"
        }
        return priority_map.get(severity, "normal")

# Singleton instance
webhook_service = WebhookService()

