from math import gcd

def prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for loop in range(int(input())):
    num = input()
    numList = [int(digit) for digit in str(num)]

    count = 0
    for i in numList:
        if (prime(i)):
            count += 1
    if count >= len(str(num))/2 and prime(len(str(num))):
        print("YES")
    else:
        print("NO")
