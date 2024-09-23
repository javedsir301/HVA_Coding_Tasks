def leastCommonMultiple(firstNum, secondNum):
    gcd = firstNum
    while secondNum:
        gcd, secondNum = secondNum, gcd % secondNum
    lcm_Value = (firstNum * secondNum) // gcd
    print(lcm_Value)

firstNum = int(input("Enter the Value of First Number : "))
secondNum = int(input("Enter the Value of Second Number : "))
leastCommonMultiple(firstNum, secondNum)
