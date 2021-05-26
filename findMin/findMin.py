def findMin(arr):
    min = 1000000
    for element in arr:
        if(min > element):
            min = element
    return element