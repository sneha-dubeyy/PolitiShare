#!/bin/bash
echo "🚀 Activating PolitiShare development environment..."
conda activate politishare
echo "✅ Environment activated!"
echo "Current environment: $(conda info --envs | grep '*' | awk '{print $1}')"
echo ""
echo "Available commands:"
echo "  cd backend && uvicorn app.main:app --reload  # Start backend"
echo "  cd frontend && npm run dev                   # Start frontend"
echo "  jupyter lab                                  # Start Jupyter"
echo ""
