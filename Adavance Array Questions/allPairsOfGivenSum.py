def allPairOfGivenSum(arr, target):
    arr.sort() 
    pairs = []
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        
        if sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1  
        elif sum < target:
            left += 1  
        else:
            right -= 1 
    
    return pairs

arr = [1, 2, 3, 4, 5]
target = 5
result = allPairOfGivenSum(arr, target)
print(result)  
