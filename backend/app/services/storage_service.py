"""
Service for handling image storage using Supabase Storage
"""
import os
import uuid
from pathlib import Path
from typing import Optional
from fastapi import UploadFile
from supabase import create_client, Client

class StorageService:
    """Service for storing uploaded images in Supabase Storage"""

    def __init__(self):
        self.supabase_url = None
        self.supabase_key = None
        self.supabase: Optional[Client] = None
        self.bucket_name = "road-damage-images"  # Supabase storage bucket name

    def _initialize_client(self):
        """Lazy initialization of Supabase client"""
        if self.supabase is None:
            self.supabase_url = os.getenv("SUPABASE_URL")
            self.supabase_key = os.getenv("SUPABASE_KEY")

            if not self.supabase_url or not self.supabase_key:
                raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set")

            self.supabase = create_client(self.supabase_url, self.supabase_key)

            # Create bucket if it doesn't exist
            self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        """Ensure the storage bucket exists"""
        try:
            # Try to get bucket info
            buckets = self.supabase.storage.list_buckets()
            bucket_names = [bucket['name'] for bucket in buckets]

            if self.bucket_name not in bucket_names:
                print(f"Bucket '{self.bucket_name}' does not exist. Please create it manually in Supabase Dashboard:")
                print("1. Go to Storage in your Supabase project")
                print("2. Create bucket: 'road-damage-images'")
                print("3. Set it to Public")
                print("4. Configure CORS and file size limits as needed")
            else:
                print(f"Bucket '{self.bucket_name}' exists")
        except Exception as e:
            print(f"Warning: Could not verify bucket existence: {e}")
            print("Please ensure the bucket 'road-damage-images' exists and is public in your Supabase project")

    async def save_image(self, file: UploadFile) -> Optional[str]:
        """
        Save uploaded image to Supabase Storage and return public URL

        Args:
            file: Uploaded file object

        Returns:
            Public URL to the saved image or None if failed
        """
        try:
            # Initialize client if needed
            self._initialize_client()

            # Read file content
            content = await file.read()

            # Generate unique filename
            file_ext = Path(file.filename).suffix.lower()
            if not file_ext:
                file_ext = '.jpg'  # Default extension

            filename = f"{uuid.uuid4()}{file_ext}"
            file_path = f"uploads/{filename}"

            # Upload to Supabase Storage
            response = self.supabase.storage.from_(self.bucket_name).upload(
                file_path,
                content,
                file_options={
                    "content-type": file.content_type or "image/jpeg",
                    "cache-control": "3600"
                }
            )

            if response.status_code == 200:
                # Get public URL
                public_url = self.supabase.storage.from_(self.bucket_name).get_public_url(file_path)
                return public_url
            elif response.status_code == 400 and "bucket" in str(response.json()).lower():
                print(f"Bucket '{self.bucket_name}' not found. Please create it in Supabase Dashboard -> Storage")
                return None
            else:
                print(f"Supabase upload failed: {response.status_code}")
                try:
                    error_details = response.json()
                    print(f"Error details: {error_details}")
                except:
                    print(f"Response: {response.text}")
                return None

        except Exception as e:
            print(f"Error saving image to Supabase: {e}")
            return None

    async def delete_image(self, image_url: str) -> bool:
        """
        Delete an image from Supabase Storage

        Args:
            image_url: The public URL of the image to delete

        Returns:
            True if successful, False otherwise
        """
        try:
            # Initialize client if needed
            self._initialize_client()

            # Extract file path from URL
            # URL format: https://[project-id].supabase.co/storage/v1/object/public/[bucket]/[path]
            url_parts = image_url.split('/storage/v1/object/public/')
            if len(url_parts) == 2:
                path_part = url_parts[1]
                # Remove bucket name from path
                file_path = path_part.replace(f"{self.bucket_name}/", "", 1)

                response = self.supabase.storage.from_(self.bucket_name).remove([file_path])
                return response.status_code == 200
            return False
        except Exception as e:
            print(f"Error deleting image: {e}")
            return False

# Singleton instance
storage_service = StorageService()


