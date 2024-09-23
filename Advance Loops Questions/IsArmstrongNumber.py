def isArmstrongNumber(n):
    num_digits = 0
    temp = n
    while temp > 0:
        num_digits += 1
        temp = temp // 10

    sum_of_powers = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp = temp // 10

    if sum_of_powers == n:
        print("Yes")
    else:
        print("No")


n = int(input("Enter the Value of n : "))
isArmstrongNumber(n)
