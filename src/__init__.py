"""Main module for the pipeline IA application."""

import logging
from typing import Optional

from .config import get_settings
from .core.pipeline import Pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for the application."""
    settings = get_settings()
    logger.info("Starting Pipeline IA application")
    
    try:
        pipeline = Pipeline(settings)
        pipeline.run()
        logger.info("Pipeline IA application completed successfully")
    except Exception as e:
        logger.error(f"Application failed: {e}")
        raise


if __name__ == "__main__":
    main()
