#include <stdio.h>
#include <stdlib.h>

// Mandelbrot function: generates fractal data
void mandelbrot(int size, int iterations, int *col) {
    for (int y = 0; y < size; y++) {
        for (int x = 0; x < size; x++) {
            double cx = (x - size / 2.0) * 4.0 / size;
            double cy = (y - size / 2.0) * 4.0 / size;
            double zx = 0.0, zy = 0.0;
            int i;
            for (i = 0; i < iterations; i++) {
                double temp = zx * zx - zy * zy + cx;
                zy = 2.0 * zx * zy + cy;
                zx = temp;
                if (zx * zx + zy * zy > 4.0) break;
            }
            col[y * size + x] = i;
        }
    }
}
