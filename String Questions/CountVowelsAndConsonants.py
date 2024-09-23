def countVowelsAndConsonants():
    str = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    vowelCount = 0
    consonantCount = 0
    index = 0
    
    while index < len(str):
        char = str[index]
        if char.isalpha():
            if char in vowels:
                vowelCount += 1
            else:
                consonantCount += 1
        index += 1
    
    print(vowelCount, consonantCount)

countVowelsAndConsonants()
