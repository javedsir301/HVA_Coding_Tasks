n = int(input("Enter the value of n: "))
start = 0
firstEvenNum = 2
while start < n:
    print(firstEvenNum, end=" ")
    firstEvenNum += 3
    start += 1
