def firstRepeatElement(arr):
    present = set()
    index = 0
    while index < len(arr):
        number = arr[index]
        if number in present:
            return number
        present.add(number)
        index += 1
    return "No"

arr = [5, 11, 4, 7, 8, 4, 6, 11, 7]
res=firstRepeatElement(arr)
print(res) 
