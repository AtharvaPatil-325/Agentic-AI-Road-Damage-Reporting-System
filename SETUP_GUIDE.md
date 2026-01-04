# Setup Guide - Road Damage Reporting System

This guide will help you set up and run the complete system.

## Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.10+
- **Supabase Account** (free tier works)
- **OpenAI API Key** (for vision analysis - optional but recommended)
- **relay.app Webhook URL** (for authority notifications)

## Step 1: Backend Setup

1. **Navigate to backend directory:**
```bash
cd backend
```

2. **Create virtual environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Fill in your credentials:
     ```
     SUPABASE_URL=https://your-project.supabase.co
     SUPABASE_KEY=your-anon-key
     RELAY_APP_WEBHOOK_URL=https://your-relay-app-endpoint.com/webhook
     OPENAI_API_KEY=sk-your-openai-key
     ENVIRONMENT=development
     ```

5. **Set up Supabase database:**
   - Go to your Supabase project dashboard
   - Navigate to SQL Editor
   - Run the SQL script from `supabase_setup.sql`
   - This creates the `reports` table and necessary indexes

6. **Create uploads directory:**
```bash
mkdir uploads
```

7. **Run the backend server:**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Step 2: Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

3. **Configure environment:**
   - Copy `.env.example` to `.env`
   - Set the API URL:
     ```
     VITE_API_URL=http://localhost:8000
     ```

4. **Run the development server:**
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000` (or the port Vite assigns)

## Step 3: Testing the System

1. **Open the frontend** in your browser
2. **Start a report:**
   - Upload a road damage image
   - Select or enter location
   - Choose damage type and severity
   - Add optional remarks
   - Submit the report

3. **Verify:**
   - Check Supabase dashboard to see the report in the database
   - Check your relay.app webhook endpoint to see the notification payload

## Step 4: Production Deployment

### Backend:
- Deploy to services like Railway, Render, or AWS
- Set environment variables in your hosting platform
- Use a proper file storage service (S3, Cloudinary) for images instead of local storage
- Set up proper CORS origins for your frontend domain

### Frontend:
- Build for production: `npm run build`
- Deploy to Vercel, Netlify, or similar
- Update `VITE_API_URL` to point to your production backend

## Troubleshooting

### Backend Issues:
- **Supabase connection errors**: Verify your URL and key are correct
- **Webhook failures**: Check that RELAY_APP_WEBHOOK_URL is accessible
- **Image upload errors**: Ensure `uploads` directory exists and is writable

### Frontend Issues:
- **API connection errors**: Verify VITE_API_URL matches your backend URL
- **CORS errors**: Check backend CORS settings include your frontend origin
- **Image upload not working**: Check backend is running and accessible

## Architecture Notes

- **LangGraph Workflow**: The agentic workflow is defined in `backend/app/agents/workflow.py`
- **Webhook Payload**: Reports are sent to relay.app with structured JSON (see backend README)
- **Database Schema**: All reports are stored in Supabase with geospatial indexing
- **Image Storage**: Currently uses local storage; upgrade to CDN for production

## Next Steps

- Enhance authority mapping with geospatial database
- Add email/SMS notifications
- Implement report status tracking
- Add admin dashboard for authorities
- Integrate with mapping services for better location accuracy


