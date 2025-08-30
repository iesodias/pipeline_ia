#!/bin/bash

# Lint script for the Pipeline IA project

set -e

echo "🔍 Running code quality checks..."

# Format check with Black
echo "⚫ Checking code formatting with Black..."
black --check --diff src/ tests/

# Import sorting check
echo "📋 Checking import sorting with isort..."
isort --check-only --diff src/ tests/

# Lint with flake8
echo "🔎 Linting with flake8..."
flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503

# Type check with mypy
echo "🔍 Type checking with mypy..."
mypy src/ --ignore-missing-imports

# Security check with bandit
echo "🔒 Security check with bandit..."
bandit -r src/ --skip B101

# Check for known security vulnerabilities
echo "🛡️ Checking dependencies for vulnerabilities..."
safety check

echo "✅ All code quality checks passed!"
