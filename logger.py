import logging
from logging import handlers

logger = logging.getLogger("SwachhWindows")
logger.setLevel(logging.DEBUG)


file_handler = logging.handlers.RotatingFileHandler(filename="Logs/application.log",
                                                    mode="a",
                                                    maxBytes=100000,
                                                    backupCount=10)
file_handler.setLevel(logging.DEBUG)
logger_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(logger_format)

logger.addHandler(file_handler)

