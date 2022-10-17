# Set Theory

# Assume natural numbers begin at 1

# Given a positive integer n, divide first n natural numbers into 2 subsets with minimal difference
# Returns the DIFFERENCE only
def subsetDiff(n):
    # Formula for sum of first n natural numbers
    sum = int(n * (n+1) / 2)

    if (n%4==0): # Divisible by 4
        diff = 0
    else:
        if (n%4) in [1, 2]:
            diff = 1
        else:
            diff = 0

    return diff

# Given a positive integer n, divide first n natural numbers into 2 subsets with minimal difference
# Returns the SUBSETS only
def approxEvenSubsets(n): # Doesn't work
    nums = list(range(1, n+1))

    # Organize nums into 4-element subsets
    subLists = []
    while (nums): # List is not empty
        if (len(nums)>4):
            sub = nums[:5] # First 4 elements
            nums = nums[5:] # Remove first 4 elements of nums
        else:
            sub = nums
            nums = [] # Loop will terminate

        subLists.append(sub)


    subset1, subset2 = [], []
    for lst in subLists:
        subset1.extend(lst[:3]) # First 2 items to s1
        subset2.extend(lst[3:]) # Last 2 items to s2

    return subset1, subset2
