def checkAscendingOrder(arr):
    index = 1
    
    while index < len(arr):
        try:
            isAscending = arr[index] > arr[index - 1]
        except:
            isAscending = False
        
        if not isAscending:
            print("No")
            return
        
        index += 1
    
    print("Yes")


arr=[3,1,5,8,1]
checkAscendingOrder(arr)