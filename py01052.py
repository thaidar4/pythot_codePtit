def prime(num):
    if num < 2:
        return False
    for i in range(2 , int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for loop in range(int(input())):
    num = input()
    numSum = sum(int(digit) for digit in num if digit.isdigit())

    if prime(numSum):
        print("YES")
    else:
        print("NO")
