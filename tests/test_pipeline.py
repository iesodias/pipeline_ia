"""Test pipeline."""

import pytest
from unittest.mock import Mock, patch

from src.config import Settings
from src.core.pipeline import Pipeline


@pytest.fixture
def settings():
    """Test settings fixture."""
    return Settings(
        app_name="Test Pipeline IA",
        debug=True
    )


@pytest.fixture
def pipeline(settings):
    """Test pipeline fixture."""
    return Pipeline(settings)


def test_pipeline_initialization(pipeline, settings):
    """Test pipeline initialization."""
    assert pipeline.settings == settings
    assert pipeline.logger is not None


def test_pipeline_run_success(pipeline):
    """Test successful pipeline run."""
    with patch.object(pipeline, '_load_data', return_value={"test": "data"}), \
         patch.object(pipeline, '_process_data', return_value={"processed": "data"}), \
         patch.object(pipeline, '_run_inference', return_value={"results": "predictions"}), \
         patch.object(pipeline, '_save_results'):
        
        result = pipeline.run()
        
        assert result["status"] == "success"
        assert "results" in result


def test_pipeline_run_failure(pipeline):
    """Test pipeline run with failure."""
    with patch.object(pipeline, '_load_data', side_effect=Exception("Test error")):
        
        with pytest.raises(Exception, match="Test error"):
            pipeline.run()


def test_load_data(pipeline):
    """Test data loading."""
    result = pipeline._load_data()
    
    assert isinstance(result, dict)
    assert "data" in result


def test_process_data(pipeline):
    """Test data processing."""
    input_data = {"test": "data"}
    result = pipeline._process_data(input_data)
    
    assert isinstance(result, dict)
    assert "processed_data" in result


def test_run_inference(pipeline):
    """Test AI inference."""
    input_data = {"processed": "data"}
    result = pipeline._run_inference(input_data)
    
    assert isinstance(result, dict)
    assert "inference_results" in result
