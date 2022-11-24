def variance(x: list[float]):
    """
    Return the variance of a dataset. If dataset is empty, return None
    """
    if(len(x)): 
        numerator = 0
        xBar = sum(x)/len(x) # Arithmetic mean
        for pt in x: # Sigma
            numerator+=(pt-xBar)**2
        try:
            return numerator/(len(x)-1) # /(n-1)
        except ZeroDivisionError: # Constant (dataset has one pt)
            return 0

    return None # Empty dataset

def std(x: list[float]):
    """
    Return the standard deviation of a dataset. If dataset is empty, return None.
    """
    try:
        return variance(x)**(1/2)
    except TypeError:
        return None

print(std([]))