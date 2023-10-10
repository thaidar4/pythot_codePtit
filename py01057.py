import math

def prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(math.sqrt(n))
    for i in range (5, sqr + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def check (n):
    for i in range(0, len(n)):
        tmp = ord(n[i]) - ord('0')
        if prime(i) and not prime(tmp):
            return False
        elif not prime(i) and prime(tmp):
            return False
    return True

for i in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
