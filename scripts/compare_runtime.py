import ctypes
import os
import time
import subprocess

# Paths to shared libraries and Java class
current_dir = os.path.dirname(__file__)
loop_so_path = os.path.join(current_dir, '../compiled/loop.so')
loop_cpp_so_path = os.path.join(current_dir, '../compiled/loop_cpp.so')
java_class_path = os.path.join(current_dir, '../compiled')

# Load shared libraries
loop_c = ctypes.CDLL(loop_so_path)
loop_cpp = ctypes.CDLL(loop_cpp_so_path)

# Define argument and return types for C and C++
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

# Java function wrapper
def java_loop(iterations, seed):
    command = [
        "java",
        "-cp",
        java_class_path,
        "Loop",
        str(iterations),
        str(seed)
    ]
    start_time = time.perf_counter()
    result = subprocess.check_output(command, text=True).strip()
    end_time = time.perf_counter()
    return float(result), end_time - start_time

# Compare runtimes
def compare_runtimes():
    iterations = 1000000000
    seed = 1.00001

    # C runtime
    print("Running loop in C...")
    start_time = time.perf_counter()
    result_c = loop_c.perform_loop(iterations, seed)
    c_runtime = time.perf_counter() - start_time
    print(f"C runtime: {c_runtime:.6f} seconds, Result: {result_c:.6f}")

    # Python runtime
    print("Running loop in Python...")
    start_time = time.perf_counter()
    result_py = python_loop(iterations, seed)
    python_runtime = time.perf_counter() - start_time
    print(f"Python runtime: {python_runtime:.6f} seconds, Result: {result_py:.6f}")

    # C++ runtime
    print("Running loop in C++...")
    start_time = time.perf_counter()
    result_cpp = loop_cpp.perform_loop(iterations, seed)
    cpp_runtime = time.perf_counter() - start_time
    print(f"C++ runtime: {cpp_runtime:.6f} seconds, Result: {result_cpp:.6f}")

    # Java runtime
    print("Running loop in Java...")
    result_java, java_runtime = java_loop(iterations, seed)
    print(f"Java runtime: {java_runtime:.6f} seconds, Result: {result_java:.6f}")

if __name__ == "__main__":
    compare_runtimes()