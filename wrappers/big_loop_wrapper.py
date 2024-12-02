import ctypes
import os
import time

# Dynamically compute the path to the shared library
current_dir = os.path.dirname(__file__)
so_path = os.path.join(current_dir, '../compiled/big_loop.so')

# Load the shared library
big_loop = ctypes.CDLL(so_path)

def run_big_loop():
    print("Running big loop...")
    big_loop.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
    big_loop.perform_loop.restype = None

    iterations = 10000
    seed = 1.00001

    # Time the function
    start = time.perf_counter()
    big_loop.perform_loop(iterations, seed)
    end = time.perf_counter()

    print(f"Big loop runtime: {end - start:.6f} seconds")

if __name__ == "__main__":
    run_big_loop()