# Some theorems from MAT137

def intermediateValueTheoremCalculator(f, precision, value=0, upperGuess=0):
    """
    Given a 2d function "f", return the float solution, valid to a number of decimal points "precision"

    Optional parameters:
    "value": Defaulted to zero, lets user specify the solution
    "upperGuess": Defaulted to zero, given to shorten the approximation.



    >>> def myFunc(x): return ((x**3) + (2x) - 1) 
    >>> intermediateValueTheorem(myFunc, 3, 0)
    {output}
    """

    while (True):
        # First, check if upperGuess gives valid output
        pass