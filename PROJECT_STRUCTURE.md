# Project Structure

```
road-damage-reporting/
│
├── README.md                    # Main project documentation
├── SETUP_GUIDE.md              # Step-by-step setup instructions
├── ARCHITECTURE.md             # System architecture documentation
├── PROJECT_STRUCTURE.md        # This file
├── .gitignore                  # Git ignore rules
│
├── frontend/                   # React + Vite frontend
│   ├── package.json            # Frontend dependencies
│   ├── vite.config.js          # Vite configuration
│   ├── tailwind.config.js      # Tailwind CSS configuration
│   ├── postcss.config.js       # PostCSS configuration
│   ├── index.html              # HTML entry point
│   ├── .env.example            # Frontend environment template
│   ├── README.md               # Frontend-specific README
│   │
│   └── src/
│       ├── main.jsx            # React entry point
│       ├── App.jsx             # Main app component
│       ├── index.css           # Global styles with Tailwind
│       │
│       ├── components/         # React components
│       │   ├── Header.jsx      # App header with branding
│       │   ├── ChatInterface.jsx    # Main chat UI and workflow
│       │   ├── MessageBubble.jsx    # Chat message display
│       │   ├── ImageUpload.jsx      # Image upload component
│       │   ├── LocationPicker.jsx   # Location selection
│       │   ├── DamageTypeSelector.jsx  # Damage type selection
│       │   └── SeveritySelector.jsx     # Severity selection
│       │
│       └── utils/
│           └── api.js          # API client utilities
│
├── backend/                    # FastAPI backend
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # Backend environment template
│   ├── README.md               # Backend-specific README
│   ├── supabase_setup.sql      # Database schema SQL
│   │
│   └── app/
│       ├── __init__.py
│       ├── main.py             # FastAPI application entry
│       │
│       ├── routers/            # API route handlers
│       │   ├── __init__.py
│       │   ├── reports.py      # Report submission endpoints
│       │   ├── chat.py         # Chat interaction endpoints
│       │   └── analyze.py      # Image analysis endpoints
│       │
│       ├── services/           # Business logic services
│       │   ├── __init__.py
│       │   ├── supabase_service.py    # Database operations
│       │   ├── authority_service.py   # Authority mapping
│       │   ├── webhook_service.py     # Webhook notifications
│       │   └── storage_service.py     # Image storage
│       │
│       ├── schemas/            # Pydantic data models
│       │   ├── __init__.py
│       │   └── report.py       # Report schemas and enums
│       │
│       └── agents/             # LangGraph agentic workflows
│           ├── __init__.py
│           └── workflow.py     # Multi-agent workflow definition
│
└── uploads/                    # Image upload directory (created at runtime)
```

## Key Files Explained

### Frontend

- **ChatInterface.jsx**: Main component that orchestrates the entire reporting workflow, manages state, and handles user interactions
- **ImageUpload.jsx**: Handles drag-and-drop and click-to-upload for road damage images
- **LocationPicker.jsx**: GPS-based location detection with manual coordinate entry fallback
- **api.js**: Centralized API client for all backend communication

### Backend

- **main.py**: FastAPI application setup with CORS, routers, and static file serving
- **reports.py**: Main report submission endpoint with validation and webhook triggering
- **workflow.py**: LangGraph workflow with 6 specialized agents for intelligent reporting
- **supabase_service.py**: Database operations with lazy initialization
- **webhook_service.py**: Structured JSON payload generation and delivery to relay.app

### Configuration

- **.env.example**: Template for environment variables (copy to .env)
- **supabase_setup.sql**: Complete database schema with indexes and RLS policies
- **requirements.txt**: Python package dependencies
- **package.json**: Node.js package dependencies

## File Organization Principles

1. **Separation of Concerns**: Frontend, backend, and database logic are clearly separated
2. **Modularity**: Services, routers, and components are in dedicated modules
3. **Scalability**: Structure supports easy addition of new features
4. **Maintainability**: Clear naming conventions and organization
5. **Documentation**: README files at each level explain purpose and usage

## Environment Variables

### Backend (.env)
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
RELAY_APP_WEBHOOK_URL=your_webhook_url
OPENAI_API_KEY=your_openai_key
ENVIRONMENT=development
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
```

## Dependencies

### Backend (Python)
- FastAPI: Web framework
- LangGraph: Agentic workflow orchestration
- Supabase: Database client
- OpenAI: Vision API for image analysis
- Pydantic: Data validation
- httpx: Async HTTP client for webhooks

### Frontend (Node.js)
- React: UI framework
- Vite: Build tool and dev server
- Tailwind CSS: Utility-first styling
- Axios: HTTP client
- Lucide React: Icon library


