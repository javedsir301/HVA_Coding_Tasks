def sumArrayExpectSelf(arr):
    arrSize = len(arr)
    result = []
    
    i = 0
    while i < arrSize:
        sum = 0
        j = 0
        while j < arrSize:
            if j != i:
                sum += arr[j]
            j += 1
        result.append(sum)
        i += 1
    
    return result

arr = [7, 3, 6, 7, 5]
print(sumArrayExpectSelf(arr))  
