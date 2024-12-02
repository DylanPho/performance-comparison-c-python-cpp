# Performance Comparison: C, Python, and C++

This project compares the runtime performance of iterative computations in C, Python, and C++. It demonstrates the use of Python's `ctypes` library for cross-language integration and highlights the performance benefits of compiled languages over interpreted ones.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [How to Run](#how-to-run)
6. [Results](#results)

## Overview
This project explores runtime differences between C, Python, and C++ by:
- Writing shared libraries (`.so` files) in C and C++.
- Calling these libraries from Python using the `ctypes` module.
- Measuring and comparing runtimes across these languages.

## Features
- Cross-language integration using `ctypes`.
- Performance benchmarking for iterative computations.
- Logarithmic runtime comparison plots.

## Requirements
- GCC or Clang (for compiling C and C++ files)
- Python 3.x
- Python modules:
  - `matplotlib`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/performance-comparison-c-python-cpp.git
   cd performance-comparison-c-python-cpp

2. Compile the C and C++ source files into shared libraries:
   ```bash
   gcc -shared -o compiled/loop.so -fPIC src/loop.c
   g++ -shared -o compiled/loop_cpp.so -fPIC src/loop.cpp
   gcc -shared -o compiled/big_loop.so -fPIC src/big_loop.c

3. Install Python dependencies:
   ```bash
   pip install matplotlib

## How to Run
### Compare Runtimes
Run the `compare_runtime.py` script to measure runtimes:

`python scripts/compare_runtime.py`

### Generate Runtime Plot
Run the `compare_runtime_plot.py` script to visualize runtimes:

`python scripts/compare_runtime.py`

## Example Output
- The runtime comparison script will print runtimes for each language.
- The plot will display the results and save as `runtime_comparison.png`.

## Results
- C and C++: Near-identical runtimes due to similar compilation processes.
- Python: Significantly slower, demonstrating the overhead of interpreted languages.
- Plot: Logarithmic plot for runtime comparison over varying iteration counts.

## Lessons Leanred
- Cross-language integration is effective for combining performance and flexibility.
- Python is slower but easier to use for high-level tasks.
- Using `ctypes` is an efficient way to integrate C and C++ with Python.

## License
This project is licensed under the MIT License.
