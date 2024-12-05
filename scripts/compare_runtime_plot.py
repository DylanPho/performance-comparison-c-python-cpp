import ctypes
import os
import time
import subprocess
import matplotlib.pyplot as plt

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

# Compare runtimes across iteration counts
iteration_values = [10, 50, 100, 500, 1000, 5000, 10000]
runtimes_c = []
runtimes_python = []
runtimes_cpp = []
runtimes_java = []

seed = 1.00001

for iterations in iteration_values:
    # C runtime
    start_c = time.perf_counter()
    loop_c.perform_loop(iterations, seed)
    end_c = time.perf_counter()
    runtimes_c.append(end_c - start_c)

    # Python runtime
    start_py = time.perf_counter()
    python_loop(iterations, seed)
    end_py = time.perf_counter()
    runtimes_python.append(end_py - start_py)

    # C++ runtime
    start_cpp = time.perf_counter()
    loop_cpp.perform_loop(iterations, seed)
    end_cpp = time.perf_counter()
    runtimes_cpp.append(end_cpp - start_cpp)

    # Java runtime
    _, java_time = java_loop(iterations, seed)
    runtimes_java.append(java_time)

# Plot the runtimes
plt.figure()
plt.plot(iteration_values, runtimes_c, label="C Runtime", marker='o')
plt.plot(iteration_values, runtimes_python, label="Python Runtime", marker='o')
plt.plot(iteration_values, runtimes_cpp, label="C++ Runtime", marker='o')
plt.plot(iteration_values, runtimes_java, label="Java Runtime", marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Number of Iterations")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime Comparison: C vs. Python vs. C++ vs. Java")
plt.legend()

# Save and show the plot
plt.savefig('runtime_comparison.png', dpi=300)
plt.show()