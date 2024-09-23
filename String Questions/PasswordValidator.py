def validatePassword():
    password = input("Enter a password: ")
    hasLower = False
    hasUpper = False
    hasDigit = False
    hasSpecial = False
    specialCharacters = "!@#$%^&*()-+=<>?/"
    
    index = 0
    while index < len(password):
        char = password[index]
        if char.islower():
            hasLower = True
        elif char.isupper():
            hasUpper = True
        elif char.isdigit():
            hasDigit = True
        elif char in specialCharacters:
            hasSpecial = True
        index += 1
    
    if (len(password) >= 8 and hasLower and hasUpper and hasDigit and hasSpecial):
        print("Yes")
    else:
        print("No")

validatePassword()
