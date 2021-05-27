def calculate_min(arr):
    if(len(arr) == 0):
        return -1
    min = arr[0]
    for element in arr:
        if(min > element):
            min = element
    return min