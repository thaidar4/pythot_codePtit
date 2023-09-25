from math import gcd

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for loop in range(int(input())):
    num = int(input())
    primeNum = num % 10000
     
    if is_prime(primeNum):
        print("YES")
    else:
        print("NO")

