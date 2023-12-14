from timefile import watch
import time

@watch
def o_one(n):
    time.sleep(n/10**4)

@watch
def o_two(m):
    time.sleep(m**2/10**4)

for i in range(10):
    o_one(i)
    o_two(i)