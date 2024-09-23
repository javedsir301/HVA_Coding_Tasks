def frequenciesOfEachElement(arr):
    freq = {}
    
    index = 0
    
    while index < len(arr):
        number = arr[index]
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
        index += 1
    
    index = 0
    allElements = set()
    
    while index < len(arr):
        number = arr[index]
        if number not in allElements:
            print(f"{number} {freq[number]}")
            allElements.add(number)
        index += 1

arr = [3, 6, 2, 1, 7, 3, 7, 4, 1, 7, 4]
frequenciesOfEachElement(arr)
