import ctypes
import os
import time
import matplotlib.pyplot as plt

# Dynamically compute the absolute paths to the .so files
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
loop_so_path = os.path.join(current_dir, '../compiled/loop.so')  # Path to loop.so
loop_cpp_so_path = os.path.join(current_dir, '../compiled/loop_cpp.so')  # Path to loop_cpp.so

# Load the shared libraries
loop_c = ctypes.CDLL(loop_so_path)
loop_cpp = ctypes.CDLL(loop_cpp_so_path)

# Define function arguments and return types
loop_c.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_c.perform_loop.restype = None

loop_cpp.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
loop_cpp.perform_loop.restype = None

# Function to run the loop in Python
def python_loop(iterations, seed):
    result = seed
    for _ in range(iterations):
        result += 1
    return result

# Runtime comparison for various iteration counts
iteration_values = [10, 50, 100, 500, 1000, 5000, 10000]
runtimes_c = []
runtimes_python = []
runtimes_cpp = []

seed = 1.00001

for iterations in iteration_values:
    # Measure C runtime
    start_c = time.time()
    loop_c.perform_loop(iterations, seed)
    end_c = time.time()
    runtimes_c.append(end_c - start_c)

    # Measure Python runtime
    start_py = time.time()
    python_loop(iterations, seed)
    end_py = time.time()
    runtimes_python.append(end_py - start_py)

    # Measure C++ runtime
    start_cpp = time.time()
    loop_cpp.perform_loop(iterations, seed)
    end_cpp = time.time()
    runtimes_cpp.append(end_cpp - start_cpp)

# Plotting the runtimes
plt.figure()
plt.plot(iteration_values, runtimes_c, label="C Runtime", marker='o')
plt.plot(iteration_values, runtimes_python, label="Python Runtime", marker='o')
plt.plot(iteration_values, runtimes_cpp, label="C++ Runtime", marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Number of Iterations")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime Comparison: C vs. Python vs. C++")
plt.legend()

# Save and show the plot
plt.savefig('runtime_comparison.png', dpi=300)
plt.show()