n = int(input("Enter the value of n: "))
start = 1
currentEvenNum = 2
while start <= n:
    print(currentEvenNum, end=" ")
    currentEvenNum += 2
    start += 1
