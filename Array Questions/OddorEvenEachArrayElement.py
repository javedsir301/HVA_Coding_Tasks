def oddOrEven(arr):
    index = 0
    while index < len(arr):
        number = arr[index]
        print("Odd" * (number % 2) + "Even" * (1 - number % 2))
        index += 1

arr = [4, 7, 9, 10, 13, 17]
oddOrEven(arr)
