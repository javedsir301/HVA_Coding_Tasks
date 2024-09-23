def minMaxDifference(arr):
    if not arr:  
        return None

    minVal = arr[0]
    maxVal = arr[0]
    index = 1

    while index < len(arr):
        if arr[index] < minVal:
            minVal = arr[index]
        if arr[index] > maxVal:
            maxVal = arr[index]
        index += 1

    return maxVal - minVal

array = [5 ,4 ,7 ,8 ,4 ,6 ,11 ,9]
result = minMaxDifference(array)
print("Difference between max and min:", result)
