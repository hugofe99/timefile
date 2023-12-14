from timefile import watch

@watch
def f1(a, b):
    return a + b

@watch
def n():
    pass
# @watch()
# def f2(a, b):
#     return a + b

# @watch(lambda a: a)
# def f3(a, b):
#     return a + b

# @watch(lambda a: str(a))
# def f4(a, b):
#     return a + b

n()
for i in range(10**5):
    f1(1,2)
    # f2(1,2)
    # f3(1,2)
    # f4(1,2)