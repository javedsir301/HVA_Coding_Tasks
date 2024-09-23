def isPerfectNumber(n):
    sumOfDivisors = 0
    i = 1
    while i <= n // 2:
        if n % i == 0:
            sumOfDivisors += i
        i += 1
    if sumOfDivisors == n:
        print("Yes")
    else:
        print("No")

n = int(input("Enter the Value of n : "))
isPerfectNumber(n)