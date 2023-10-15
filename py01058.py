def prime(num):
    num = int(num) 
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True



for loop in range(int(input())):
    num = input()
    if prime(num[-4:]):
        print("YES")
    else: print("NO")
