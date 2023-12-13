import logging
from typing import Callable
import time
from dataclasses import dataclass, asdict
from . import config
from .models import TimeLog
from functools import wraps
from .helpers import filter_kwargs


def timelog(function: Callable) -> Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(function.__name__)
        time_start = time.perf_counter()
        _return = function(*args, **kwargs)
        time_delta = time.perf_counter() - time_start

        arg_kwargs = {kw: arg for arg, kw in zip(args, function.__code__.co_varnames)}
        kwargs.update(arg_kwargs)
        kwargs = filter_kwargs(kwargs)

        log = TimeLog(kwargs=kwargs, time_delta=time_delta, _fn=function.__name__)
        logger.log(level=config.LOGGING_LEVEL_VALUE, msg=log.json_str())
        return _return

    return wrapper
