def squareElements(arr):
    index = 0
    while index < len(arr):
        print(arr[index] * arr[index], end=" ")
        index += 1

arr = [5, 3, 4, 7, 2, 9]
squareElements(arr)
