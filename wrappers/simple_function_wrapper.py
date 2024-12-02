import ctypes

# Load the shared library
simple_function = ctypes.CDLL('../compiled/simple_function.so')  # Use .dll on Windows

# Call the print_message function
simple_function.print_message()

# Define and call the add_numbers function
simple_function.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
simple_function.add_numbers.restype = ctypes.c_int

result = simple_function.add_numbers(10, 20)
print(f"Result of adding 10 and 20: {result}")
