def sumOfelements(arr):
    sum = 0
    index = 0
    while index < len(arr):
        sum += arr[index]
        index += 1
    print(sum)

arr = [10, 5, 6, 3, 4, 3, 5, 6]
sumOfelements(arr)
