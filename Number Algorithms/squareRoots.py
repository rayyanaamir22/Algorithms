# Square roots

'''
# Recursion
def sqrt(n, precision):
    def helper(x=n/2): # Let x represent the initial guess
        if str(n)[:precision+1] == str(x)[:precision+1]: # Base case
            return n
        else:
            x1 = (x+(n/2))/2
'''

# Iterative
def babylonianSqrt(n, precision): # Precision is num of digits following decimal, not total digits
    if n < 0:
        return None
    
    x = n
    x1 = n/2

    while (x-x1) > (10**(-precision)):
        x = (x+x1)/2
        x1 = n/x

    root = round(x, precision)
    return root

# Iterative
def newtonianSqrt(n, precision): 
    x = n

    while True:
        root = (x + (n/x)) / 2
        if (abs(root - x) < precision):
            return root

        x = root # For next iteration