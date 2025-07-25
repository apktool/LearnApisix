import logging
import os
import sys

from canary.config import base_path
from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())


def config_logging():
    log_path: str = os.path.join(base_path, "logs")
    log_console_level: str = "INFO"
    log_file_level: str = "DEBUG"

    os.makedirs(name=log_path, exist_ok=True)

    logger.remove()
    logger.add(
        sys.stdout,
        level=log_console_level,
    )

    logger.add(
        os.path.join(log_path, "canary-{time:YYYY-MM-DD}.log"),
        level=log_file_level,
        enqueue=True,
    )


logging.basicConfig(handlers=[InterceptHandler()], level=logging.NOTSET, force=True)
config_logging()
