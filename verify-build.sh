#!/bin/bash

echo "🚀 Verifying builds before deployment..."

# Check if we're in the project root
if [ ! -d "frontend" ] || [ ! -d "backend" ]; then
    echo "❌ Error: Run this script from the project root directory"
    exit 1
fi

echo "📦 Checking frontend build..."
cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📥 Installing frontend dependencies..."
    npm install
fi

# Build frontend
echo "🔨 Building frontend..."
if npm run build; then
    echo "✅ Frontend build successful"
else
    echo "❌ Frontend build failed"
    exit 1
fi

cd ..

echo "🐍 Checking backend..."
cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📥 Creating virtual environment..."
    python -m venv venv
fi

# Activate venv and install dependencies
echo "📥 Installing backend dependencies..."
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Linux/Mac

pip install -r requirements.txt

# Test import
echo "🧪 Testing backend imports..."
if python -c "from app.main import app; print('✅ Backend imports successful')"; then
    echo "✅ Backend ready for deployment"
else
    echo "❌ Backend import failed"
    exit 1
fi

cd ..

echo ""
echo "🎉 All builds verified successfully!"
echo ""
echo "Ready for deployment:"
echo "- Frontend: Run 'vercel --prod' in frontend/ directory"
echo "- Backend: Deploy to Render with the render.yaml configuration"
echo ""
echo "Don't forget to set environment variables in your deployment platforms!"
