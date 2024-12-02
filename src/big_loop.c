#include <stdio.h>

void perform_loop(int iterations, double seed) {
    double result = seed;
    for (int i = 0; i < iterations; i++) {
        result += 1;  // Example logic to prevent overflow
    }
    printf("Final result after %d iterations: %f\n", iterations, result);
}