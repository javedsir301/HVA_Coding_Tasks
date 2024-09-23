def isPrime(n):
    if n <= 1:
        print("No")
        return
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("No")
            return
        i += 1
    print("Yes")

n = int(input("Enter the value of n: "))
isPrime(n)
