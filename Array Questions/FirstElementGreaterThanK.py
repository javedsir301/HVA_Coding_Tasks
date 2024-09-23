def firstElementGreater_than_k(arr, k):
    index = 0
    
    while index < len(arr):
        try:
            greaterThan_k = arr[index] > k
        except:
            greaterThan_k = False
        
        if greaterThan_k:
            print(arr[index])
            return
        
        index += 1
    
    print("No")


k=int(input("Enter the Value of K : "))
arr=[2,3,4,6]
firstElementGreater_than_k(arr,k)