#!/usr/bin/env python3
"""
PolitiShare Environment Verification Script
Checks that all required packages are installed and functioning.
"""

import sys
import importlib
import subprocess

def check_package(package_name, import_name=None):
    """Check if a package is installed and importable."""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name}")
        return True
    except ImportError:
        print(f"❌ {package_name} - NOT INSTALLED")
        return False

def check_conda_env():
    """Check if we're in the correct conda environment."""
    try:
        result = subprocess.run(['conda', 'info', '--envs'], 
                              capture_output=True, text=True)
        if 'politishare' in result.stdout and '*' in result.stdout:
            env_line = [line for line in result.stdout.split('\n') 
                       if 'politishare' in line and '*' in line]
            if env_line:
                print("✅ Running in 'politishare' conda environment")
                return True
    except:
        pass
    
    print("❌ Not in 'politishare' conda environment")
    print("   Run: conda activate politishare")
    return False

def main():
    print("🚀 PolitiShare Environment Verification")
    print("=" * 40)
    
    # Check conda environment
    env_ok = check_conda_env()
    print()
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    if python_version >= (3, 11):
        print("✅ Python version is compatible")
    else:
        print("❌ Python version should be 3.11+")
    print()
    
    # Check core packages
    print("Core Packages:")
    core_packages = [
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('scikit-learn', 'sklearn'),
        ('matplotlib', 'matplotlib'),
        ('seaborn', 'seaborn'),
        ('xgboost', 'xgboost'),
        ('jupyter', 'jupyter'),
    ]
    
    core_ok = all(check_package(pkg, imp) for pkg, imp in core_packages)
    print()
    
    # Check backend packages
    print("Backend Packages:")
    backend_packages = [
        ('fastapi', 'fastapi'),
        ('uvicorn', 'uvicorn'),
        ('sqlalchemy', 'sqlalchemy'),
        ('alembic', 'alembic'),
        ('pydantic', 'pydantic'),
        ('jose', 'jose'),
        ('passlib', 'passlib'),
    ]
    
    backend_ok = all(check_package(pkg, imp) for pkg, imp in backend_packages)
    print()
    
    # Overall status
    if env_ok and core_ok and backend_ok:
        print("🎉 Environment setup is COMPLETE!")
        print("Ready to build PolitiShare!")
    else:
        print("⚠️  Some packages are missing. Please review the installation steps.")
    
    print("\nNext steps:")
    print("1. cd politishare/backend")
    print("2. uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()
