"""logging for this dashboard"""

import logging
import os

def _get_filename() -> str:
    """ get filename for current file"""

    filename = os.path.basename(p=__file__)
    return filename

def init_logging() -> logging.Logger:
    """logging function"""

    file_log_formatter = logging.Formatter(fmt="[%(asctime)s]: [%(name)s]: [%(filename)s]: [%(levelname)s]: [%(message)s]")
    stream_log_formatter = logging.Formatter(fmt="[%(asctime)s]: [%(funcName)s]: [%(lineno)s]: [%(levelname)s]: [%(message)s]")
    logger = logging.getLogger(name=_get_filename().replace('.py', ''))
    file_handler = logging.FileHandler(filename=_get_filename().replace('.py', '.log'))
    stream_handler = logging.StreamHandler()

    logger.addHandler(hdlr=file_handler)
    logger.addHandler(hdlr=stream_handler)

    file_handler.setFormatter(fmt=file_log_formatter)
    stream_handler.setFormatter(fmt=stream_log_formatter)

    file_handler.setLevel(level=logging.INFO)
    stream_handler.setLevel(level=logging.INFO)
    logger.setLevel(logging.INFO)
    return logger
