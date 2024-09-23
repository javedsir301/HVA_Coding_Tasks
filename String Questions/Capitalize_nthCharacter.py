def capitalize_nth():
    s = input("Enter a string: ")
    n = int(input("Enter the index of the character to capitalize: "))
    
    if 0 <= n < len(s):
        s = s[:n] + s[n].upper() + s[n+1:]
        print(s)
    else:
        print("Index out of range")

capitalize_nth()
