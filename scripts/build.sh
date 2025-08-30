#!/bin/bash

# Build script for the Pipeline IA project

set -e

echo "🔧 Building Pipeline IA..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install build dependencies
echo "📋 Installing build dependencies..."
pip install pip-tools

# Compile requirements
echo "🔄 Compiling requirements..."
pip-compile requirements.in
pip-compile requirements-dev.in

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
pre-commit install

# Run tests
echo "🧪 Running tests..."
pytest tests/ --cov=src/ --cov-report=html --cov-report=term

# Run linting
echo "🔍 Running code quality checks..."
black --check src/ tests/
isort --check-only src/ tests/
flake8 src/ tests/
mypy src/

echo "✅ Build completed successfully!"
