from src import timelog

@timelog
def some_function(arg, *args, kwarg, **kwargs):
    return arg, *args, kwarg, *kwargs

some_function(1, *(2,3), kwarg=4, **{'5': 5, '6': 6})

