import numpy as np
import time

def f(x):
    return np.sin(3 * np.pi * np.cos(2 * np.pi * x) * np.sin(np.pi * x))

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print(f"No sign change between f({a:.6f}) = {func(a):.6f} and f({b:.6f}) = {func(b):.6f}")
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

a = -3
b = 5
x0 = np.linspace(a, b, 500)  # Generate 500 intervals for root searching

start_time = time.time()

roots = []
for i in range(len(x0) - 1):
    root = bisection_method(f, x0[i], x0[i+1])
    if root is not None and not np.isclose(f(root), 0, atol=1e-4):
        roots.append(root)

end_time = time.time()
serial_time = end_time - start_time

print(f"Serial Execution Time: {serial_time:.6f} seconds")
print(f"Found Roots: {roots}")


