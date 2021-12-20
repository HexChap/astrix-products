import os
import sys

from loguru import logger

from app.core.config import config

s = os.sep
LOG_FILE = f"logs{s}log.log"

logger.remove(0)  # removes standart handler
logger.add(
    LOG_FILE,
    level=config.logging.level,
    rotation=config.logging.rotation,
    compression=config.logging.compression
)
logger.add(sys.stderr, level=config.logging.level)
