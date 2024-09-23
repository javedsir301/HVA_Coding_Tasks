def minimumInArray(arr):
    min_value = arr[0]
    index = 1
    while index < len(arr):
        min_value = (arr[index] * (arr[index] < min_value)) + (min_value * (arr[index] >= min_value))
        index += 1
    print(min_value)

arr = [10, 5, 6, 3, 4, 3, 5, 6]
minimumInArray(arr)
