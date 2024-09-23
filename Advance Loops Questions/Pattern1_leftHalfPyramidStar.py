def leftHalfPyramidStar(n):
    i = 1
    while i <= n:
        print("*" * i)
        i += 1


n = int(input("Enter the value of n: "))
leftHalfPyramidStar(n)
