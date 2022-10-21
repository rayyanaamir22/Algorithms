// Prime Numbers

function isPrime(n) {
    console.log("hello world!");

    if (n<=1) { // 1 or less is never prime
        return false;
    }

    for (i=2; i<((n**(1/2))+1); i++) { // If divisible by any number from 2 to sqrt(n)
        if (n%i==0) {
            return false;
        }
    }

    return true; // All numbers not satisfying first 2 cases are prime
}