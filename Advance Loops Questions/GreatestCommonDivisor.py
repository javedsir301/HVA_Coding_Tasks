def greatestCommonDivisor(firstNum, secondNum):
    while secondNum:
        firstNum, secondNum = secondNum, firstNum % secondNum
    print(firstNum)


firstNum = int(input("Enter the Value of First Number : "))
secondNum = int(input("Enter the Value of Second Number : "))
greatestCommonDivisor(firstNum, secondNum)
