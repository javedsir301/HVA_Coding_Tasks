a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print(maximum)


# a, b, c = map(int, input("Enter three numbers: ").split())
# print(max(a, b, c))



