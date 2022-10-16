# Factorials

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))

# Factorial but multiply by numbers with same parity (even or odd)
def doubleFactorial(n):
    if (n in [0, 1]):
        return 1
    else:
        return (n * doubleFactorial(n-2))

