import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
mandelbrot = ctypes.CDLL('../compiled/mandelbrot.so')  # Use .dll for Windows

# Configure the function's arguments and return types
mandelbrot.mandelbrot.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
mandelbrot.mandelbrot.restype = None

# Mandelbrot settings
size = 400
iterations = 100

# Create an empty array to store the fractal data
col = np.zeros((size * size,), dtype=np.int32)

# Call the C function
mandelbrot.mandelbrot(size, iterations, col.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))

# Reshape and display the result
col = col.reshape((size, size))
plt.imshow(col, cmap='hot', extent=[-2, 2, -2, 2])
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
