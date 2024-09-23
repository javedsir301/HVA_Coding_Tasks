def longestIncreasingSubarray(arr):
    if not arr:
        return 0

    maxLength = 1
    currentLength = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            currentLength += 1
        else:
            maxLength = max(maxLength, currentLength)
            currentLength = 1

    maxLength = max(maxLength, currentLength) 
    return maxLength

input_array = [5, 4, 4, 7, 6, 3, 2, 4, 6, 8, 6, 3, 6, 8, 5]
print(longestIncreasingSubarray(input_array)) 
