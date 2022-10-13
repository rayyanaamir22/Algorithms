# Quick sort

def partition(array, low, high):
    pivot = array[high] # Select righmost element as pivot 
    i = low-1 

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i]) # Swap i and j 

    (array[i+1], array[high]) = (array[high], array[i+1]) # Swap pivot with the greater element i

def quickSort(array, low, high):
    if low < high:
        partitionIndex = partition(array, low, high)

        quickSort(low, partitionIndex-1)
        quickSort(partitionIndex+1, high)