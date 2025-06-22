#!/usr/bin/env python3
"""
Validate PolitiShare configuration and environment setup
"""

def validate_environment():
    try:
        from app.core.config import settings
        print("🚀 PolitiShare Configuration Validation")
        print("=" * 40)
        
        # Check basic settings
        print(f"Project Name: {settings.PROJECT_NAME}")
        print(f"Environment: {settings.ENVIRONMENT}")
        print(f"Debug Mode: {settings.DEBUG}")
        print(f"API Prefix: {settings.API_V1_STR}")
        
        # Check security settings
        print(f"\n🔐 Security Configuration:")
        if settings.SECRET_KEY == "politishare-development-key-change-in-production":
            print("⚠️  Using default SECRET_KEY (OK for development)")
        else:
            print("✅ Custom SECRET_KEY configured")
        
        print(f"Token Expiry: {settings.ACCESS_TOKEN_EXPIRE_MINUTES} minutes")
        print(f"Algorithm: {settings.ALGORITHM}")
        
        # Check database
        print(f"\n🗄️  Database Configuration:")
        print(f"Database URL: {settings.DATABASE_URL}")
        
        # Check CORS
        print(f"\n🌐 CORS Origins:")
        for origin in settings.BACKEND_CORS_ORIGINS:
            print(f"  - {origin}")
        
        # Check ML settings
        print(f"\n🤖 ML Configuration:")
        print(f"Model Path: {settings.MODEL_PATH}")
        print(f"Model Version: {settings.MODEL_VERSION}")
        print(f"Batch Size: {settings.PREDICTION_BATCH_SIZE}")
        
        print(f"\n✅ Configuration loaded successfully!")
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    validate_environment()
