def bubble_sort(arr):
    #Loop until break statement encountered
    while True:
        #Set count to zero
        count = 0
        #Loop through array n - 1 times
        for i in range(len(arr) - 1):
            #Check if i is greater than i + 1
            if arr[i] > arr[i + 1]:
                #Swap places in array
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                #Increment count by 1
                count += 1
                
        #Check to see if any swaps were made
        if count == 0:
            #Break out of loop
            break



    return arr

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        #Set min_idx to i
        min_idx = i

        #Loop throgh arr starting at i + 1
        for a in range(i + 1, len(arr)):
            #If arr[min_idx] is greater than arr[a]
            #set min_idx to a
            if arr[min_idx] > arr[a]:
                min_idx = a

        #Swap places in array
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr


