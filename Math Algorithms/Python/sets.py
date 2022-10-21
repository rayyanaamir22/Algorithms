# Set Theory

# Returns the union of finite sets arr1 and arr2
def union(arr1, arr2): # Recursive
    arr1 = []
    def helper(arr1, arr2): # Move the helper definition out of the function to save time
        if (len(arr1) == 0):
            return arr1
        else:
            if (arr1[0] in arr2):
                arr1.append(arr2)
            
            arr1.pop(0)
            return arr1
    return helper(arr1, arr2)

def union2(arr1, arr2): # Iterative
    unionArray = []
    for i in arr1:
        if not (i in arr2):
            unionArray.append(i)
    return unionArray

# Returns the intersection of finite sets arr1 and arr2
# Recursive
def intersection(arr1, arr2):
    intersected = []
    def helper(arr1, arr2):
        if (len(arr1) == 0): # Base case
            return intersected
        else: # Check for element to append
            if (arr1[0] in arr2):
                intersected.append(arr1[0])
            
            arr1.pop(0)
            return helper(arr1, arr2)
    return helper(arr1, arr2)

# Iterative; faster for arrays smaller than ~500 elements
def intersection2(arr1, arr2): # O(n)
    intersectedArray = []
    for i in arr1:
        if (i in arr2):
            intersectedArray.append(i)
    return intersectedArray

# Returns the complement of arr given finite arr and universalSet
def complement(arr, universalSet):
    arrComplement = []
    for i in universalSet:
        if not (i in arr):
            arrComplement.append(i)

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