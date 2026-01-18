# Quick Start Guide

## Prerequisites Check

Before starting, ensure you have:
- ✅ Node.js 18+ installed (`node --version`)
- ✅ Python 3.10+ installed (`python --version`)
- ✅ npm or yarn installed
- ✅ Supabase account (free tier works)
- ✅ OpenAI API key (optional but recommended)

## Step-by-Step Setup

### 1. Clone/Navigate to Project

```bash
cd "D:\Ai Project"
```

### 2. Backend Setup

#### 2.1 Navigate to Backend
```bash
cd backend
```

#### 2.2 Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2.3 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2.4 Create Environment File
```bash
# Copy the example file
copy .env.example .env  # Windows
# OR
cp .env.example .env    # Mac/Linux
```

#### 2.5 Edit .env File
Open `backend/.env` and add your credentials:
```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-key-here
RELAY_APP_WEBHOOK_URL=https://your-relay-app-endpoint.com/webhook
OPENAI_API_KEY=sk-your-openai-key-here
ENVIRONMENT=development
```

**How to get these values:**
- **SUPABASE_URL & SUPABASE_KEY**: 
  1. Go to https://supabase.com
  2. Create a new project (or use existing)
  3. Go to Settings → API
  4. Copy "Project URL" and "anon public" key

- **RELAY_APP_WEBHOOK_URL**: Your relay.app webhook endpoint URL
- **OPENAI_API_KEY**: Get from https://platform.openai.com/api-keys

#### 2.6 Set Up Database
1. Go to your Supabase project dashboard
2. Click on "SQL Editor" in the left sidebar
3. Open `backend/supabase_setup.sql` file
4. Copy and paste the entire SQL script
5. Click "Run" to execute

#### 2.7 Create Uploads Directory
```bash
mkdir uploads
```

#### 2.8 Start Backend Server
```bash
uvicorn app.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

✅ **Backend is now running on http://localhost:8000**

### 3. Frontend Setup

#### 3.1 Open New Terminal
Keep the backend running, open a **new terminal window**.

#### 3.2 Navigate to Frontend
```bash
cd "D:\Ai Project\frontend"
```

#### 3.3 Install Dependencies
```bash
npm install
```

#### 3.4 Create Environment File
```bash
# Windows
copy .env.example .env
# Mac/Linux
cp .env.example .env
```

#### 3.5 Edit .env File
Open `frontend/.env` and ensure:
```env
VITE_API_URL=http://localhost:8000
```

#### 3.6 Start Frontend Server
```bash
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

✅ **Frontend is now running on http://localhost:5173** (or port shown)

### 4. Test the Application

1. **Open your browser** and go to: `http://localhost:5173`
2. **You should see** the Road Damage Reporter interface
3. **Try submitting a report:**
   - Upload an image (or any image for testing)
   - Select/enter a location
   - Choose damage type
   - Select severity
   - Add remarks (optional)
   - Submit

4. **Check results:**
   - You should see a confirmation with a report ID
   - Check Supabase dashboard → Table Editor → `reports` table
   - Check your relay.app webhook endpoint for the notification

## Troubleshooting

### Backend Issues

**Error: "SUPABASE_URL and SUPABASE_KEY must be set"**
- Solution: Make sure `.env` file exists in `backend/` directory and has correct values

**Error: "Module not found"**
- Solution: Activate virtual environment and run `pip install -r requirements.txt`

**Error: "Port 8000 already in use"**
- Solution: Change port: `uvicorn app.main:app --reload --port 8001`
- Then update `frontend/.env`: `VITE_API_URL=http://localhost:8001`

**Error: "Failed to create report in database"**
- Solution: Make sure you ran the SQL setup script in Supabase

### Frontend Issues

**Error: "Cannot connect to API"**
- Solution: 
  1. Check backend is running
  2. Verify `VITE_API_URL` in `frontend/.env` matches backend URL
  3. Check browser console for CORS errors

**Error: "npm install fails"**
- Solution: 
  1. Delete `node_modules` folder
  2. Delete `package-lock.json`
  3. Run `npm install` again

**Blank page or build errors**
- Solution: Check browser console (F12) for errors
- Make sure all environment variables are set correctly

### Database Issues

**Reports not appearing in Supabase**
- Solution:
  1. Check Supabase dashboard → Table Editor
  2. Verify RLS policies allow inserts
  3. Check backend logs for errors

## Quick Commands Reference

### Backend
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Run server
uvicorn app.main:app --reload

# Install new package
pip install package-name
pip freeze > requirements.txt
```

### Frontend
```bash
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Stopping the Servers

- **Backend**: Press `Ctrl+C` in the backend terminal
- **Frontend**: Press `Ctrl+C` in the frontend terminal

## Next Steps

Once everything is running:
1. ✅ Test the complete workflow
2. ✅ Check Supabase for stored reports
3. ✅ Verify webhook notifications
4. ✅ Customize authority mapping logic
5. ✅ Add your own styling/branding
6. ✅ Deploy to production 




