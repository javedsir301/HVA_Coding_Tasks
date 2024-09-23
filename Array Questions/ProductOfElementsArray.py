def productOfElements(arr):
    product = 1
    index = 0
    while index < len(arr):
        product *= arr[index]
        index += 1
    print(product)

arr = [3, 2, 5, 1, 4]
productOfElements(arr)
