"""
Helper script to create .env file from template
"""
import os
from pathlib import Path

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    backend_dir = Path(__file__).parent
    env_file = backend_dir / ".env"
    template_file = backend_dir / "ENV_TEMPLATE.txt"
    
    if env_file.exists():
        print("✅ .env file already exists!")
        print(f"Location: {env_file}")
        return
    
    if not template_file.exists():
        print("❌ ENV_TEMPLATE.txt not found!")
        return
    
    # Read template
    with open(template_file, 'r') as f:
        template_content = f.read()
    
    # Create .env file
    with open(env_file, 'w') as f:
        f.write(template_content)
    
    print("✅ Created .env file from template!")
    print(f"Location: {env_file}")
    print("\n⚠️  IMPORTANT: Edit .env file and add your actual credentials:")
    print("   - SUPABASE_URL")
    print("   - SUPABASE_KEY")
    print("   - RELAY_APP_WEBHOOK_URL (optional)")
    print("   - OPENAI_API_KEY (optional)")

if __name__ == "__main__":
    create_env_file()


