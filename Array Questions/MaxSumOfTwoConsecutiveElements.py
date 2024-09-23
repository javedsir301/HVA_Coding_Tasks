def maxSumConsecutive(array):
    if len(array) < 2:
        raise ValueError("Array must contain at least two elements")
    
    max_sum = float('-inf')
    
    for i in range(len(array) - 1):
        current_sum = array[i] + array[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

arr = [3, 6, 2, 1, 8, 2, 1]
print(maxSumConsecutive(arr))
