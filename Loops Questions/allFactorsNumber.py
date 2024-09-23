n = int(input("Enter the value of n: "))
start = 1
while start <= n:
    if n % start == 0:
        print(start, end=" ")
    start += 1
