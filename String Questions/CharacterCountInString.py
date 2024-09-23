def countCharacter():
    str = input("Enter a string: ")
    chr = input("Enter the character to count: ")
    count = 0
    index = 0
    
    while index < len(str):
        if str[index] == chr:
            count += 1
        index += 1
    
    if count > 0:
        print(count)
    else:
        print("No")

countCharacter()
