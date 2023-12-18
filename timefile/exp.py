from typing import Callable
from functools import wraps
from timefile.helpers import filter_kwargs
import types
import logging
import time
from . models import TimeLog
from . import config


class NoMap:
    def __init__(self):
        self.__name__ = ''
    def __bool__(self):
        return False

_nm = NoMap()



import queue
import threading
import atexit


log_queue = queue.Queue()

def log_worker():
    while True:
        logger_name, log_record = log_queue.get()
        if log_record is None:  # Signal to exit the thread
            break
        logger = logging.getLogger(logger_name)
        logger.handle(log_record)
        log_queue.task_done()


log_thread = threading.Thread(target=log_worker)
log_thread.daemon = True
log_thread.start()

def watch(mapping=_nm):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.perf_counter()
            result = func(*args, **kwargs)
            time_delta = time.perf_counter() - time_start

            watch_start = time.perf_counter()
            if (func.__name__ == mapping.__name__):
                arg_kwargs = {kw: arg for arg, kw in zip(args, func.__code__.co_varnames)}
                kwargs.update(arg_kwargs)
                kwargs = filter_kwargs(kwargs)
            elif not mapping:
                kwargs = {}
            else:
                kwargs = {}

            log = TimeLog(kwargs=kwargs, time_delta=time_delta, _fn=func.__name__)
            log_queue.put(
                (
                    func.__name__,
                    logging.LogRecord(
                        name=func.__name__, 
                        level=config.LOGGING_LEVEL_VALUE, 
                        pathname=None,
                        lineno=None,
                        msg=log.json_str(),
                        args=None,
                        exc_info=None
                    )
                )
            )
            watch_delta = time.perf_counter() - watch_start
            log_queue.put(
                (
                    'watch',
                    logging.LogRecord(
                        name='watch', 
                        level=config.LOGGING_LEVEL_VALUE, 
                        pathname=None,
                        lineno=None,
                        msg=TimeLog(kwargs={}, time_delta=watch_delta).json_str(),
                        args=None,
                        exc_info=None
                    )
                )
            )
            return result
        return wrapper

    if not mapping or (mapping.__code__.co_name == '<lambda>'):
        return decorator
    else:
        return decorator(mapping)


def cleanup_log_queue_thread():
    start = time.perf_counter()
    log_queue.put((None, None))
    log_thread.join()
    delta = time.perf_counter() - start
    print(f'Time to cleanup thread {delta}')


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





