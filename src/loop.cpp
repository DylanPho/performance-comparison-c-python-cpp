#include <iostream>
using namespace std;

extern "C" void perform_loop(int iterations, double seed) {
    double result = seed;
    for (int i = 0; i < iterations; i++) {
        result = result + 1;  // Adjusted formula to prevent overflow
    }
    cout << "Final result after " << iterations << " iterations: " << result << endl;
}