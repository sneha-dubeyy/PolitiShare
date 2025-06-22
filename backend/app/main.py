from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users, surveys, predictions, social

app = FastAPI(
    title="PolitiShare API",
    description="API for political party prediction and social features",
    version="1.0.0"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
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
    return {"message": "PolitiShare API is running"}

@app.get("/health")
async def health_check():
    import sys
    import pandas as pd
    import sklearn
    import numpy as np
    
    return {
        "status": "healthy",
        "python_version": sys.version,
        "pandas_version": pd.__version__,
        "sklearn_version": sklearn.__version__,
        "numpy_version": np.__version__,
        "environment": "ready"
    }
