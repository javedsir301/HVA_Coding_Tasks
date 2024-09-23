def fibonacciSeries(n):
    firstNum, nextNum = 0, 1
    count = 0
    while count < n:
        print(firstNum, end=" ")
        firstNum, nextNum = nextNum, firstNum + nextNum
        count += 1

n = int(input("Enter the Value of n : "))
fibonacciSeries(n)
