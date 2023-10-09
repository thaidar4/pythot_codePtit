def cal(num):
    res = 1
    for digit in str(num):
        if digit != '0':
            res *= int(digit)
    return res

for loop in range(int(input())):
    num = input()
    print(cal(num))
