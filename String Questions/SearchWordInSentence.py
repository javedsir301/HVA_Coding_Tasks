def searchWord():
    sentence = input("Enter a sentence: ")
    word = input("Enter the word to search for: ")
    words = sentence.split()
    index = 0
    
    while index < len(words):
        if words[index] == word:
            print("Yes")
            return
        index += 1
    
    print("No")

searchWord()
