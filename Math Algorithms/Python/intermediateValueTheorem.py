# Some theorems from MAT137

def findBounds(f, guess, sol=0, distance=10):
    """
    Given a function f and a guess, return potential max and min values for the solution of f.

    Optional Parameters:
    "sol": Defaulted to zero, lets user specify the solution
    "distance": Defaulted to 10, lets user specify the range of tolerance (inclusive) for a solution to be within of guess
    """
    # Store a variable alt which is the max/min complementary to guess
    # IF f(guess) > sol, then guess is max and alt is min
    # IF f(guess) < sol, then guess is min and alt is max
    alt = guess//2
    t = 0 # Tries
    while (t < 1_000):
        y1, y2 = f(guess), f(alt)

        if (y1 > sol and y2 < sol):
            if (abs(guess - alt) <= distance): # Within tolerance
                return guess, alt
        elif (y1 > y2 > sol):
            guess -= alt # Make guess smaller than alt
        elif (y2 > y1 > sol):
            alt -= guess # Make alt smaller than guess
        elif (sol > y1 > y2):
            alt += guess
        elif (sol > y2 > y1):
            guess += alt

        # Increment tries
        t += 1

    return None


def h(x): return x**2 - 1
print(findBounds(h, 0))

class IntermediateValueTheorem:
    def __init__(self, f, precision=2, sol=0, guess=0):
        self.f = f
        self.precision = precision
        self.sol = sol
        self.guess = guess

    def approx(self, f):
        """
        Given a continous function f, return a solution, valid to 2 decimal points.

        Optional Parameters:
        "precision": Defaulted to 2, lets user specify number of decimal points the solution is valid to
        "sol": Defaulted to zero, lets user specify the solution
        "guess": Defaulted to zero, given to shorten the approximation.

        Examples:
        >>> def g(x): return ((x**3) + (2x) - 1) 
        >>> intermediateValueTheorem(g, 3)
        {output}
        """ 