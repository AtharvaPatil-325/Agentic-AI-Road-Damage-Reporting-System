# Frontend - Road Damage Reporting UI

React + Vite frontend with Tailwind CSS for the road damage reporting system.

## Setup

1. **Install dependencies:**
```bash
npm install
```

2. **Configure environment:**
Copy `.env.example` to `.env` and set:
- `VITE_API_URL`: Backend API URL (default: http://localhost:8000)

3. **Run development server:**
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Build for Production

```bash
npm run build
```

## Features

- **Chat Interface**: AI-powered conversational reporting experience
- **Image Upload**: Drag-and-drop or click to upload road damage photos
- **Location Picker**: GPS-based or manual location selection
- **Damage Type Selection**: Visual selection of damage types
- **Severity Assessment**: Three-level severity selection
- **Real-time Validation**: Immediate feedback on input quality
- **Confirmation Screen**: Reference ID and submission confirmation

## Components

- `ChatInterface`: Main chat container and workflow orchestration
- `MessageBubble`: Individual chat message display
- `ImageUpload`: Image upload with preview
- `LocationPicker`: Location selection (GPS/manual)
- `DamageTypeSelector`: Damage type selection UI
- `SeveritySelector`: Severity level selection
- `Header`: Application header with branding

## Styling

The app uses Tailwind CSS with a custom civic-tech theme:
- Primary colors: Blue palette for actions
- Civic colors: Neutral grays for backgrounds
- Responsive design: Mobile-friendly layout


