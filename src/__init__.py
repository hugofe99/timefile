import logging
import os
import shutil
import atexit
from . import config
from .logger import timelog
from .plotter import timeplot

dirs = [config.LOG_DIR, config.PLOT_DIR]
for dir in dirs:
    if os.path.exists(dir) and config.RESET:
        shutil.rmtree(dir)
    os.makedirs(dir, exist_ok=True)


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