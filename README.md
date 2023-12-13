# ⏱️ timefile
Probably the simplest time profiling in python 

### 📍 Getting started
```
pip install timefile
```

To time your functions simply import <code>timelog</code> like this:
```python
from timefile import timelog
import time

@timelog
def o_one(n):
    time.sleep(n/10**4)

@timelog
def o_two(m):
    time.sleep(m**2/10**4)

for i in range(10):
    o_one(i)
    o_two(i)
```
Check out the plots saved in **timefiles/plots/**

### 🍻 Feedback and Contributions
I warmly welcome any bug reports, bug fixes, documentation improvements, enhancements, and ideas.

___

### ⚠️ Performance 
This package is built for simple runtime insight. For proper profiling in python check out more serious tools like cProfile, timeit, line_profiler, etc...