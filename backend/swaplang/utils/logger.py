import logging
from swaplang.config import setup_logger
from swaplang.config import settings

setup_logger(log_level=settings.LOG_LEVEL, log_path=settings.LOG_PATH)

logger = logging.getLogger("app")
