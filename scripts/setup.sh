#!/bin/bash

# Setup script for the Pipeline IA project

set -e

echo "🚀 Setting up Pipeline IA development environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or later."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $python_version is installed, but Python $required_version or later is required."
    exit 1
fi

echo "✅ Python $python_version is installed"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install pip-tools
echo "🔧 Installing pip-tools..."
pip install pip-tools

# Compile requirements
echo "📋 Compiling requirements..."
pip-compile requirements.in
pip-compile requirements-dev.in

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
echo "🪝 Setting up pre-commit hooks..."
pre-commit install

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cat > .env << EOF
# Application settings
APP_NAME=Pipeline IA
DEBUG=true
VERSION=0.1.0

# Database settings
# DATABASE_URL=postgresql://user:password@localhost:5432/pipeline_ia

# API settings
API_HOST=0.0.0.0
API_PORT=8000

# Security settings
SECRET_KEY=your-secret-key-here-change-in-production

# External API settings
# EXTERNAL_API_KEY=your-api-key-here
# EXTERNAL_API_URL=https://api.example.com
EOF
    echo "✅ Created .env file with default settings"
fi

# Run initial tests
echo "🧪 Running initial tests..."
pytest tests/ -v

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the application, use:"
echo "  python -m src"
echo ""
echo "To run tests, use:"
echo "  pytest tests/"
echo ""
echo "To run code quality checks, use:"
echo "  ./scripts/lint.sh"
