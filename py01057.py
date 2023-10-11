def prime(num):
    num = int(num) 
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check(num):
    temp = 0
    for i in range(len(num)):
        if prime(i) == prime(num[i]):
            temp = 1
        else:
            temp = 0
            break
    if temp == 0: return False
    else : return True


for loop in range(int(input())):
    num = input()
    if check(num):
        print("YES")
    else: print("NO")
