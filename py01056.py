def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def evenOdd(num):
    for i in range(len(num)):
        if i % 2 == 0:  
            if int(num[i]) % 2 != 0:  
                return False
        else:  
            if int(num[i]) % 2 == 0: 
                return False
    return True

for loop in range(int(input())):
    num = input()

    sumNum = sum(int(digit) for digit in str(num))
    if prime(sumNum) and evenOdd(num):
        print("YES")
    else:
        print("NO")
