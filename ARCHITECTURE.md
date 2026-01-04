# System Architecture - Road Damage Reporting

## Overview

This system implements an **Agentic AI-based Road Damage Reporting and Authority Notification System** using LangGraph for intelligent workflow orchestration, React for the frontend, and FastAPI for the backend.

## System Components

### 1. Frontend (React + Vite + Tailwind)

**Location**: `frontend/`

**Key Components**:
- **ChatInterface**: Main orchestrator that manages the reporting workflow
- **ImageUpload**: Handles image upload with drag-and-drop
- **LocationPicker**: GPS-based or manual location selection
- **DamageTypeSelector**: Visual selection of damage types
- **SeveritySelector**: Three-level severity assessment
- **MessageBubble**: Displays chat messages with metadata

**Workflow**:
1. User initiates report → Greeting message
2. Image upload → Vision analysis trigger
3. Location selection → Authority mapping preparation
4. Damage type selection → Categorization
5. Severity selection → Priority calculation
6. Remarks (optional) → Final validation
7. Submission → Webhook trigger

### 2. Backend (FastAPI + Python)

**Location**: `backend/app/`

#### API Endpoints

**Reports Router** (`/api/reports`):
- `POST /submit`: Submit complete report with validation
- `GET /{report_id}`: Retrieve report by ID

**Chat Router** (`/api`):
- `POST /chat`: Handle AI assistant chat interactions

**Analysis Router** (`/api`):
- `POST /analyze-image`: Analyze road damage images using OpenAI Vision

#### Services

**SupabaseService**:
- Database operations (create, read, update reports)
- Lazy initialization for flexibility
- Handles report storage with geospatial data

**AuthorityService**:
- Maps locations to responsible authorities
- Determines jurisdiction (city/county/state)
- Returns authority contact information

**WebhookService**:
- Sends structured JSON payloads to relay.app
- Handles retries and error logging
- Calculates priority based on severity

**StorageService**:
- Handles image uploads
- Generates unique filenames
- Returns accessible URLs

### 3. Agentic AI Workflow (LangGraph)

**Location**: `backend/app/agents/workflow.py`

**Agent Nodes**:

1. **Greeting Agent**
   - Welcomes users
   - Explains the reporting process
   - Sets initial workflow state

2. **Vision Analysis Agent**
   - Processes uploaded images
   - Detects road damage
   - Provides analysis feedback

3. **Location & Authority Mapping Agent**
   - Processes location data
   - Identifies responsible authority
   - Maps to appropriate department

4. **Validation Agent**
   - Checks data completeness
   - Validates all required fields
   - Ensures quality standards

5. **Decision & Orchestration Agent**
   - Determines next workflow step
   - Routes to appropriate agent
   - Manages state transitions

6. **Action Agent**
   - Triggers final submission
   - Initiates webhook notifications
   - Confirms completion

**Workflow Graph**:
```
Greeting → Vision Analysis → Location/Authority → Validation → Decision → Action → END
```

**Conditional Edges**:
- Validation passes → Proceed to submission
- Validation fails → Return to data collection
- Image analysis → Route based on detection results

### 4. Database (Supabase)

**Schema**: See `backend/supabase_setup.sql`

**Tables**:
- `reports`: Stores all road damage reports
  - Location (lat/lng with geospatial index)
  - Damage details (type, severity, remarks)
  - Status tracking
  - Authority information
  - Timestamps

**Features**:
- Geospatial indexing for location queries
- Row Level Security (RLS) policies
- Automatic timestamp updates
- Status-based filtering

### 5. Integrations

#### Supabase Integration
- **Purpose**: Persistent storage
- **Operations**: Create, read, update reports
- **Security**: RLS policies for access control

#### relay.app Webhook
- **Purpose**: Authority notifications
- **Trigger**: After successful report validation
- **Payload Structure**:
  ```json
  {
    "event_type": "road_damage_report",
    "report_id": "uuid",
    "timestamp": "ISO8601",
    "location": {...},
    "damage_details": {...},
    "responsible_authority": {...},
    "status": "submitted",
    "priority": "urgent|high|normal"
  }
  ```

#### OpenAI Vision API
- **Purpose**: Image analysis
- **Model**: gpt-4-vision-preview
- **Function**: Detect and classify road damage
- **Fallback**: Mock responses if API unavailable

## Data Flow

### Report Submission Flow

1. **User Interaction** (Frontend)
   - User uploads image → Stored temporarily
   - User selects location → GPS or manual input
   - User selects damage type → Categorized
   - User selects severity → Prioritized
   - User adds remarks → Optional details

2. **Frontend Processing**
   - Validates required fields
   - Prepares FormData payload
   - Sends to `/api/reports/submit`

3. **Backend Processing**
   - Receives and validates data
   - Saves image to storage
   - Creates report in Supabase
   - Identifies responsible authority
   - Triggers webhook to relay.app
   - Returns confirmation with report ID

4. **Webhook Notification**
   - Structured JSON payload
   - Includes all report details
   - Authority contact information
   - Priority level calculation

5. **User Confirmation**
   - Frontend displays success message
   - Shows reference ID
   - Option to submit another report

## Security Considerations

1. **Input Validation**: Pydantic schemas validate all inputs
2. **File Upload**: Type checking and size limits (can be added)
3. **CORS**: Configured for specific origins
4. **Environment Variables**: Sensitive data in .env files
5. **Database**: RLS policies for access control
6. **API Keys**: Stored securely, not in code

## Scalability Considerations

1. **Image Storage**: Currently local; should migrate to CDN (S3, Cloudinary)
2. **Database**: Supabase scales automatically
3. **API**: FastAPI supports async operations
4. **Caching**: Can add Redis for frequently accessed data
5. **Load Balancing**: Can deploy multiple backend instances

## Error Handling

1. **Frontend**: Try-catch blocks with user-friendly messages
2. **Backend**: HTTPException with appropriate status codes
3. **Services**: Graceful degradation (e.g., mock responses if API fails)
4. **Webhooks**: Logged but don't fail the request
5. **Database**: Transaction rollback on errors

## Future Enhancements

1. **Real-time Updates**: WebSocket for status changes
2. **Email Notifications**: Send confirmations to users
3. **Admin Dashboard**: For authorities to manage reports
4. **Mobile App**: React Native version
5. **Advanced Analytics**: Damage pattern analysis
6. **Geospatial Queries**: Find nearby reports
7. **Image Processing**: Automatic damage measurement
8. **Multi-language Support**: i18n for global deployment

## Testing Strategy

1. **Unit Tests**: Test individual services and functions
2. **Integration Tests**: Test API endpoints
3. **E2E Tests**: Test complete user workflows
4. **Load Tests**: Test system under load
5. **Security Tests**: Test input validation and access control

## Monitoring & Logging

1. **Application Logs**: Python logging for backend
2. **Error Tracking**: Sentry or similar
3. **Performance Monitoring**: APM tools
4. **Webhook Monitoring**: Track delivery success
5. **Database Monitoring**: Query performance


