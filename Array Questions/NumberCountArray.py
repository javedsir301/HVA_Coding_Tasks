def numberCountInArray(arr, number):
    count = 0
    index = 0
    while index < len(arr):
        count += (arr[index] == number)
        index += 1
    print(count)

arr = [4, 7, 9, 10, 7, 14, 12, 4, 7, 27]
numberCountInArray(arr, 7)
