#include <stdio.h>

// Perform loop function
double perform_loop(int iterations, double seed) {
    double result = seed;
    for (int i = 0; i < iterations; i++) {
        result += 1.0;  // Increment result
    }
    // Only return the final result, do not print inside the loop
    return result;
}