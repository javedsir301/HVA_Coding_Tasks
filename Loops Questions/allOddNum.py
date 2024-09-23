n = int(input("Enter the value of n: "))
firstOddNum = 1
currentOddValue = 1
while firstOddNum <= n:
    print(currentOddValue, end=" ")
    currentOddValue += 2
    firstOddNum += 1
