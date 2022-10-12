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
    primes = list(range(2, n+1))
    for num in primes:
        m = 2 # Multiplier
        while ((num * m) <= primes[-1]): # Test for non-primes
            if (num * m) in primes:
                primes.remove(num * m) # Remove non-primes
            m += 1 # Increase multiplier for next iteration
    
    # Only verified primes remain now
    return primes

def goldbachConjectureTest():
    pass