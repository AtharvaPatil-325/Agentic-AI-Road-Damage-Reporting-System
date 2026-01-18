"""
Supabase service for database operations
"""
import os
from supabase import create_client, Client
from typing import Optional, Dict, Any
from app.schemas.report import ReportCreate, ReportStatus

class SupabaseService:
    """Service for interacting with Supabase database"""
    
    def __init__(self):
        self._client: Optional[Client] = None
    
    @property
    def client(self) -> Client:
        """Lazy initialization of Supabase client"""
        if self._client is None:
            supabase_url = os.getenv("SUPABASE_URL")
            supabase_key = os.getenv("SUPABASE_KEY")
            
            if not supabase_url or not supabase_key:
                raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")
            
            self._client = create_client(supabase_url, supabase_key)
        return self._client
    
    async def create_report(self, report_data: ReportCreate, image_url: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new report in the database
        
        Args:
            report_data: Report creation data
            image_url: Optional URL to uploaded image
            
        Returns:
            Dictionary containing the created report data
        """
        report_dict = {
            "location_lat": report_data.location.lat,
            "location_lng": report_data.location.lng,
            "location_address": report_data.location.address,
            "damage_type": report_data.damage_type.value,
            "severity": report_data.severity.value,
            "remarks": report_data.remarks,
            "image_url": image_url,
            "status": ReportStatus.SUBMITTED.value,
        }
        
        result = self.client.table("reports").insert(report_dict).execute()

        if result.data:
            # Get the created record with all fields including timestamps
            report_id = result.data[0]["id"]
            full_result = self.client.table("reports").select("*").eq("id", report_id).execute()

            if full_result.data:
                return full_result.data[0]

        raise Exception("Failed to create report in database")
    
    async def get_report(self, report_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a report by ID"""
        result = self.client.table("reports").select("*").eq("id", report_id).execute()
        
        if result.data:
            return result.data[0]
        return None
    
    async def update_report_status(self, report_id: str, status: ReportStatus) -> bool:
        """Update the status of a report"""
        result = self.client.table("reports").update({"status": status.value}).eq("id", report_id).execute()
        return len(result.data) > 0

# Singleton instance
supabase_service = SupabaseService()

