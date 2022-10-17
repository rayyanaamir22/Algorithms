# Fibonacci Numbers

# Returns list of all fibonacci numbers up to n (for n>0)
def fibonacciUpTo(n): # Including n if fibonacci
    f = [0, 1] 

    for i in range(2, n+1): 
        f.append(f[i-1] + f[i-2])

    return f

def isFibonacci(n): # Test if n is a fibonacci number
    if n in fibonacciUpTo(n):
        return True
    
    return False

# Returns nth fibonacci number
def fibonacci(n): # Recursive
    if n <= 1:
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

def fibonacci2(n): # Iterative
    f = fibonacciUpTo(n)

    return f[n]

def fibonacci3(n): # Golden ratio; only accurate for n < 35
    goldenRatio = float((1 + (5**(1/2))) / 2)
    f = [0, 1, 1, 2, 3, 5]

    if n < 6: # Since the ratio is inaccurate for the first few terms, just store them
        return n

    # Else start counting at 5th element
    i = 5
    fn = 5

    while i < fn:
        fn = round(fn * goldenRatio)
        i += 1

    return fn

# Determine golden ratio using nth fibonacci numbers
def approximateGoldenRatioUsingFibonacci(n): # n must be atleast 1
    # approximateGR = float(fibonacci(n) / fibonacci(n-1))
    # actualGR = float((1 + (5**(1/2))) / 2)
    # error = abs((approximateGR - actualGR) / actualGR)
    # print(f'Error: {error * 100}%)

    return float(fibonacci(n) / fibonacci(n-1))


# States that every positive integer can be expressed as the sum of two distinct, non-neighbouring fibonacci numbers
def zeckendorfTheorem(n): # Returns a pair of non-neighbouring fibonacci numbers that add to a positive integer n
    test = fibonacciUpTo(n) 

    # The Zeckendorf theorem is true for n=1, since the first 3 terms of fibonacci sequence are [0, 1, 1] 
    # and n=1 can be comprised of 0 and the second 1 to avoid neighbouring
    if (n==1): # However, the method below will only count the first occurence of 1, labelling them as neighbouring
        return 0, 1 # Therefore, separate condition for n=1 to keep it true

    for fn in test:
        diff = (n - fn)
        # Check if both are fibonacci numbers that are atleast 2 indices away from eachother (not neighbouring)
        if isFibonacci(diff) and (abs(test.index(fn) - test.index(diff)) >= 2):
            return fn, diff

print(fibonacciUpTo(2)) # Incorrect for n=2 or n=3