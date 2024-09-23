def countUntilNegative(arr):
    index = 0
    count = 0
    while index < len(arr):
        try:
            negativeFound = arr[index] < 0
        except:
            negativeFound = False

        if negativeFound:
            break
        
        count += 1
        index += 1
    
    print(count)
    
arr = [3, 6, 2, -1, 8, 2, 1]
countUntilNegative(arr)
