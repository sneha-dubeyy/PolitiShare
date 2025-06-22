#!/bin/bash
# Railway startup script for PolitiShare backend

# Set default port if not provided
export PORT=${PORT:-8000}

echo "Starting PolitiShare backend on port $PORT"

# Run database migrations first
echo "Running database migrations..."
alembic upgrade head

# Start the server
echo "Starting uvicorn server..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1
