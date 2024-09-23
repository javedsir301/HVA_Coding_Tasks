def removeDuplicates():
    str = input("Enter a string: ")
    result = ""
    index = 0
    
    while index < len(str):
        if str[index] not in result:
            result += str[index]
        index += 1
    
    print(result)

removeDuplicates()
