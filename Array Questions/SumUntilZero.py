def sumUntilZero(arr):
    index = 0
    total_sum = 0
    
    while index < len(arr):
        try:
            zero_found = arr[index] == 0
        except:
            zero_found = False

        if zero_found:
            break
        
        total_sum += arr[index]
        index += 1
    
    print(total_sum)


arr=[2,3,5,1,0,4,6,3,4]
sumUntilZero(arr)