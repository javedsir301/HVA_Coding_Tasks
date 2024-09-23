a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    a, b = b, a
elif b > c:
    b, c = c, b
else:
    a, b = b, a

print(a, b, c)
