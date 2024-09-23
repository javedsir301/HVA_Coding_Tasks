age = int(input("Enter your Age: "))
if 0 <= age <= 2:
    print("Infant")
elif 3 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 65:
    print("Adult")
else:
    print("Senior")
