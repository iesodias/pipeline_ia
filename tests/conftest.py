"""Test fixtures and configurations."""

import pytest
import tempfile
import os
from typing import Generator

from src.config import Settings


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir


@pytest.fixture
def test_settings() -> Settings:
    """Create test settings."""
    return Settings(
        app_name="Test Pipeline IA",
        debug=True,
        database_url="sqlite:///:memory:",
        secret_key="test-secret-key"
    )


@pytest.fixture(autouse=True)
def clean_environment():
    """Clean environment variables before each test."""
    env_vars_to_clean = [
        "APP_NAME",
        "DEBUG", 
        "DATABASE_URL",
        "SECRET_KEY",
        "EXTERNAL_API_KEY"
    ]
    
    original_values = {}
    for var in env_vars_to_clean:
        original_values[var] = os.environ.get(var)
        if var in os.environ:
            del os.environ[var]
    
    yield
    
    # Restore original values
    for var, value in original_values.items():
        if value is not None:
            os.environ[var] = value
