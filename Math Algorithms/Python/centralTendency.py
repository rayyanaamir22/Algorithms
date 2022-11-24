def arithmeticMean(x: list[float]) -> float:
    """
    Return the arithmetic mean of a numerical dataset.
    """
    return sum(x) / len(x)

def median(x: list[float]) -> float:
    """
    Return the median of a numerical dataset.
    """
    from math import ceil, floor
    x.sort()
    if (len(x)%2 != 0): # Odd length
        return x[len(x)/2]
    
    return (x[floor(len(x)/2)] + x[ceil(len(x)/2)]) / 2 # Average of 2 middle vals