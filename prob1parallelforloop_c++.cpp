#include <iostream>
#include <cmath>
#include <omp.h>
#include <chrono>

using namespace std;

double f(double x) {
    return sin(3 * M_PI * cos(2 * M_PI * x) * sin(M_PI * x));
}

double bisection(double a, double b, double tol = 1e-6) {
    double mid;
    while ((b - a) >= tol) {
        mid = (a + b) / 2;
        if (f(mid) == 0.0)
            break;
        else if (f(mid) * f(a) < 0)
            b = mid;
        else
            a = mid;
    }
    return mid;
}

int main() {
    double a = -3.0, b = 5.0;
    int num_roots = 100;
    double initial_guesses[100];
    
    for (int i = 0; i < num_roots; ++i) {
        initial_guesses[i] = a + i * (b - a) / num_roots;
    }
    auto start = chrono::high_resolution_clock::now();

    #pragma omp parallel for
    for (int i = 0; i < num_roots; ++i) {
        double root = bisection(a, b);
        #pragma omp critical
        cout << "Root: " << root << endl;
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "Parallel Execution Time: " << elapsed.count() << " seconds" << endl;

    return 0;
}

