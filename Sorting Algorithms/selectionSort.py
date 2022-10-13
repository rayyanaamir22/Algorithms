# Selection Sort

def selectionSort(array): 
    for i in range(len(array)): # Loop through array

        min = i # Store the first item as reference
        for j in range(i+1, len(array)): # Loop through rest of the array (ignoring the current min)
            if array[min] > array[j]:
                min = j # Move it to current min
    
        array[i], array[min] = array[min], array[i] # Swap min with the first element

    return array