def sumOfAllSubarrays(arr):
    n = len(arr)
    sum = 0
    i = 0
    
    while i < n:
        count_subarrays = (i + 1) * (n - i)
        sum += arr[i] * count_subarrays
        i += 1
    
    return sum

arr = [3, 7, 5]

result = sumOfAllSubarrays(arr)
print(result)  
