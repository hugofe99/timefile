from src import timelog

@timelog
def some_function(some_argument, another_argument):
    return

@timelog
def another_function(some_input, another_input): 
    return 

some_function(1,2)
some_function(3,4)
another_function('a', 'b')
another_function('c', 'd')
some_function(1,2)
some_function(3,4)
another_function('a', 'b')
another_function('c', 'd')
