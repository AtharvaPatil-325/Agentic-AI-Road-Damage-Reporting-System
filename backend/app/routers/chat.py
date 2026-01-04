"""
API router for chat interactions with AI assistant
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any

router = APIRouter()

class ChatMessage(BaseModel):
    """Chat message schema"""
    message: str
    step: Optional[str] = None
    report_data: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    """Chat response schema"""
    message: str
    next_step: Optional[str] = None
    requires_input: bool = True

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_message: ChatMessage):
    """
    Handle chat interactions with the AI assistant
    
    This endpoint processes user messages and determines the next step
    in the reporting workflow.
    """
    user_message = chat_message.message.lower()
    current_step = chat_message.step or "greeting"
    
    # Simple rule-based responses (in production, this would use LangGraph workflow)
    if current_step == "greeting" or "hello" in user_message or "hi" in user_message:
        return ChatResponse(
            message="Hello! I'll help you report road damage. Let's start by uploading a photo of the damage.",
            next_step="image",
            requires_input=True
        )
    
    elif "location" in user_message or current_step == "location":
        return ChatResponse(
            message="Please provide the location using the map picker or by entering coordinates.",
            next_step="location",
            requires_input=True
        )
    
    elif "type" in user_message or "damage" in user_message or current_step == "damageType":
        return ChatResponse(
            message="What type of damage is this? Please select from the options provided.",
            next_step="damageType",
            requires_input=True
        )
    
    elif "severity" in user_message or "how bad" in user_message or current_step == "severity":
        return ChatResponse(
            message="How severe is this damage? Please select the severity level.",
            next_step="severity",
            requires_input=True
        )
    
    elif "remarks" in user_message or "additional" in user_message or current_step == "remarks":
        return ChatResponse(
            message="Would you like to add any additional remarks or details?",
            next_step="remarks",
            requires_input=True
        )
    
    else:
        return ChatResponse(
            message="I understand. Please continue with the reporting process using the options provided.",
            next_step=current_step,
            requires_input=True
        )


