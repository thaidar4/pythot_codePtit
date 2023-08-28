loop = int(input())

def check(num):
    digitList = [int(digit) for digit in str(num)]
    sumList = sum(digitList)
    found = True
    if sumList % 10 != 0:
        return False
    else:
        for i in range(0, len(digitList) - 1):
            if abs(digitList[i] - digitList[i + 1]) != 2:
                found = False
        return found  

while loop > 0:
    num = int(input()) 
    if check(num):
        print("YES")
    else:
        print("NO")
    loop -= 1
