# Webhook Configuration Guide

## Overview

The webhook notification to relay.app is **optional**. Reports will be saved successfully even if the webhook is not configured or fails.

## Current Behavior

✅ **Reports are ALWAYS saved to Supabase** - even if webhook fails
✅ **Webhook failures do NOT block report submission**
✅ **System works without webhook URL configured**

## Configuration

### Option 1: Configure Webhook (Recommended)

1. **Get your relay.app webhook URL**
   - Set up your webhook endpoint in relay.app
   - Copy the webhook URL

2. **Add to backend/.env:**
   ```env
   RELAY_APP_WEBHOOK_URL=https://hook.relay.app/api/v1/playbook/cmjzjlqwd00f60pkq0v7peeha/trigger/Cxg6-JhnsGxOXIyySUyXYw
   ```

3. **Restart backend server:**
   ```powershell
   # Stop backend (Ctrl+C)
   # Then restart:
   cd "D:\Ai Project\backend"
   venv\Scripts\activate
   uvicorn app.main:app --reload
   ```

### Option 2: Run Without Webhook (For Testing)

If you don't have a webhook URL yet, you can:

1. **Leave it unset in .env** (or comment it out):
   ```env
   # RELAY_APP_WEBHOOK_URL=https://your-relay-app-endpoint.com/webhook
   ```

2. **Reports will still be saved** to Supabase
3. **You'll see a warning** in backend logs: "RELAY_APP_WEBHOOK_URL not configured"
4. **Frontend will show**: "Note: Webhook notification was not sent"

## Webhook Payload Format

When webhook is configured, it sends this JSON structure:

```json
{
  "event_type": "road_damage_report",
  "report_id": "uuid-here",
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
    "image_url": "http://localhost:8000/uploads/image.jpg"
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

## Troubleshooting

### Issue: "Webhook notification failed"

**Possible causes:**
1. Webhook URL is incorrect
2. Webhook endpoint is not accessible
3. Network/firewall blocking the request
4. Webhook endpoint returning error

**Solution:**
- Check backend terminal for detailed error message
- Verify webhook URL is correct in `.env`
- Test webhook URL manually (use Postman or curl)
- Check relay.app dashboard for webhook logs

### Issue: "RELAY_APP_WEBHOOK_URL not configured"

**This is normal if:**
- You haven't set up a webhook yet
- You're testing without webhook
- The environment variable is missing

**Solution:**
- Reports still work! They're saved to Supabase
- Add webhook URL to `.env` when ready
- Restart backend after adding URL

### Issue: Report submission fails entirely

**This should NOT happen** - webhook failures are non-blocking.

**If it does happen, check:**
1. Supabase configuration (SUPABASE_URL, SUPABASE_KEY)
2. Database connection
3. Backend logs for actual error

## Testing

### Test Without Webhook:
1. Don't set `RELAY_APP_WEBHOOK_URL` in `.env`
2. Submit a report
3. ✅ Report should save successfully
4. ⚠️ You'll see warning in backend logs
5. ℹ️ Frontend shows webhook was not sent

### Test With Webhook:
1. Set `RELAY_APP_WEBHOOK_URL` in `.env`
2. Submit a report
3. ✅ Report saves to Supabase
4. ✅ Webhook notification sent
5. ✅ Check relay.app dashboard for received payload

## Summary

- **Webhook is optional** - system works without it
- **Reports always save** to Supabase regardless of webhook status
- **Webhook failures are logged** but don't block submission
- **Configure webhook** when ready to notify authorities automatically

