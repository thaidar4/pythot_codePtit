
loop = int(input())

while loop > 0:
    num = int(input())
    letterList = list(str(num))
    count = 1
    for i in range(len(letterList) - 1):
        if letterList[i] > letterList[i+1] :
            break
        count += 1

    if count == len(letterList):
        print("YES")
    else :
        print("NO")
    loop -= 1