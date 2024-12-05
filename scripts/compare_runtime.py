import ctypes
import os
import time

# Paths to shared libraries
current_dir = os.path.dirname(__file__)
loop_so_path = os.path.join(current_dir, '../compiled/loop.so')
loop_cpp_so_path = os.path.join(current_dir, '../compiled/loop_cpp.so')

# Load shared libraries
loop_c = ctypes.CDLL(loop_so_path)
loop_cpp = ctypes.CDLL(loop_cpp_so_path)

# Define argument and return types
loop_c.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_c.perform_loop.restype = ctypes.c_double

loop_cpp.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_cpp.perform_loop.restype = ctypes.c_double

# Python function
def python_loop(iterations, seed):
    result = seed
    for _ in range(iterations):
        result += 1
    return result

# Compare runtimes
def compare_runtimes():
    iterations = 1000000000
    seed = 1.00001
    num_runs = 100  # Averaging over 100 runs

    # C runtime
    print("Running loop in C...")
    total_c_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        result_c = loop_c.perform_loop(iterations, seed)
        total_c_time += time.perf_counter() - start_time
    avg_c_time = total_c_time / num_runs
    print(f"Final result after {iterations} iterations: {result_c:.6f}")
    print(f"Average C runtime over {num_runs} runs: {avg_c_time:.6f} seconds\n")

    # Python runtime
    print("Running loop in Python...")
    total_py_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        result_py = python_loop(iterations, seed)
        total_py_time += time.perf_counter() - start_time
    avg_py_time = total_py_time / num_runs
    print(f"Final result after {iterations} iterations: {result_py:.6f}")
    print(f"Average Python runtime over {num_runs} runs: {avg_py_time:.6f} seconds\n")

    # C++ runtime
    print("Running loop in C++...")
    total_cpp_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        result_cpp = loop_cpp.perform_loop(iterations, seed)
        total_cpp_time += time.perf_counter() - start_time
    avg_cpp_time = total_cpp_time / num_runs
    print(f"Final result after {iterations} iterations: {result_cpp:.6f}")
    print(f"Average C++ runtime over {num_runs} runs: {avg_cpp_time:.6f} seconds\n")

if __name__ == "__main__":
    compare_runtimes()