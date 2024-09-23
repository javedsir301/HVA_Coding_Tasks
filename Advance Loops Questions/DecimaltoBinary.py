def decimalToBinary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    print(binary)

decimal = int(input("Enter the Decimal Value: "))
decimalToBinary(decimal)
