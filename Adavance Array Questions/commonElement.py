def commonElementInArray(arr1, arr2):
    commonElements = []
    i = 0
    j = 0
    arr1.sort()
    arr2.sort()

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            # arr1[i] == arr2[j]
            if arr1[i] not in commonElements:
                commonElements.append(arr1[i])
            i += 1
            j += 1
    
    return commonElements

arr1 = [3, 4, 5, 6, 7]
arr2 = [4, 8, 9, 1, 2, 3]
res = commonElementInArray(arr1, arr2)
print(res) 
