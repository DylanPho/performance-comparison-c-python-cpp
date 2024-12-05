import ctypes
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
so_path = os.path.join(current_dir, "../compiled/simple_function.so")
simple_function = ctypes.CDLL(so_path)

# Call the print_message function
simple_function.print_message()

# Define and call the add_numbers function
simple_function.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
simple_function.add_numbers.restype = ctypes.c_int

result = simple_function.add_numbers(10, 20)
print(f"Result of adding 10 and 20 is {result}")
