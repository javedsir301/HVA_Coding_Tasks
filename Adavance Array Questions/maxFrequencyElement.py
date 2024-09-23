def maxFrequencyElementInArray(arr):
    frequency = {}
    i = 0
    while i < len(arr):
        num = arr[i]
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        i += 1
    
    max_freq = 0
    max_freq_element = None
    i = 0
    while i < len(arr):
        num = arr[i]
        if frequency[num] > max_freq:
            max_freq = frequency[num]
            max_freq_element = num
        i += 1
    
    return max_freq_element

arr = [2, 3, 4, 5, 4, 5, 1, 1, 1]
result = maxFrequencyElementInArray(arr)
print(result)
