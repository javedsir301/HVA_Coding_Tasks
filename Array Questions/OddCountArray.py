def oddCount(arr):
    count = 0
    index = 0
    while index < len(arr):
        count += arr[index] % 2
        index += 1
    print(count)

arr = [4, 7, 9, 10, 13, 17]
oddCount(arr)
