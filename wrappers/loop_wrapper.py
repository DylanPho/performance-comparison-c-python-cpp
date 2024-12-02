import ctypes
import time
import math

# Parameters
iterations = 10000
seed = 1.00001

# Load the C shared library
loop_c = ctypes.CDLL('../compiled/loop.so')

# Define the C function signature
loop_c.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_c.perform_loop.restype = None

# Measure runtime for the C function
print("Running loop in C...")
start_c = time.time()
loop_c.perform_loop(iterations, seed)
end_c = time.time()
print(f"C function runtime: {end_c - start_c:.6f} seconds")

# Measure runtime for the Python function
print("\nRunning loop in Python...")
start_py = time.time()
result = seed
overflow_iteration = -1
for i in range(iterations):
    result = (result + 1) * (result + 1)
    if math.isinf(result):
        overflow_iteration = i
        print(f"Overflow detected at iteration {i}")
        break
end_py = time.time()
print(f"Python function runtime: {end_py - start_py:.6f} seconds")
print(f"Final result after {iterations} iterations in Python: {result if not math.isinf(result) else 'inf'}")
