def checkPalindrome(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        if arr[start] != arr[end]:
            return 'No'
        start += 1
        end -= 1
    
    return 'Yes'

array = [1, 2, 3, 2, 1]
result = checkPalindrome(array)
print(result) 
