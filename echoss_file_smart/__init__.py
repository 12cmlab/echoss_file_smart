from . import file_smart

import logging
import echoss_fileformat

logger = logging.getLogger(__name__)

# if the logger have not handlers, set a logger handler to console stdout logging
if logger.handlers:
    LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s - %(message)s"
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)