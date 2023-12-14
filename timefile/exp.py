from typing import Callable
from functools import wraps
from timefile.helpers import filter_kwargs
import types
import picologging as logging
import time
from . models import TimeLog
from . import config

def _str(s):
    return str(s)

class NoMap:
    def __init__(self):
        self.__name__ = ''
    def __bool__(self):
        return False

_nm = NoMap()

def watch(mapping=_nm):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            time_start = time.perf_counter()
            result = func(*args, **kwargs)
            time_delta = time.perf_counter() - time_start

            if (func.__name__ == mapping.__name__):
                arg_kwargs = {kw: arg for arg, kw in zip(args, func.__code__.co_varnames)}
                kwargs.update(arg_kwargs)
                kwargs = filter_kwargs(kwargs)
            elif not mapping:
                kwargs = {}
            else:
                kwargs = {}

            log = TimeLog(kwargs=kwargs, time_delta=time_delta, _fn=func.__name__)
            watch_start = time.perf_counter()
            logger.info(log.json_str())
            watch_delta = time.perf_counter() - watch_start
            logging.getLogger('watch').log(config.LOGGING_LEVEL_VALUE, TimeLog(kwargs={}, time_delta=watch_delta).json_str())
            return result
        return wrapper

    if not mapping or (mapping.__code__.co_name == '<lambda>'):
        return decorator
    else:
        return decorator(mapping)




# @watch
# def f1(a, b):
#     return a + b
# f1(1,2)

# @watch()
# def f2(a, b):
#     return a + b
# f2(1,2)

# @watch(lambda a: a)
# def f3(a, b):
#     return a + b
# f3(1,2)

# @watch(lambda a: _str(a))
# def f4(a, b):
#     return a + b
# f4(1,2)





