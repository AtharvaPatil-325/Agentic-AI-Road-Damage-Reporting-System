# How to Run the Project - Backend & Frontend

## Prerequisites Checklist

Before running, make sure you have:
- ✅ Python 3.10+ installed
- ✅ Node.js 18+ installed
- ✅ Virtual environment created (if not, see below)
- ✅ Dependencies installed
- ✅ Environment variables configured

## Step-by-Step Instructions

### STEP 1: Set Up Backend Environment

**1.1 Navigate to backend directory:**
```powershell
cd "D:\Ai Project\backend"
```

**1.2 Create virtual environment (if not already created):**
```powershell
python -m venv venv
```

**1.3 Activate virtual environment:**
```powershell
venv\Scripts\activate
```
You should see `(venv)` in your terminal prompt.

**1.4 Install Python dependencies:**
```powershell
pip install -r requirements.txt
```

**1.5 Create .env file:**
```powershell
# Copy the template
Copy-Item ENV_TEMPLATE.txt .env

# Then edit .env file with your actual credentials:
# - SUPABASE_URL
# - SUPABASE_KEY
# - RELAY_APP_WEBHOOK_URL
# - OPENAI_API_KEY (optional)
```

**1.6 Create uploads directory:**
```powershell
mkdir uploads
```

---

### STEP 2: Start Backend Server

**2.1 Make sure you're in backend directory with venv activated:**
```powershell
cd "D:\Ai Project\backend"
venv\Scripts\activate
```

**2.2 Start the FastAPI server:**
```powershell
uvicorn app.main:app --reload
```

**✅ You should see:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Application startup complete.
```

**✅ Backend is now running on http://localhost:8000**

**Keep this terminal window open!**

---

### STEP 3: Set Up Frontend (New Terminal Window)

**3.1 Open a NEW terminal/PowerShell window**

**3.2 Navigate to frontend directory:**
```powershell
cd "D:\Ai Project\frontend"
```

**3.3 Install Node.js dependencies:**
```powershell
npm install
```

**3.4 Create .env file:**
```powershell
# Copy the template
Copy-Item ENV_TEMPLATE.txt .env

# Edit .env and ensure:
# VITE_API_URL=http://localhost:8000
```

---

### STEP 4: Start Frontend Server

**4.1 Make sure you're in frontend directory:**
```powershell
cd "D:\Ai Project\frontend"
```

**4.2 Start the development server:**
```powershell
npm run dev
```

**✅ You should see:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

**✅ Frontend is now running on http://localhost:3000**

---

### STEP 5: Access the Application

**Open your browser and go to:**
```
http://localhost:3000
```

You should see the **Road Damage Reporter** interface!

---

## Quick Reference: Running Both Servers

### Terminal 1 (Backend):
```powershell
cd "D:\Ai Project\backend"
venv\Scripts\activate
uvicorn app.main:app --reload
```

### Terminal 2 (Frontend):
```powershell
cd "D:\Ai Project\frontend"
npm run dev
```

---

## Troubleshooting

### Backend Issues

**Problem: "Module not found"**
- Solution: Make sure virtual environment is activated and dependencies are installed
  ```powershell
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

**Problem: "SUPABASE_URL and SUPABASE_KEY must be set"**
- Solution: Create `.env` file in backend directory with your Supabase credentials

**Problem: "Port 8000 already in use"**
- Solution: Use a different port:
  ```powershell
  uvicorn app.main:app --reload --port 8001
  ```
  Then update `frontend/.env`: `VITE_API_URL=http://localhost:8001`

**Problem: "Cannot connect to database"**
- Solution: 
  1. Verify Supabase credentials in `.env`
  2. Make sure you ran the SQL setup script in Supabase

### Frontend Issues

**Problem: "Cannot connect to API" or CORS errors**
- Solution:
  1. Verify backend is running on port 8000
  2. Check `VITE_API_URL` in `frontend/.env` matches backend URL
  3. Check browser console (F12) for specific errors

**Problem: "npm install fails"**
- Solution:
  ```powershell
  Remove-Item -Recurse -Force node_modules
  Remove-Item package-lock.json
  npm install
  ```

**Problem: "Blank page"**
- Solution: Check browser console (F12) for JavaScript errors

---

## Stopping the Servers

- **Backend**: Press `Ctrl+C` in Terminal 1
- **Frontend**: Press `Ctrl+C` in Terminal 2

---

## Testing the Application

1. **Open** http://localhost:3000 in your browser
2. **Upload** a road damage image (or any image for testing)
3. **Select** or enter a location
4. **Choose** damage type and severity
5. **Add** optional remarks
6. **Submit** the report
7. **Verify**:
   - You see a confirmation with report ID
   - Check Supabase dashboard → Table Editor → `reports` table
   - Check your relay.app webhook endpoint

---

## Development Workflow

1. **Start Backend** (Terminal 1) - Keep running
2. **Start Frontend** (Terminal 2) - Keep running
3. **Make changes** to code
4. **Backend** auto-reloads (thanks to `--reload` flag)
5. **Frontend** auto-reloads (Vite hot module replacement)
6. **Test** in browser

---

## Next Steps After Running

- ✅ Test the complete reporting workflow
- ✅ Check Supabase for stored reports
- ✅ Verify webhook notifications
- ✅ Customize the UI/UX
- ✅ Add your branding
- ✅ Deploy to production

