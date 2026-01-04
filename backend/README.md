# Backend - Road Damage Reporting API

FastAPI backend with LangGraph-based agentic AI workflows for intelligent road damage reporting.

## Setup

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**
Copy `.env.example` to `.env` and fill in your credentials:
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase anon key
- `RELAY_APP_WEBHOOK_URL`: Your relay.app webhook endpoint
- `OPENAI_API_KEY`: Your OpenAI API key (for vision analysis)

4. **Set up Supabase database:**
Run the SQL script in `supabase_setup.sql` in your Supabase SQL editor to create the necessary tables.

5. **Run the server:**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Reports
- `POST /api/reports/submit` - Submit a new road damage report
- `GET /api/reports/{report_id}` - Get a report by ID

### Chat
- `POST /api/chat` - Chat with AI assistant

### Analysis
- `POST /api/analyze-image` - Analyze road damage image

## Architecture

### Agents (LangGraph)
The system uses multiple specialized agents:
- **Greeting Agent**: Welcomes users and explains the process
- **Vision Analysis Agent**: Analyzes uploaded images
- **Location & Authority Mapping Agent**: Identifies responsible authority
- **Validation Agent**: Ensures data completeness
- **Decision Agent**: Orchestrates workflow steps
- **Action Agent**: Triggers webhooks and finalizes reports

### Services
- **SupabaseService**: Database operations
- **AuthorityService**: Authority identification based on location
- **WebhookService**: Sends notifications to relay.app
- **StorageService**: Handles image uploads

## Webhook Payload Format

Reports are sent to relay.app with the following JSON structure:

```json
{
  "event_type": "road_damage_report",
  "report_id": "uuid",
  "timestamp": "2024-01-01T00:00:00Z",
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "address": "Main Street, City"
  },
  "damage_details": {
    "type": "pothole",
    "severity": "high",
    "description": "Large pothole in the middle of the road",
    "image_url": "http://..."
  },
  "responsible_authority": {
    "name": "City Public Works Department",
    "department": "Infrastructure Maintenance",
    "contact": "publicworks@city.gov"
  },
  "status": "submitted",
  "priority": "urgent"
}
```


