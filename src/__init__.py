import logging
import os
import atexit
from . import config
from .logger import timelog
from .plotter import timeplot

dirs = [config.LOG_DIR, config.PLOT_DIR]
for dir in dirs:
    if not os.path.exists(dir):
        os.makedirs(dir)


logging.addLevelName(
    level=config.LOGGING_LEVEL_VALUE,
    levelName=config.LOGGING_LEVEL_NAME
)


logging.basicConfig(
    filename=config.LOG_FILEPATH,
    level=config.LOGGING_LEVEL_VALUE,
    format=config.LOGGING_FORMAT,
    datefmt=config.LOGGING_DATETIME
)

atexit.register(timeplot)