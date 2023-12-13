from src import timelog
import time

@timelog
def some_function(some_argument, another_argument):
    time.sleep(0.01)
    return

@timelog
def a_thing(some_input, another_input): 
    time.sleep(0.02)
    return 

@timelog
def foo(): 
    time.sleep(0.02)
    return

@timelog
def bar(): 
    time.sleep(0.02)
    return

some_function(1,2)
some_function(3,4)
a_thing('a', 'b')
foo()
bar()

