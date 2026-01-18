"""
API router for report submission and management
"""
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
import json
from datetime import datetime
import uuid

from app.schemas.report import ReportCreate, ReportResponse, Location, DamageType, Severity
from app.services.supabase_service import supabase_service
from app.services.authority_service import authority_service
from app.services.webhook_service import webhook_service
from app.services.storage_service import storage_service

router = APIRouter()

@router.post("/submit", response_model=ReportResponse)
async def submit_report(
    image: Optional[UploadFile] = File(None),
    location: str = Form(...),
    damage_type: str = Form(...),
    severity: str = Form(...),
    remarks: Optional[str] = Form(None)
):
    """
    Submit a complete road damage report
    
    This endpoint:
    1. Validates all input data
    2. Stores image if provided
    3. Creates report in Supabase
    4. Identifies responsible authority
    5. Triggers webhook to relay.app
    6. Returns confirmation with report ID
    """
    try:
        # Parse location JSON
        try:
            location_data = json.loads(location)
            location_obj = Location(**location_data)
        except (json.JSONDecodeError, ValueError) as e:
            raise HTTPException(status_code=400, detail=f"Invalid location data: {str(e)}")
        
        # Validate damage type and severity
        try:
            damage_type_enum = DamageType(damage_type)
            severity_enum = Severity(severity)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid damage type or severity: {str(e)}")
        
        # Save image if provided
        image_url = None
        if image:
            image_url = await storage_service.save_image(image)
        
        # Create report data
        report_data = ReportCreate(
            location=location_obj,
            damage_type=damage_type_enum,
            severity=severity_enum,
            remarks=remarks or "No additional remarks",
            image_url=image_url
        )
        
        # Store in Supabase
        try:
            db_report = await supabase_service.create_report(report_data, image_url)
            report_id = db_report.get("id")
            
            if not report_id:
                raise HTTPException(status_code=500, detail="Failed to create report in database")
        except ValueError as e:
            # Supabase configuration error
            raise HTTPException(
                status_code=500, 
                detail=f"Database configuration error: {str(e)}. Please check SUPABASE_URL and SUPABASE_KEY in .env file."
            )
        except Exception as e:
            # Other Supabase errors
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to save report to database: {str(e)}"
            )
        
        # Identify responsible authority
        authority = authority_service.identify_authority(location_obj)
        
        # Send webhook notification to relay.app (non-blocking)
        webhook_sent = False
        try:
            webhook_sent = await webhook_service.send_notification(db_report, authority)
            if not webhook_sent:
                print(f"Warning: Webhook notification failed for report {report_id}")
        except Exception as webhook_error:
            # Log webhook error but don't fail the request
            print(f"Warning: Webhook notification error for report {report_id}: {str(webhook_error)}")
        
        # Determine success message based on webhook status
        if webhook_sent:
            message = "Report submitted successfully. Responsible authority has been notified."
        else:
            message = "Report submitted successfully. (Webhook notification was not sent - check configuration)"

        return ReportResponse(
            report_id=str(report_id),
            status="submitted",
            message=message,
            authority_notified=webhook_sent,
            created_at=datetime.now(),
            image_url=db_report.get("image_url")  # Include image URL in response
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{report_id}")
async def get_report(report_id: str):
    """Retrieve a report by ID"""
    report = await supabase_service.get_report(report_id)
    
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

