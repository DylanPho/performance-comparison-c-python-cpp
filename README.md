# Performance Comparison: C, C++, Python, and Java

This project compares the runtime performance of iterative computations in C, C++, Python, and Java. It demonstrates the use of Python's `ctypes` library for cross-language integration and highlights the performance differences between compiled and interpreted languages.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [How to Run](#how-to-run)
6. [Results](#results)
7. [Lessons Learned](#lessons-learned)
8. [License](#license)

## Overview
This project explores runtime differences between C, C++, Python, and Java by:
- Writing shared libraries (`.so` files) in C and C++.
- Calling these libraries from Python using the `ctypes` module.
- Measuring and comparing runtimes across these languages.
- Integrating Java for an additional runtime comparison.

## Features
- Cross-language integration using `ctypes` and `subprocess`.
- Performance benchmarking for iterative computations.
- Logarithmic runtime comparison plots.
- Demonstrates Java's runtime performance alongside C, C++, and Python.

## Requirements
- GCC or Clang (for compiling C and C++ files)
- Python 3.x
- Java Development Kit (JDK)
- Python modules:
  - `matplotlib`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/performance-comparison-c-python-cpp-java.git
   cd performance-comparison-c-python-cpp-java

2. Compile the C and C++ source files into shared libraries:
   ```bash
   gcc -shared -o compiled/loop.so -fPIC src/loop.c
   g++ -shared -o compiled/loop_cpp.so -fPIC src/loop.cpp

3. Compile the Java file:
   ```bash
   javac -d compiled src/Loop.java

4. Install Python dependencies:
   ```bash
   pip install matplotlib

## How to Run
### Compare Runtimes
1. Run the `compare_runtime.py` script to measure runtimes:
   ```bash
   `python scripts/compare_runtime.py`

### Generate Runtime Plot
2. Run the `compare_runtime_plot.py` script to visualize runtimes:
   ```bash
   `python scripts/compare_runtime.py`

## Example Output
- **Text Output**: The `compare_runtime.py` script prints the runtime for each language along with the final result.
   ```bash
   Running loop in C...
   C runtime: 0.000040 seconds, Result: 10001.000010
   Running loop in Python...
   Python runtime: 0.000397 seconds, Result: 10001.000010
   Running loop in C++...
   C++ runtime: 0.000015 seconds, Result: 10001.000010
   Running loop in Java...
   Java runtime: 0.000045 seconds, Result: 10001.000010
- **Plot Output**: The compare_runtime_plot.py script generates a runtime_comparison.png file showing the runtime comparison on a logarithmic scale.

## Results
- **C and C++**: Near-identical runtimes due to similar compilation processes.
- **Java**: Competitive runtime due to Just-In-Time (JIT) compilation but slightly slower than C/C++.
- **Python**: Significantly slower, demonstrating the overhead of interpreted languages.

## Lessons Leanred
- **Cross-Language Integration**: Combining Python with C/C++/Java leverages performance and flexibility.
- **Performance Tradeoffs**: Compiled languages (C, C++, Java) excel in performance, while Python offers ease of development.
- **Effective Use of Tools**: `ctypes` and `subprocess` enable seamless integration across languages.

## License
This project is licensed under the MIT License.
