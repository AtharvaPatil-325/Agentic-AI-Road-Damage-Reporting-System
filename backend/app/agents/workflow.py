"""
LangGraph-based agentic workflow for road damage reporting
"""
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
import os

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

class AgentState(TypedDict):
    """State shared across all agents"""
    step: str
    messages: Annotated[list, lambda x, y: x + y]
    report_data: dict
    validation_status: str
    next_action: str

def greeting_agent(state: AgentState) -> AgentState:
    """
    Greeting & Guidance Agent
    Welcomes user and explains the reporting process
    """
    if state["step"] == "greeting":
        message = (
            "Hello! I'm your AI assistant for reporting road damage. "
            "I'll guide you through the process step by step. "
            "Let's start by uploading a photo of the road damage."
        )
        return {
            "messages": [AIMessage(content=message)],
            "next_action": "collect_image"
        }
    return state

def vision_analysis_agent(state: AgentState) -> AgentState:
    """
    Vision Analysis Agent
    Analyzes uploaded road damage images (placeholder - would use vision API)
    """
    if state["step"] == "analyze_image":
        # In production, this would call OpenAI Vision API or similar
        message = (
            "I've analyzed your image. I can see road damage in the photo. "
            "Now, please provide the location of this damage."
        )
        return {
            "messages": [AIMessage(content=message)],
            "report_data": {**state["report_data"], "image_analyzed": True},
            "next_action": "collect_location"
        }
    return state

def location_authority_agent(state: AgentState) -> AgentState:
    """
    Location & Authority Mapping Agent
    Identifies responsible authority based on location
    """
    if state["step"] == "map_authority" and state["report_data"].get("location"):
        location = state["report_data"]["location"]
        
        # Determine authority (simplified logic)
        authority = "City Public Works Department"
        if location.get("address", "").lower().find("highway") != -1:
            authority = "State Department of Transportation"
        
        message = f"Location confirmed. The responsible authority is: {authority}."
        
        return {
            "messages": [AIMessage(content=message)],
            "report_data": {
                **state["report_data"],
                "authority": authority
            },
            "next_action": "collect_damage_type"
        }
    return state

def validation_agent(state: AgentState) -> AgentState:
    """
    Validation Agent
    Ensures all required data is complete and valid
    """
    report_data = state["report_data"]
    missing_fields = []
    
    required_fields = {
        "image": "image",
        "location": "location",
        "damage_type": "damage type",
        "severity": "severity"
    }
    
    for field, label in required_fields.items():
        if not report_data.get(field):
            missing_fields.append(label)
    
    if missing_fields:
        message = f"Please provide: {', '.join(missing_fields)}"
        return {
            "messages": [AIMessage(content=message)],
            "validation_status": "incomplete",
            "next_action": "collect_missing_data"
        }
    else:
        return {
            "validation_status": "complete",
            "next_action": "submit_report"
        }

def decision_agent(state: AgentState) -> AgentState:
    """
    Decision & Orchestration Agent
    Determines next steps in the workflow
    """
    current_step = state["step"]
    next_action = state.get("next_action", "")
    
    # Route to appropriate next step
    step_mapping = {
        "collect_image": "image",
        "collect_location": "location",
        "collect_damage_type": "damage_type",
        "collect_severity": "severity",
        "collect_remarks": "remarks",
        "submit_report": "submit"
    }
    
    next_step = step_mapping.get(next_action, current_step)
    
    return {
        "step": next_step
    }

def action_agent(state: AgentState) -> AgentState:
    """
    Action Agent
    Triggers webhook notifications and finalizes report
    """
    if state["step"] == "submit" and state["validation_status"] == "complete":
        message = (
            "All information has been validated. "
            "Your report is being submitted to the responsible authority."
        )
        return {
            "messages": [AIMessage(content=message)],
            "next_action": "complete"
        }
    return state

# Build the workflow graph
def create_workflow():
    """Create and return the LangGraph workflow"""
    workflow = StateGraph(AgentState)
    
    # Add nodes (agents)
    workflow.add_node("greeting", greeting_agent)
    workflow.add_node("vision_analysis", vision_analysis_agent)
    workflow.add_node("location_authority", location_authority_agent)
    workflow.add_node("validation", validation_agent)
    workflow.add_node("decision", decision_agent)
    workflow.add_node("action", action_agent)
    
    # Define edges
    workflow.set_entry_point("greeting")
    
    workflow.add_edge("greeting", "vision_analysis")
    workflow.add_conditional_edges(
        "vision_analysis",
        lambda x: "location_authority" if x["report_data"].get("image") else "greeting",
        {
            "location_authority": "location_authority",
            "greeting": "greeting"
        }
    )
    workflow.add_edge("location_authority", "validation")
    workflow.add_conditional_edges(
        "validation",
        lambda x: "decision" if x["validation_status"] == "complete" else "decision",
        {
            "decision": "decision"
        }
    )
    workflow.add_conditional_edges(
        "decision",
        lambda x: "action" if x["step"] == "submit" else END,
        {
            "action": "action",
            END: END
        }
    )
    workflow.add_edge("action", END)
    
    return workflow.compile()

# Export workflow instance
workflow = create_workflow()


