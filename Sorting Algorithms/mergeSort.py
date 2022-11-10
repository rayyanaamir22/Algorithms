# Merge sort

def mergeSort(array: list) -> None:
    '''
    Given a list, sort it using the merge sort algorithm
    '''
    if (len(array) > 1): # Base case
        middle = len(array)//2 # Midpoint 

        # Store each half of the array
        left = array[:middle] 
        right = array[middle:]

        # Merge sort each half recursively
        mergeSort(left) 
        mergeSort(right)

        i = j = k = 0 # Counters to ensure all elements are merged
        while ((i < len(left)) and (j < len(right))):
            if (left[i] < right[j]): # If left is smaller
                array[k] = left[i] # Reassing in array
                i += 1
            else: # If right is smaller 
                array[k] = right[j] # Reassign in array
                j += 1
            k += 1 

        # Check any remaining elements
        while (i < len(left)):
            array[k] = left[i]
            i += 1
            k += 1
        while (j < len(right)):
            array[k] = right[j]
            j += 1
            k += 1

arr = [4,3,67,21,23,4,0,1]
mergeSort(arr)
print(arr)