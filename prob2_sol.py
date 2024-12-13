import time
import random
from concurrent.futures import ThreadPoolExecutor

def timeconsumingfun():
    pause_time = random.uniform(1, 5)  # Random pause between 1 and 5 seconds
    time.sleep(pause_time)             

def run_serial(n):
    start_time = time.time()  # Start timer
    for _ in range(n):
        timeconsumingfun()    # Run time-consuming function serially
    end_time = time.time()    # Stop timer
    return end_time - start_time

def run_parallel(n, num_workers):
    start_time = time.time()  # Start timer
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(timeconsumingfun) for _ in range(n)]
        for future in futures:
            future.result()  
    end_time = time.time()    
    return end_time - start_time

def calculate_metrics(serial_time, parallel_time, num_workers):
    speedup = serial_time / parallel_time
    efficiency = speedup / num_workers
    return speedup, efficiency

def run_experiment(n, num_workers):
    serial_time = run_serial(n)
    print(f"Serial Execution Time for n = {n}: {serial_time:.2f} seconds")

    parallel_time = run_parallel(n, num_workers)
    print(f"Parallel Execution Time for n = {n} with {num_workers} workers: {parallel_time:.2f} seconds")

    speedup, efficiency = calculate_metrics(serial_time, parallel_time, num_workers)
    
    print(f"Speedup: {speedup:.2f}")
    print(f"Efficiency: {efficiency:.2f}")
    print('-----------------------------------')

small_n = 10
medium_n = 100
large_n = 1000

num_workers = 4

if _name_ == "_main_":
    
    print('Running small n experiment...')
    run_experiment(small_n, num_workers)
    print('Running medium n experiment...')
    run_experiment(medium_n, num_workers)

    print('Running large n experiment...')
    run_experiment(large_n, num_workers)
