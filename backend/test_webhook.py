#!/usr/bin/env python3
"""
Test script to debug webhook payload issues
"""
import asyncio
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from app.services.webhook_service import webhook_service
from app.services.authority_service import authority_service
from app.schemas.report import Location

async def test_webhook():
    """Test webhook with sample data"""

    # Sample report data (similar to what Supabase returns)
    sample_report = {
        "id": "test-report-123",
        "created_at": "2024-01-01T12:00:00Z",
        "location_lat": 40.7128,
        "location_lng": -74.0060,
        "location_address": "Main Street, City",
        "damage_type": "pothole",
        "severity": "high",
        "remarks": "Large pothole causing traffic issues",
        "image_url": "http://localhost:8000/uploads/test.jpg",
        "status": "submitted"
    }

    # Sample location for authority lookup
    sample_location = Location(
        lat=40.7128,
        lng=-74.0060,
        address="Main Street, City"
    )

    # Get authority
    authority = authority_service.identify_authority(sample_location)

    print("=== WEBHOOK TEST ===")
    print(f"Webhook URL configured: {webhook_service.is_configured()}")
    print(f"Webhook URL: {webhook_service.webhook_url}")
    print(f"Sample report data: {json.dumps(sample_report, indent=2)}")
    print(f"Authority data: {json.dumps(authority, indent=2)}")

    # Test webhook
    print("\n=== SENDING WEBHOOK ===")
    success = await webhook_service.send_notification(sample_report, authority)

    print(f"\nWebhook test result: {'SUCCESS' if success else 'FAILED'}")

if __name__ == "__main__":
    asyncio.run(test_webhook())


