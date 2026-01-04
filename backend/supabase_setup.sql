-- Supabase database schema for Road Damage Reporting System
-- Run this SQL in your Supabase SQL editor to create the necessary tables

-- Create reports table
CREATE TABLE IF NOT EXISTS reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    location_lat DOUBLE PRECISION NOT NULL,
    location_lng DOUBLE PRECISION NOT NULL,
    location_address TEXT,
    damage_type VARCHAR(50) NOT NULL CHECK (damage_type IN ('pothole', 'crack', 'surface_damage', 'other')),
    severity VARCHAR(20) NOT NULL CHECK (severity IN ('low', 'medium', 'high')),
    remarks TEXT,
    image_url TEXT,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'submitted', 'in_progress', 'resolved', 'closed')),
    authority_name TEXT,
    authority_contact TEXT,
    webhook_sent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index on location for geospatial queries
CREATE INDEX IF NOT EXISTS idx_reports_location ON reports USING GIST (
    point(location_lng, location_lat)
);

-- Create index on status for filtering
CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status);

-- Create index on created_at for sorting
CREATE INDEX IF NOT EXISTS idx_reports_created_at ON reports(created_at DESC);

-- Enable Row Level Security (RLS)
ALTER TABLE reports ENABLE ROW LEVEL SECURITY;

-- Create policy to allow all operations (adjust based on your security requirements)
CREATE POLICY "Allow all operations" ON reports
    FOR ALL
    USING (true)
    WITH CHECK (true);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create trigger to automatically update updated_at
CREATE TRIGGER update_reports_updated_at BEFORE UPDATE ON reports
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Optional: Create a view for report summaries
CREATE OR REPLACE VIEW report_summaries AS
SELECT 
    id,
    damage_type,
    severity,
    status,
    location_address,
    created_at,
    CASE 
        WHEN severity = 'high' THEN 'urgent'
        WHEN severity = 'medium' THEN 'high'
        ELSE 'normal'
    END as priority
FROM reports;


