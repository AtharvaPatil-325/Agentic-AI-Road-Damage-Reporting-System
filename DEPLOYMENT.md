# 🚀 Deployment Guide

This guide covers deploying the Road Damage Reporting System to production.

## 📋 Prerequisites

- Supabase account and project
- Vercel account (frontend)
- Render account (backend)
- Domain name (optional)

## 🗂️ Project Structure

```
road-damage-reporting-system/
├── frontend/          # React + Vite app
├── backend/           # FastAPI application
└── deployment files
```

## 🌐 Frontend Deployment (Vercel)

### 1. Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy frontend
cd frontend
vercel --prod
```

### 2. Configure Environment Variables

In Vercel dashboard, set:

```
VITE_API_URL=https://your-backend-url.onrender.com
```

### 3. Custom Domain (Optional)

Add your custom domain in Vercel settings.

## ⚙️ Backend Deployment (Render)

### 1. Connect Repository

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Select the `backend/` directory as root

### 2. Configure Service

- **Name**: `road-damage-api`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### 3. Set Environment Variables

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
RELAY_APP_WEBHOOK_URL=https://hook.relay.app/api/v1/playbook/your-playbook/trigger/your-trigger
OPENAI_API_KEY=your-openai-key (optional)
```

### 4. Deploy

Click "Create Web Service" to deploy.

## 🗄️ Database Setup (Supabase)

### 1. Create Storage Bucket

1. Go to Supabase Dashboard → Storage
2. Create bucket: `road-damage-images`
3. Set as **Public** bucket
4. Configure file size limit: `5MB`
5. Allowed MIME types: `image/jpeg`, `image/png`, `image/gif`, `image/webp`

### 2. Run Database Schema

Execute `backend/supabase_setup.sql` in Supabase SQL Editor.

## 🔗 Connecting Frontend to Backend

Update the frontend's `VITE_API_URL` environment variable with your Render backend URL:

```bash
# Example
VITE_API_URL=https://road-damage-api.onrender.com
```

## ✅ Deployment Checklist

### Frontend
- [ ] Vercel account created
- [ ] Repository connected
- [ ] `VITE_API_URL` set to backend URL
- [ ] Custom domain configured (optional)
- [ ] Build successful

### Backend
- [ ] Render account created
- [ ] Repository connected
- [ ] Environment variables configured
- [ ] Build successful
- [ ] API accessible

### Database
- [ ] Supabase project created
- [ ] Storage bucket `road-damage-images` created and public
- [ ] Database schema executed
- [ ] Tables and policies configured

### Integration
- [ ] Frontend can communicate with backend
- [ ] Backend can access Supabase
- [ ] Webhook URLs configured
- [ ] Email notifications working

## 🔍 Testing Deployment

### API Health Check
```bash
curl https://your-backend-url.onrender.com/health
# Should return: {"status":"healthy"}
```

### Frontend Access
```bash
# Frontend should load and be able to submit reports
open https://your-frontend-url.vercel.app
```

### Database Connection
```bash
# Test webhook functionality
curl -X POST https://your-backend-url.onrender.com/api/reports/submit \
  -F "location={\"lat\":40.7128,\"lng\":-74.0060,\"address\":\"Test Location\"}" \
  -F "damage_type=pothole" \
  -F "severity=medium" \
  -F "remarks=Test report"
```

## 🆘 Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure backend allows frontend domain
2. **Environment Variables**: Double-check all required vars are set
3. **Storage Bucket**: Ensure bucket is public and accessible
4. **Webhook URLs**: Verify relay.app URLs are correct

### Logs

- **Frontend**: Vercel dashboard → Functions → Logs
- **Backend**: Render dashboard → Service → Logs
- **Database**: Supabase dashboard → Logs

## 📊 Monitoring

- Set up uptime monitoring for both services
- Monitor database usage in Supabase
- Check webhook delivery in relay.app

## 🎉 Post-Deployment

1. Test all features end-to-end
2. Share the frontend URL with users
3. Monitor for any issues
4. Set up backups if needed

---

**Deployment URLs:**
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-api.onrender.com`
- API Docs: `https://your-api.onrender.com/docs`
