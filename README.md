# ⏱️ timefile
Probably the simplest time profiling in python 

## 📍 Getting started
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
Check out the plots saved in the **timefiles/plots/** directory for visualizations of the runtime.

## 🍻 Feedback and Contributions
I warmly welcome any contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas.
Feel free to create issues or pull requests at the [timefile GitHub](https://github.com/hugofe99/timefile).

## 🛣️ Roadmap
 - [ ] Tests !!!
 - [ ] Documentation
 - [ ] Small fixes / cleanup
 - [ ] Performance improvements
 - [ ] Prettier plots
 - [ ] Multivariable plots?
 - [ ] Simple regression or analysis? 

___

#### ⚠️ Disclaimer 
This package is designed for simple runtime insights and is **not** optmized for performance. For more comprehensive profiling in Python, consider using more robust tools like cProfile, timeit, line_profiler, etc.