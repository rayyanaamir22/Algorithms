# Prime Number Algorithms

# Returns whether n is prime
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

def primesUpTo2(n):
    primes = list(range(2, n+1))
    for num in primes:
        if not isPrime(num):
            primes.remove(num)

# Returns a pair of prime numbers that add to an even integer greater than 2, n
def goldbachConjecture1(n):
    for x in range(2, n//2):
        y = (n - x)
        if (isPrime(x) and isPrime(y)):
            return x, y

def goldbachConjecture2(n):
    x, y = 0, 0
    sum = 0
    if (n%2 == 0): # n is even
        primesToTest = primesUpTo(n)
        
        while sum != n:
            for i in range(len(primesToTest)):
                if sum == n:
                   break
                x = primesToTest[i]
                for j in range(len(primesToTest)):
                    y = primesToTest[j]
                    sum = (x+y)
                    if sum == n: 
                        break

    return x, y