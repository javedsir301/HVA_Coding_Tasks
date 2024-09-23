def reverseNumber(n):
    reversed_num = 0
    while n > 0:
        remainder = n % 10
        reversed_num = reversed_num * 10 + remainder
        n = n // 10
    print(reversed_num)

n = int(input("Enter the Value of n : "))
reverseNumber(n)
