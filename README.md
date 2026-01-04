# Agentic AI Road Damage Reporting System

An intelligent civic reporting system that uses LangGraph-based multi-agent AI to guide users through reporting road damage and automatically notifies responsible authorities.

## 🎯 Project Overview

This system aligns with SDG 11 (Sustainable Cities and Communities) by providing an AI-powered platform for citizens to report road damage efficiently. The system uses agentic AI workflows to intelligently guide users, validate inputs, and route reports to appropriate authorities.

## 🏗️ Architecture

### Frontend
- **React + Vite**: Modern, fast frontend framework
- **Tailwind CSS**: Utility-first styling for clean UI
- **Chat Interface**: AI chatbot-style guided reporting experience

### Backend
- **FastAPI**: High-performance Python web framework
- **Pydantic**: Data validation and serialization
- **LangGraph**: Agentic AI workflow orchestration

### Database & Integrations
- **Supabase**: PostgreSQL database for report storage
- **relay.app**: Webhook integration for authority notifications

## 🤖 Agentic AI Flow

The system uses LangGraph to orchestrate multiple specialized agents:

1. **Greeting & Guidance Agent**: Welcomes users and explains the process
2. **Vision Analysis Agent**: Analyzes uploaded road damage images
3. **Location & Authority Mapping Agent**: Identifies responsible authority based on location
4. **Validation Agent**: Ensures all required data is complete and valid
5. **Decision & Orchestration Agent**: Determines next steps in the workflow
6. **Action Agent**: Triggers webhook notifications and stores data

## 📁 Project Structure

```
road-damage-reporting/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── utils/
│   ├── package.json
│   └── vite.config.js
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── agents/
│   │   ├── schemas/
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
└── README.md
```

## 🚀 Quick Start

**For detailed step-by-step instructions, see [QUICK_START.md](./QUICK_START.md)**

### Quick Commands

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# OR source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
# Create .env file with your credentials (see .env.example)
uvicorn app.main:app --reload
```

**Frontend (in a new terminal):**
```bash
cd frontend
npm install
# Create .env file with VITE_API_URL=http://localhost:8000
npm run dev
```

**Then open:** http://localhost:5173 (or the port shown)

### Prerequisites
- Node.js 18+
- Python 3.10+
- Supabase account (free tier works)
- OpenAI API key (optional but recommended)
- relay.app webhook endpoint

### Environment Variables

Create `.env` files in both frontend and backend:

**Backend `.env`:**
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
RELAY_APP_WEBHOOK_URL=your_relay_app_webhook_url
OPENAI_API_KEY=your_openai_api_key  # For vision analysis
```

**Frontend `.env`:**
```
VITE_API_URL=http://localhost:8000
```

## 📊 Database Schema

The system stores reports in Supabase with the following structure:
- Report ID (UUID)
- User location (lat/lng)
- Damage type
- Severity level
- Image URL
- User remarks
- Responsible authority
- Status
- Created timestamp

## 🔄 Workflow

1. User initiates report via chat interface
2. AI guides through step-by-step data collection
3. Image upload triggers vision analysis
4. Location determines responsible authority
5. Validation ensures completeness
6. Report stored in Supabase
7. Webhook POST to relay.app with structured JSON
8. User receives confirmation with reference ID

## 🛠️ Technology Stack

- **Frontend**: React, Vite, Tailwind CSS
- **Backend**: Python, FastAPI, Pydantic
- **AI**: LangGraph, OpenAI (for vision)
- **Database**: Supabase (PostgreSQL)
- **Integrations**: relay.app webhooks

## 📝 License

This project is a prototype for smart city governance applications.

