# Fibonacci Code

def fibonacciUpTo(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f

def isFibonacci(n): # Test if n is a fibonacci number
    if n in fibonacciUpTo(n):
        return True
    
    return False

# States that every positive integer can be expressed as the sum of two distinct, non-neighbouring fibonacci numbers
def zeckendorfTheorem(n): # Returns a pair of non-neighbouring fibonacci numbers that add to a positive integer n
    test = fibonacciUpTo(n) 
    for fn in test:
        diff = (n - fn)
        # Check if both are fibonacci numbers that are atleast 2 indices away from eachother (not neighbouring)
        if isFibonacci(diff) and (abs(test.index(fn) - test.index(diff)) >= 2):
            return fn, diff

def fibonacciCode(n):
    pass