#!/usr/bin/env python3
"""
Test Supabase Storage configuration
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app.services.storage_service import storage_service

def test_storage():
    """Test Supabase storage setup"""
    try:
        storage_service._initialize_client()
        print('SUCCESS: Supabase client initialized successfully')

        # List buckets
        buckets = storage_service.supabase.storage.list_buckets()
        print(f'Found {len(buckets)} buckets:')
        for bucket in buckets:
            name = bucket.get('name', 'unknown')
            public = bucket.get('public', False)
            print(f'   - {name} (public: {public})')

        # Test our bucket
        bucket_name = storage_service.bucket_name
        print(f'Our bucket: {bucket_name}')

        # Check if our bucket exists and is public
        bucket_exists = any(b.get('name') == bucket_name for b in buckets)
        if bucket_exists:
            print(f'SUCCESS: Bucket "{bucket_name}" exists')
        else:
            print(f'ERROR: Bucket "{bucket_name}" does not exist - you may need to create it manually')

        # Test URL generation even if bucket doesn't exist
        test_url = storage_service.supabase.storage.from_(bucket_name).get_public_url('test.jpg')
        print(f'Sample URL format: {test_url}')

        # Test URL structure
        if 'storage/v1/object/public' in test_url:
            print('SUCCESS: URL format looks correct')
        else:
            print('WARNING: URL format may be incorrect')

    except Exception as e:
        print(f'❌ Error: {e}')
        import traceback
        traceback.print_exc()

def test_image_accessibility():
    """Test if uploaded images are accessible"""
    import httpx

    try:
        storage_service._initialize_client()
        bucket_name = storage_service.bucket_name

        # Test URL generation
        test_url = storage_service.supabase.storage.from_(bucket_name).get_public_url('test.jpg')
        print(f"\nTesting image accessibility...")
        print(f"Test URL: {test_url}")

        # Try to access the URL (will fail for non-existent file, but should not give auth errors)
        try:
            response = httpx.head(test_url, timeout=10)
            print(f"HTTP Status: {response.status_code}")
            if response.status_code == 404:
                print("SUCCESS: URL is accessible (404 is expected for non-existent file)")
            elif response.status_code == 200:
                print("SUCCESS: URL is accessible")
            else:
                print(f"WARNING: Unexpected status code: {response.status_code}")
        except Exception as e:
            print(f"ERROR accessing URL: {e}")

    except Exception as e:
        print(f"Error testing accessibility: {e}")

if __name__ == "__main__":
    test_storage()
    test_image_accessibility()
