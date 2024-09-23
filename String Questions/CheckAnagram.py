def checkAnagram():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    def clean_string(str):
        return ''.join([ch.lower() for ch in str if ch.isalpha()])
    
    str1_clean = clean_string(str1)
    str2_clean = clean_string(str2)
    
    if sorted(str1_clean) == sorted(str2_clean):
        print("Yes")
    else:
        print("No")

checkAnagram()
