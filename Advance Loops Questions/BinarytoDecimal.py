def binaryToDecimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        remainder = binary % 10
        decimal += remainder * (2 ** power)
        binary = binary // 10
        power += 1
    print(decimal)

binary = int(input("Enter the Binary Value: "))
binaryToDecimal(binary)
