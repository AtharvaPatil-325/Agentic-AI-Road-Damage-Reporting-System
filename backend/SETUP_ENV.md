# Setting Up Environment Variables

## Quick Setup

### Step 1: Create .env File

**Option A: Using the script (Recommended)**
```powershell
cd "D:\Ai Project\backend"
python setup_env.py
```

**Option B: Manual creation**
1. Navigate to `backend` folder
2. Copy `ENV_TEMPLATE.txt` and rename it to `.env`
3. Open `.env` in a text editor

### Step 2: Get Supabase Credentials

1. Go to https://supabase.com
2. Sign in or create an account
3. Create a new project (or use existing)
4. Go to **Settings** → **API**
5. Copy:
   - **Project URL** → This is your `SUPABASE_URL`
   - **anon public** key → This is your `SUPABASE_KEY`

### Step 3: Edit .env File

Open `backend/.env` and replace the placeholder values:

```env
# Supabase Configuration (REQUIRED)
SUPABASE_URL=https://your-actual-project-id.supabase.co
SUPABASE_KEY=your-actual-anon-key-here

# Webhook Configuration (OPTIONAL - can leave as is for now)
RELAY_APP_WEBHOOK_URL=https://your-relay-app-endpoint.com/webhook

# OpenAI API Key (OPTIONAL - can leave as is for now)
OPENAI_API_KEY=sk-your-openai-api-key-here

# Environment
ENVIRONMENT=development

# Base URL
BASE_URL=http://localhost:8000
```

### Step 4: Set Up Supabase Database

1. Go to your Supabase project dashboard
2. Click **SQL Editor** in the left sidebar
3. Open `backend/supabase_setup.sql` file
4. Copy the entire SQL script
5. Paste it into the SQL Editor
6. Click **Run** to execute

### Step 5: Restart Backend

After creating/editing `.env` file:

```powershell
# Stop backend (Ctrl+C)
# Then restart:
cd "D:\Ai Project\backend"
venv\Scripts\activate
uvicorn app.main:app --reload
```

## Verification

To verify your .env file is set up correctly:

1. Check that `.env` file exists in `backend/` folder
2. Check that it contains your actual Supabase URL and Key
3. Restart backend server
4. Try submitting a report again

## Troubleshooting

### Error: "SUPABASE_URL and SUPABASE_KEY must be set"

**Causes:**
- `.env` file doesn't exist
- `.env` file has placeholder values (not replaced)
- Backend wasn't restarted after creating .env
- `.env` file is in wrong location (should be in `backend/` folder)

**Solution:**
1. Verify `.env` file exists: `backend/.env`
2. Open it and check values are actual credentials (not placeholders)
3. Make sure there are no extra spaces or quotes around values
4. Restart backend server

### Error: "Failed to create report in database"

**Causes:**
- Supabase credentials are incorrect
- Database table doesn't exist (didn't run SQL setup)
- Network/firewall blocking connection

**Solution:**
1. Verify Supabase URL and Key are correct
2. Run the SQL setup script in Supabase SQL Editor
3. Check Supabase project is active and accessible

## Example .env File

```env
SUPABASE_URL=https://abcdefghijklmnop.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiY2RlZmdoaWprbG1ub3AiLCJyb2xlIjoiYW5vbiIsImlhdCI6MTY0MDAwMDAwMCwiZXhwIjoxOTU1NTY3MjAwfQ.example
RELAY_APP_WEBHOOK_URL=
OPENAI_API_KEY=
ENVIRONMENT=development
BASE_URL=http://localhost:8000
```

**Note:** You can leave `RELAY_APP_WEBHOOK_URL` and `OPENAI_API_KEY` empty if you don't have them yet.


