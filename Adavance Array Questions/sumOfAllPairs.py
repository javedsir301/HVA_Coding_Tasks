def sumOfAllPairs(arr):
    n = len(arr)
    arr.sort()
    sum = 0
    i = 0
    
    while i < n:
        eachElement = (n - 1 - 2 * i) * arr[i]
        sum += eachElement
        i += 1 
    
    return abs(sum)


arr = [7 ,3 ,6 ,4]
print(sumOfAllPairs(arr))
