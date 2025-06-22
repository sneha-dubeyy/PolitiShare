from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PolitiShare API",
    description="API for political party prediction and social features",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "PolitiShare API is running"}

@app.get("/health")
async def health_check():
    import sys, pandas as pd, sklearn, numpy as np
    return {
        "status": "healthy",
        "python_version": sys.version,
        "pandas_version": pd.__version__,
        "sklearn_version": sklearn.__version__,
        "numpy_version": np.__version__,
        "environment": "ready"
    }