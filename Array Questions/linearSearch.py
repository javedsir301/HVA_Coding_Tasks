def linear_search(arr, target):
    index = 0
    
    while index < len(arr):
        try:
            numberFound = arr[index] == target
        except:
            numberFound = False

        if numberFound:
            print("Yes")
            return
        
        index += 1
    
    print("No")

target=int(input("Enter the Target Value : "))
arr=[3,4,5,6,1]
linear_search(arr,target)