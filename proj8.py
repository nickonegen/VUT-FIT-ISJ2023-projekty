#!/usr/bin/env python3

import collections
from functools import wraps


def log_and_count(key=None, counts=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal key
            key = key or func.__name__
            print(f"called {func.__name__} with {args} and {kwargs}")
            res = func(*args, **kwargs)
            counts[key] += 1
            return res

        return wrapper

    return decorator


if __name__ == "__main__":
    my_counter = collections.Counter()

    @log_and_count(key="basic functions", counts=my_counter)
    def f1(a, b=2):
        return a**b

    @log_and_count(key="basic functions", counts=my_counter)
    def f2(a, b=3):
        return a**2 + b

    @log_and_count(counts=my_counter)
    def f3(a, b=5):
        return a**3 - b

    f1(2)
    f2(2, b=4)
    f1(a=2, b=4)
    f2(4)
    f2(5)
    f3(5)
    f3(5, 4)

    print(my_counter)
