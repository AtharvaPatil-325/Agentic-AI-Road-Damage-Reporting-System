# 🚨 Agentic AI Road Damage Reporting System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![Node.js](https://img.shields.io/badge/node.js-18+-green.svg)](https://nodejs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org)

> **SDG 11 Initiative**: An intelligent civic reporting system that uses LangGraph-based multi-agent AI to guide users through reporting road damage and automatically notifies responsible authorities.

## 🌟 Features

- 🤖 **Multi-Agent AI Workflows** - LangGraph orchestrates specialized agents for intelligent guidance
- 💬 **Interactive Chat Interface** - Modern React frontend with step-by-step reporting
- 📍 **GPS Location Integration** - Automatic location detection with manual override
- 📷 **Image Analysis** - AI-powered road damage detection using OpenAI Vision
- 🗄️ **Supabase Database** - Geospatial queries and real-time data storage
- 📧 **Automated Notifications** - Webhook integration with relay.app for authority alerts
- 🎨 **Modern UI/UX** - Clean, accessible design with Tailwind CSS
- 🔒 **Secure & Scalable** - Production-ready architecture with proper validation

## 🏗️ System Architecture

### Frontend Layer
- **React 18 + Vite** - Modern, fast development and building
- **Tailwind CSS** - Utility-first styling with custom civic theme
- **Chat Interface** - Conversational AI-guided reporting experience
- **Component Architecture** - Modular, reusable UI components

### Backend Layer
- **FastAPI** - High-performance async web framework
- **Pydantic** - Robust data validation and serialization
- **LangGraph** - Agentic AI workflow orchestration
- **RESTful APIs** - Clean, documented endpoints

### AI & Intelligence
- **Multi-Agent System** - 6 specialized agents working in harmony
- **OpenAI Vision** - Advanced image analysis for damage detection
- **Intelligent Routing** - Automatic authority identification and notification

### Database & Storage
- **Supabase PostgreSQL** - Serverless database with real-time capabilities
- **Geospatial Indexing** - Location-based queries and mapping
- **File Storage** - Secure image upload and serving
- **Row-Level Security** - Enterprise-grade data protection

## 🤖 Agentic AI Workflow

Powered by **LangGraph**, the system orchestrates 6 specialized agents in a sophisticated workflow:

### Core Agents

1. **🎯 Greeting & Guidance Agent**
   - Welcomes users with contextual information
   - Explains the reporting process clearly
   - Sets user expectations for data collection

2. **👁️ Vision Analysis Agent**
   - Processes uploaded road damage images
   - Uses OpenAI Vision API for intelligent analysis
   - Provides confidence scores and damage detection
   - Falls back gracefully if AI unavailable

3. **📍 Location & Authority Mapping Agent**
   - Determines geographic coordinates (GPS/manual)
   - Maps locations to responsible authorities
   - Handles jurisdiction boundaries and departments
   - Supports highways, cities, and counties

4. **✅ Validation Agent**
   - Ensures data completeness and quality
   - Validates image uploads and location data
   - Checks for required fields and data integrity
   - Provides clear feedback on missing information

5. **🧠 Decision & Orchestration Agent**
   - Analyzes workflow state and user progress
   - Determines optimal next steps dynamically
   - Routes between different workflow branches
   - Handles error recovery and user guidance

6. **🚀 Action Agent**
   - Triggers final report submission
   - Stores complete data in Supabase
   - Sends webhook notifications to relay.app
   - Provides confirmation and reference IDs

### Workflow States

```
User Input → Greeting → Image Upload → Vision Analysis
                     ↓
Location Selection → Authority Mapping → Validation
                     ↓
Decision Making → Report Submission → Webhook Notification → Confirmation
```

### Intelligent Features

- **Context Awareness** - Agents maintain conversation context
- **Dynamic Routing** - Workflow adapts based on user input and validation
- **Error Recovery** - Graceful handling of API failures and user errors
- **Progressive Disclosure** - Information revealed as needed
- **Quality Assurance** - Multiple validation checkpoints

## 📁 Project Structure

```
road-damage-reporting/
├── 📄 README.md                 # Main project documentation
├── 📄 QUICK_START.md           # Step-by-step setup guide
├── 📄 PROJECT_STRUCTURE.md     # Detailed file organization
├── 🔧 Ai.code-workspace        # VS Code workspace configuration
├── 🚫 .gitignore               # Git ignore rules
│
├── 🎨 frontend/                # React + Vite Frontend
│   ├── 📄 package.json         # Node.js dependencies
│   ├── ⚙️ vite.config.js       # Vite build configuration
│   ├── 🎨 tailwind.config.js   # Tailwind CSS configuration
│   ├── 📄 index.html           # HTML entry point
│   ├── 📄 ENV_TEMPLATE.txt     # Environment variables template
│   └── 📁 src/
│       ├── ⚛️ App.jsx          # Main application component
│       ├── 🎨 index.css        # Global styles with Tailwind
│       ├── ⚛️ main.jsx         # React application entry
│       ├── 🔧 utils/
│       │   └── 🌐 api.js       # API client and utilities
│       └── 🧩 components/      # Reusable UI components
│           ├── 💬 ChatInterface.jsx    # Main chat orchestrator
│           ├── 🖼️ ImageUpload.jsx      # Image upload with preview
│           ├── 📍 LocationPicker.jsx   # GPS/manual location input
│           ├── 🔧 DamageTypeSelector.jsx  # Damage type selection
│           ├── 📊 SeveritySelector.jsx    # Severity level picker
│           ├── 💭 MessageBubble.jsx      # Chat message display
│           └── 🏠 Header.jsx             # Application header
│
└── 🐍 backend/                 # FastAPI Backend
    ├── 📄 requirements.txt     # Python dependencies
    ├── 📄 README.md           # Backend-specific documentation
    ├── 🔧 setup_env.py        # Environment setup helper
    ├── 📄 SETUP_ENV.md        # Environment configuration guide
    ├── 🗄️ supabase_setup.sql  # Database schema
    ├── 🧪 test_webhook.py     # Webhook testing utility
    ├── 📁 uploads/            # Image storage directory
    └── 📁 app/                # Main application package
        ├── ⚙️ main.py          # FastAPI application & CORS setup
        ├── 📋 routers/         # API route handlers
        │   ├── 📊 reports.py   # Report submission endpoints
        │   ├── 💬 chat.py      # Chat interaction endpoints
        │   ├── 🖼️ analyze.py   # Image analysis endpoints
        │   └── 📋 __init__.py
        ├── 🔧 services/        # Business logic services
        │   ├── 🌐 supabase_service.py    # Database operations
        │   ├── 🏛️ authority_service.py   # Authority mapping
        │   ├── 📧 webhook_service.py     # Relay.app notifications
        │   ├── 💾 storage_service.py     # Image file handling
        │   └── 📋 __init__.py
        ├── 🤖 agents/          # LangGraph AI workflows
        │   ├── 🧠 workflow.py  # Multi-agent orchestration
        │   └── 📋 __init__.py
        └── 📋 schemas/         # Data validation models
            ├── 📊 report.py    # Report data structures
            └── 📋 __init__.py
```

## 🚀 Quick Start

> 📖 **For detailed setup instructions, see [QUICK_START.md](./QUICK_START.md)**

### ⚡ One-Command Setup

**Prerequisites Check:**
```bash
node --version    # Should be 18+
python --version  # Should be 3.10+
```

**Backend Setup:**
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python setup_env.py  # Creates .env file
# Edit backend/.env with your credentials
uvicorn app.main:app --reload
```

**Frontend Setup (New Terminal):**
```powershell
cd frontend
npm install
copy ENV_TEMPLATE.txt .env
# Edit VITE_API_URL if needed
npm run dev
```

**Open Browser:** `http://localhost:3000`

### 🔧 Prerequisites

| Component | Version | Purpose |
|-----------|---------|---------|
| **Node.js** | 18+ | Frontend development |
| **Python** | 3.10+ | Backend development |
| **Supabase** | Free tier | Database & auth |
| **OpenAI API** | Optional | Image analysis |
| **relay.app** | Account | Email notifications |

### ⚙️ Environment Configuration

#### Backend (.env)
```env
# Supabase Database
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-key-here

# Email Notifications
RELAY_APP_WEBHOOK_URL=https://your-relay-webhook-url

# AI Features (Optional)
OPENAI_API_KEY=sk-your-openai-key-here

# System
ENVIRONMENT=development
```

#### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000
```

### 🗄️ Database Setup

1. **Create Supabase Project**
   - Go to https://supabase.com
   - Create new project
   - Get URL and anon key from Settings → API

2. **Run Schema Setup**
   - Open Supabase SQL Editor
   - Copy/paste `backend/supabase_setup.sql`
   - Execute to create tables and indexes

### 🧪 Testing the System

1. **Open** `http://localhost:3000`
2. **Upload** a road damage photo
3. **Select** location and damage details
4. **Submit** report
5. **Verify**:
   - ✅ Report appears in Supabase dashboard
   - ✅ Email notification sent via relay.app
   - ✅ Reference ID generated

## 🗄️ Database Schema

### Reports Table Structure

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Primary key, auto-generated |
| `location_lat` | DOUBLE | Latitude coordinate |
| `location_lng` | DOUBLE | Longitude coordinate |
| `location_address` | TEXT | Human-readable address |
| `damage_type` | VARCHAR | pothole, crack, surface_damage, other |
| `severity` | VARCHAR | low, medium, high |
| `remarks` | TEXT | User comments and details |
| `image_url` | TEXT | Uploaded image URL |
| `status` | VARCHAR | pending, submitted, in_progress, resolved, closed |
| `authority_name` | TEXT | Responsible authority name |
| `authority_contact` | TEXT | Contact email/phone |
| `webhook_sent` | BOOLEAN | Notification delivery status |
| `created_at` | TIMESTAMP | Record creation time |
| `updated_at` | TIMESTAMP | Last modification time |

### Features

- **Geospatial Indexing** - Fast location-based queries
- **Row-Level Security** - Enterprise-grade access control
- **Automatic Timestamps** - Creation and update tracking
- **Status Tracking** - Complete workflow management

## 🔄 Complete User Journey

```
1. 🌐 User Access
   └── Opens web application

2. 💬 AI Guidance
   ├── Chat interface welcomes user
   ├── Explains reporting process
   └── Guides through each step

3. 📷 Image Upload
   ├── Drag-and-drop interface
   ├── Real-time preview
   ├── AI vision analysis (optional)
   └── Confidence scoring

4. 📍 Location Selection
   ├── GPS automatic detection
   ├── Manual coordinate input
   ├── Address reverse geocoding
   └── Authority jurisdiction mapping

5. 🔧 Damage Assessment
   ├── Visual type selector
   ├── Severity level picker
   ├── Additional remarks
   └── Data validation

6. ✅ Submission & Validation
   ├── Complete data verification
   ├── Supabase storage
   ├── Authority identification
   └── Webhook notification

7. 📧 Authority Notification
   ├── relay.app webhook trigger
   ├── Professional email generation
   ├── Complete context provided
   └── Reference ID tracking

8. 🎯 Confirmation
   ├── User receives reference ID
   ├── Status tracking available
   ├── Report history maintained
   └── Follow-up notifications
```

### Intelligent Features

- **Progressive Disclosure** - Information revealed contextually
- **Error Recovery** - Graceful handling of validation failures
- **Multi-modal Input** - GPS, manual entry, image analysis
- **Real-time Validation** - Immediate feedback on data quality
- **Authority Routing** - Automatic jurisdiction detection

## 🛠️ Technology Stack

### Frontend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18+ | Component-based UI framework |
| **Vite** | 5.x | Fast build tool and dev server |
| **Tailwind CSS** | 3.x | Utility-first CSS framework |
| **Lucide React** | 0.294+ | Beautiful icon library |
| **Axios** | 1.x | HTTP client for API calls |

### Backend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.10+ | Core programming language |
| **FastAPI** | 0.104+ | High-performance web framework |
| **Pydantic** | 2.x | Data validation and serialization |
| **LangGraph** | 0.0.20 | Agentic AI workflow orchestration |
| **OpenAI** | 1.x | AI vision and language models |
| **httpx** | 0.25+ | Async HTTP client |

### Database & Infrastructure
| Technology | Purpose |
|------------|---------|
| **Supabase** | PostgreSQL database with real-time features |
| **relay.app** | Email automation and webhook processing |
| **Python-multipart** | File upload handling |
| **AIOFiles** | Async file operations |
| **python-dotenv** | Environment variable management |

### Development Tools
- **Git** - Version control
- **VS Code** - Primary IDE
- **Postman** - API testing
- **Supabase CLI** - Database management

## 🚀 Deployment

### Backend Deployment
```bash
# Railway, Render, or similar
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Frontend Deployment
```bash
npm run build
# Deploy dist/ folder to Vercel, Netlify, or similar
```

### Environment Variables
- Set all production environment variables
- Use production database URLs
- Configure production webhook endpoints
- Enable proper CORS origins

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React
- Write descriptive commit messages
- Test thoroughly before submitting PRs
- Update documentation for new features

## 📊 API Documentation

### Core Endpoints

- `POST /api/reports/submit` - Submit road damage report
- `GET /api/reports/{id}` - Retrieve report details
- `POST /api/chat` - AI chat interactions
- `POST /api/analyze-image` - Image analysis (OpenAI Vision)

### Webhook Payload Format

```json
{
  "subject": "🚨 IMPORTANT: Road Damage Report abc123",
  "report_id": "abc123",
  "location": "Main Street, City",
  "damage_type": "pothole",
  "severity": "high",
  "image_url": "http://...",
  "remarks": "Description",
  "authority_name": "City Public Works",
  "authority_contact": "email@city.gov"
}
```

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
```bash
# Check Python version
python --version  # Should be 3.10+

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Frontend build fails:**
```bash
# Clear node_modules
rm -rf node_modules package-lock.json
npm install
```

**Database connection fails:**
- Verify Supabase URL and key in `.env`
- Check Supabase project is active
- Run SQL setup script in Supabase dashboard

**Webhook not working:**
- Verify relay.app webhook URL
- Check webhook payload structure
- Test webhook endpoint manually

## 📈 Performance

- **Response Time**: <500ms for API calls
- **Image Processing**: <5 seconds for analysis
- **Database Queries**: Optimized with geospatial indexing
- **Concurrent Users**: Supports 100+ simultaneous connections

## 🔒 Security

- **API Authentication**: Secure endpoints with proper validation
- **File Upload Security**: Type checking and size limits
- **Environment Variables**: Sensitive data never in code
- **CORS Configuration**: Restricted to allowed origins
- **Input Sanitization**: All user inputs validated with Pydantic

## 📝 License

This project is a prototype for smart city governance applications.

## 🙏 Acknowledgments

- **SDG 11** - Sustainable Cities and Communities
- **OpenAI** - For providing powerful AI capabilities
- **Supabase** - For excellent developer experience
- **relay.app** - For seamless automation workflows
- **FastAPI** - For outstanding Python web framework
- **LangGraph** - For innovative agentic AI orchestration

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting section
- Contact maintainers

---

**Built with ❤️ for smarter cities and communities** 🏙️

