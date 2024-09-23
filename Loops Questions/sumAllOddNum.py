n = int(input("Enter the value of n: "))
start = 0
currentValue = 3
sum = 0
while start < n:
    sum += currentValue
    currentValue += 2
    start += 1
print(sum)
