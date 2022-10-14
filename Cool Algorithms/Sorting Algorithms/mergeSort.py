# Merge sort

def mergeSort(array):
    if len(array) > 1:
        middle = len(array)//2 # Find midpoint 

        left = array[:middle] # Store each half of the array
        right = array[middle:]

        mergeSort(left) # Merge sort each half recursively
        mergeSort(right)

        i = j = k = 0 # Counters to ensure all elements are merged
        while i < len(left) and j < len(right):
            if left[i] < right[j]: # If left is smaller
                array[k] = left[i] # Append 
                i += 1
            else: # If right is smaller 
                array[k] = right[j] # Append
                j += 1

            k += 1 

        # Check any remaining elements
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array