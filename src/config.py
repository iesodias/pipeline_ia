"""Configuration module for the pipeline IA application."""

import os
from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings."""
    
    # Application settings
    app_name: str = Field(default="Pipeline IA", env="APP_NAME")
    debug: bool = Field(default=False, env="DEBUG")
    version: str = Field(default="0.1.0", env="VERSION")
    
    # Database settings
    database_url: Optional[str] = Field(default=None, env="DATABASE_URL")
    
    # API settings
    api_host: str = Field(default="0.0.0.0", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")
    
    # Security settings
    secret_key: str = Field(default="your-secret-key-here", env="SECRET_KEY")
    
    # External API settings
    external_api_key: Optional[str] = Field(default=None, env="EXTERNAL_API_KEY")
    external_api_url: Optional[str] = Field(default=None, env="EXTERNAL_API_URL")
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Get application settings."""
    return Settings()
