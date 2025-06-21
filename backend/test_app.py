from fastapi import FastAPI
import uvicorn

app = FastAPI(title="PolitiShare Test API")

@app.get("/")
async def root():
    return {"message": "PolitiShare environment is working!", "status": "success"}

@app.get("/health")
async def health():
    import sys
    import pandas as pd
    import sklearn
    import numpy as np
    
    return {
        "python_version": sys.version,
        "pandas_version": pd.__version__,
        "sklearn_version": sklearn.__version__,
        "numpy_version": np.__version__,
        "environment": "ready"
    }

if __name__ == "__main__":
    uvicorn.run("test_app:app", host="0.0.0.0", port=8000, reload=True)
