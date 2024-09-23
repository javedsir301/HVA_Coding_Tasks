def first_nPrimeNumbers(n):
    count = 0
    num = 2
    while count < n:
        isPrime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                isPrime = False
                break
            i += 1
        if isPrime:
            print(num, end=" ")
            count += 1
        num += 1


n = int(input("Enter the Value of n : "))
first_nPrimeNumbers(n)
