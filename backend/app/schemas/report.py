"""
Pydantic schemas for report data validation
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class DamageType(str, Enum):
    """Enumeration of damage types"""
    POTHOLE = "pothole"
    CRACK = "crack"
    SURFACE_DAMAGE = "surface_damage"
    OTHER = "other"

class Severity(str, Enum):
    """Enumeration of severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Location(BaseModel):
    """Location schema"""
    lat: float = Field(..., ge=-90, le=90, description="Latitude")
    lng: float = Field(..., ge=-180, le=180, description="Longitude")
    address: Optional[str] = Field(None, description="Human-readable address")

class ReportCreate(BaseModel):
    """Schema for creating a new report"""
    location: Location
    damage_type: DamageType
    severity: Severity
    remarks: Optional[str] = Field(None, max_length=1000)
    image_url: Optional[str] = None

class ReportResponse(BaseModel):
    """Schema for report response"""
    report_id: str
    status: str
    message: str
    authority_notified: bool
    created_at: datetime

class ReportStatus(str, Enum):
    """Report status enumeration"""
    PENDING = "pending"
    SUBMITTED = "submitted"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


