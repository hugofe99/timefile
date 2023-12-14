import picologging as logging
from typing import Callable
import time
from . import config
from .models import TimeLog
from functools import wraps
from .helpers import filter_kwargs


def watch(function: Callable) -> Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        watch_start = time.perf_counter()
        logger = logging.getLogger(function.__name__)
        time_start = time.perf_counter()
        _return = function(*args, **kwargs)
        time_delta = time.perf_counter() - time_start

        arg_kwargs = {kw: arg for arg, kw in zip(args, function.__code__.co_varnames)}
        kwargs.update(arg_kwargs)
        kwargs = filter_kwargs(kwargs)

        log = TimeLog(kwargs=kwargs, time_delta=time_delta, _fn=function.__name__)
        logger.log(config.LOGGING_LEVEL_VALUE, log.json_str())
        logging.getLogger('watch').log(config.LOGGING_LEVEL_VALUE, TimeLog(kwargs={}, time_delta=time.perf_counter() - watch_start).json_str())
        return _return

    return wrapper
