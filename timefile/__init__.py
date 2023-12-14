from .exp import watch

__all__ = ["watch"]


def __init__():
    import picologging as logging
    import os
    import shutil
    import atexit
    from . import config
    from .models import TimeLog
    from .plotter import timeplot
    import time

    dirs = [config.LOG_DIR, config.PLOT_DIR]
    for dir in dirs:
        if os.path.exists(dir) and config.RESET and dir == config.LOG_DIR:
            shutil.rmtree(dir)
        os.makedirs(dir, exist_ok=True)

    # logging.addLevelName(
    #     level=config.LOGGING_LEVEL_VALUE, levelName=config.LOGGING_LEVEL_NAME
    # )

    logging.basicConfig(
        filename=config.LOG_FILEPATH,
        level=logging.INFO,
        format=config.LOGGING_FORMAT,
        datefmt=config.LOGGING_DATETIME,
    )

    def __log_total_runtime(start_time: float):
        logger = logging.getLogger(config.TOTAL_RUNTIME)
        log = TimeLog(kwargs={}, time_delta=time.perf_counter() - start_time)
        logger.log(config.LOGGING_LEVEL_VALUE, log.json_str())

    atexit.register(timeplot)
    atexit.register(__log_total_runtime, start_time=time.perf_counter())


__init__()
