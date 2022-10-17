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
def eratosthenes(n): # Sieve of Eratosthenes
    primes = list(range(2, n+1))
    for num in primes:
        m = 2 # Multiplier
        while ((num * m) <= primes[-1]): # Test for non-primes
            if (num * m) in primes:
                primes.remove(num * m) # Remove non-primes
            m += 1 # Increase multiplier for next iteration
    
    # Only verified primes remain now
    return primes

# Same function but makes use of isPrime(n) 
def primesUpTo(n):
    primes = list(range(2, n+1))
    for num in primes:
        if not isPrime(num):
            primes.remove(num)

    return primes

# Returns first n prime numbers
def firstPrimes(n):
    if n<0:
        raise ValueError

    primes = []
    p = 0
    while (len(primes) != n):
        if isPrime(p):
            primes.append(p)

        p += 1 # Test next number

    return primes

# Factorial but only multiply prime numbers
def primorial(n):
    pm = 1 # Base for multiplication
    primes = firstPrimes(n)
    for prime in primes:
        pm *= prime
    return pm

# Returns a pair of prime numbers that add to an even integer greater than 2, n
def goldbachConjecture1(n):
    for x in range(2, n//2):
        y = (n - x)
        if (isPrime(x) and isPrime(y)):
            return x, y

# Same function but using eratosthenes(n) instead of isPrime(n)
def goldbachConjecture2(n):
    x, y = 0, 0
    sum = 0
    if (n%2 == 0): # n is even
        primesToTest = eratosthenes(n)
        
        while sum != n:
            for i in range(len(primesToTest)):
                if sum == n:
                   break
                x = primesToTest[i]
                for j in range(len(primesToTest)):
                    y = primesToTest[j]
                    sum = (x+y)
                    if sum == n: 
                        return x, y

# Return list of prime factors of a number
def primeFactors(n):
    pf = []
    while (n%2==0): # n is even
        pf.append(2)
        n /= 2

    for i in range(3, int(n**(1/2))+1, 2): # n is odd
        while (n%i==0):
            pf.append(i)
            n /= i

    if (n>2): # n is prime and greater than 2
        pf.append(n)

    return pf

# Same function using Sieve of Eratosthenes
def eratosthenesPrimeFactors(n):
    pf = []
    count = 2
    while (n>1):
        if (n%count==0):
            pf.append(count)
            n /= c
        else:
            c +=1

    return pf
