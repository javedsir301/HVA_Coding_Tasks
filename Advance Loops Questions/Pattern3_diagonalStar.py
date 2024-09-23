def diagonalStar(n):
    i = 0
    while i < n:
        print(" " * i + "*")
        i += 1

n = int(input("Enter the value of n: "))
diagonalStar(n)
