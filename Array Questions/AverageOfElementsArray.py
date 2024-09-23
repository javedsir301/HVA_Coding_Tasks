def averageOfElements(arr):
    sum = 0
    count = 0
    index = 0
    while index < len(arr):
        sum += arr[index]
        count += 1
        index += 1
    print(sum / count)

arr = [10, 5, 6, 3, 4, 3, 5, 6]
averageOfElements(arr)
