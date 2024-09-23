import math

def isPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def firstPerfectSquare(arr):
    index = 0
    
    while index < len(arr):
        try:
            number = arr[index]
            sqrt = int(math.sqrt(number))
            perfect_square = sqrt * sqrt == number
        except:
            perfect_square = False
        
        if perfect_square:
            print(number)
            return
        
        index += 1
    
    print("No")


arr=[2,4,1,7,8]
firstPerfectSquare(arr)