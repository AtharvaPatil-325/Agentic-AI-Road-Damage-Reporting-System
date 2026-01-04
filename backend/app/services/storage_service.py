"""
Service for handling image storage
"""
import os
import uuid
from pathlib import Path
from typing import Optional
from fastapi import UploadFile
import aiofiles

class StorageService:
    """Service for storing uploaded images"""
    
    def __init__(self):
        self.upload_dir = Path("uploads")
        self.upload_dir.mkdir(exist_ok=True)
        self.base_url = os.getenv("BASE_URL", "http://localhost:8000")
    
    async def save_image(self, file: UploadFile) -> Optional[str]:
        """
        Save uploaded image file and return URL
        
        Args:
            file: Uploaded file object
            
        Returns:
            URL to the saved image or None if failed
        """
        try:
            # Generate unique filename
            file_ext = Path(file.filename).suffix
            filename = f"{uuid.uuid4()}{file_ext}"
            filepath = self.upload_dir / filename
            
            # Save file
            async with aiofiles.open(filepath, 'wb') as f:
                content = await file.read()
                await f.write(content)
            
            # Return URL (in production, this would be a CDN URL)
            return f"{self.base_url}/uploads/{filename}"
        except Exception as e:
            print(f"Error saving image: {e}")
            return None
    
    def get_image_path(self, filename: str) -> Path:
        """Get the file path for a stored image"""
        return self.upload_dir / filename

# Singleton instance
storage_service = StorageService()


