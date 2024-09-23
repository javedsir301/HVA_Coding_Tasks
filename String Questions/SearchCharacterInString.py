def searchCharacter():
    str = input("Enter a string: ")
    chr = input("Enter the character to search for: ")
    index = 0
    
    while index < len(str):
        if str[index] == chr:
            print("Yes")
            return
        index += 1
    
    print("No")

searchCharacter()
