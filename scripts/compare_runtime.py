import ctypes
import os
import time

# Dynamically compute the absolute paths to the .so files
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
loop_so_path = os.path.join(current_dir, '../compiled/loop.so')
loop_cpp_so_path = os.path.join(current_dir, '../compiled/loop_cpp.so')

# Load the shared libraries
loop_c = ctypes.CDLL(loop_so_path)
loop_cpp = ctypes.CDLL(loop_cpp_so_path)

# Define function arguments and return types
loop_c.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_c.perform_loop.restype = None

loop_cpp.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_cpp.perform_loop.restype = None

# Compare runtimes for C and Python
def compare_runtimes():
    iterations = 10000
    seed = 1.00001

    # Measure C runtime
    print("Running loop in C...")
    start_c = time.time()
    loop_c.perform_loop(iterations, seed)
    end_c = time.time()
    print(f"C function runtime: {end_c - start_c:.6f} seconds")

    # Measure Python runtime
    print("\nRunning loop in Python...")
    start_py = time.time()
    result = seed
    for _ in range(iterations):
        result += 1
    end_py = time.time()
    print(f"Python function runtime: {end_py - start_py:.6f} seconds")
    print(f"Final result after {iterations} iterations in Python: {result}")

    # Measure C++ runtime
    print("\nRunning loop in C++...")
    start_cpp = time.time()
    loop_cpp.perform_loop(iterations, seed)
    end_cpp = time.time()
    print(f"C++ function runtime: {end_cpp - start_cpp:.6f} seconds")

if __name__ == "__main__":
    compare_runtimes()