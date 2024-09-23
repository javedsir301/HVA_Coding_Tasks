n = int(input("Enter the value of n: "))
start = 1
factorial = 1
while start <= n:
    factorial *= start
    start += 1
print(factorial)
