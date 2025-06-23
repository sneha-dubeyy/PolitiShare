from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, users, surveys, predictions, social

# Create FastAPI app with configuration
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for political party prediction and social features",
    version="1.0.0",
    debug=settings.DEBUG
)

# Set up CORS with configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(surveys.router, prefix="/api/surveys", tags=["Surveys"])
app.include_router(predictions.router, prefix="/api/predictions", tags=["Predictions"])
app.include_router(social.router, prefix="/api/social", tags=["Social"])

@app.get("/")
async def root():
    return {
        "message": f"{settings.PROJECT_NAME} API is running",
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    try:
        import sys
        
        # Try to import packages safely
        try:
            import pandas as pd
            pandas_version = pd.__version__
        except ImportError:
            pandas_version = "Not installed"
        
        try:
            import sklearn
            sklearn_version = sklearn.__version__
        except ImportError:
            sklearn_version = "Not installed"
        
        try:
            import numpy as np
            numpy_version = np.__version__
        except ImportError:
            numpy_version = "Not installed"
        
        return {
            "status": "healthy",
            "project": settings.PROJECT_NAME,
            "environment": settings.ENVIRONMENT,
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "pandas_version": pandas_version,
            "sklearn_version": sklearn_version,
            "numpy_version": numpy_version,
            "debug_mode": settings.DEBUG
        }
    except Exception as e:
        return {
            "status": "error",
            "project": settings.PROJECT_NAME,
            "environment": settings.ENVIRONMENT,
            "error": str(e)
        }

@app.get("/config")
async def get_config_info():
    """Get non-sensitive configuration information"""
    return {
        "project_name": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT,
        "api_prefix": settings.API_V1_STR,
        "cors_origins": settings.BACKEND_CORS_ORIGINS,
        "model_version": settings.MODEL_VERSION
    }
