"""Test configuration."""

import pytest
from src.config import Settings, get_settings


def test_default_settings():
    """Test default settings."""
    settings = Settings()
    
    assert settings.app_name == "Pipeline IA"
    assert settings.debug is False
    assert settings.version == "0.1.0"
    assert settings.api_host == "0.0.0.0"
    assert settings.api_port == 8000


def test_get_settings():
    """Test get_settings function."""
    settings = get_settings()
    
    assert isinstance(settings, Settings)
    assert settings.app_name == "Pipeline IA"


def test_settings_with_env_vars(monkeypatch):
    """Test settings with environment variables."""
    monkeypatch.setenv("APP_NAME", "Test App")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("API_PORT", "9000")
    
    settings = Settings()
    
    assert settings.app_name == "Test App"
    assert settings.debug is True
    assert settings.api_port == 9000
