# Prime Number Algorithms

# Determine if n is prime
def isPrime(n):
    if (n <= 1): # Integers less than or equal to 1 are not prime
        return False

    for i in range(2, int(n**(1/2)) + 1): # From 2 to square root of n
        if (n % i == 0):
            return False

    return True

# Return a list of all primes less than or equal to a positive integer n
def primesUpTo(n): 
    pass

def goldbachConjectureTest():
    pass