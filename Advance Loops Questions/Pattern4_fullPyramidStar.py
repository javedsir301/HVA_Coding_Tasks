def fullPyramidStar(n):
    i = 1
    while i <= n:
        print(" " * (n - i) + "*" * (2 * i - 1))
        i += 1

n = int(input("Enter the value of n: "))
fullPyramidStar(n)
