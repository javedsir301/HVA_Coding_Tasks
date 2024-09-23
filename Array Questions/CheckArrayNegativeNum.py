def checkNegativeNumbers(arr):
    index = 0
    length = len(arr)
    has_negative = False

    while index < length:
        try:
            has_negative = arr[index] < 0
        except:
            pass

        if has_negative:
            print("Yes")
            return
        index += 1
    
    print("No")

arr=[1,2,3,4,5,-1]
checkNegativeNumbers(arr)
