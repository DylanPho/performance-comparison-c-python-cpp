import ctypes
import os

# Dynamically compute the absolute path to the .so file
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
so_path = os.path.join(current_dir, '../compiled/big_loop.so')  # Path to .so file

# Load the shared library
big_loop = ctypes.CDLL(so_path)

# Example function call (adjust as needed)
def run_big_loop():
    print("Running big loop...")

    # Define function arguments and return types
    big_loop.perform_loop.argtypes = [ctypes.c_int, ctypes.c_double]
    big_loop.perform_loop.restype = None

    # Call the function (example: 10000 iterations and seed 1.00001)
    iterations = 10000
    seed = 1.00001
    big_loop.perform_loop(iterations, seed)
    print("Big loop completed.")

if __name__ == "__main__":
    run_big_loop()