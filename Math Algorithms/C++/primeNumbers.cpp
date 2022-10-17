// Prime Number Algorithms

#include <iostream>
#include <cmath>
using namespace std;

int isPrime(int n) {
    if (n <= 1) { // Integers <=1 are never prime
        return false;
    }

    // Check if n is divisible by any number from 2 to square root of n
    for (int i=2; i<(pow(n, (0.5))+1); i++) { 
        if (n%i==0) {
            return false;
        }
    }

    // Otherwise
    return true;
}

int main() {
    cout << 'Hello World!' << endl;

    return 0;
}