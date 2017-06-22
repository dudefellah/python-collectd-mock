import logging

import sys

def debug(output):
    logger = logging.getLogger(__name__)
    logger.debug(output)

def info(output):
    logger = logging.getLogger(__name__)
    logger.info(output)

def notice(output):
    logger = logging.getLogger(__name__)
    # No notice in logging?
    logger.info(output)

def warning(output):
    logger = logging.getLogger(__name__)
    logger.warning(output)

def error(output):
    logger = logging.getLogger(__name__)
    logger.error(output)
