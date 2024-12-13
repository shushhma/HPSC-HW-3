import numpy as np
from multiprocessing import Pool
import time

def f(x):
    return np.sin(3 * np.pi * np.cos(2 * np.pi * x) * np.sin(np.pi * x))

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        return None  
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:  
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iter_count += 1
    return (a + b) / 2  

def find_root_interval(interval):
    a, b = interval
    return bisection_method(f, a, b)

a = -3
b = 5
x0 = np.linspace(a, b, 100)  
intervals = [(x0[i], x0[i + 1]) for i in range(len(x0) - 1)]

if _name_ == '_main_':  
    start_time = time.time()

    with Pool() as pool:
        roots = pool.map(find_root_interval, intervals)

    roots = [r for r in roots if r is not None]

    end_time = time.time()
    parallel_time = end_time - start_time

    print(f"Parallel Execution Time: {parallel_time:.6f} seconds")
    print(f"Found Roots: {roots}")

