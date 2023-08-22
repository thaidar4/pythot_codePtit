loop = int(input())
while loop > 0:

    num = input()
    numList = list(num)
    count = 0


    for check in numList:
        if check == '4' or check == '7':
            count += 1

    if count == len(numList):
        print("YES")
    else:
        print("NO")
    loop -= 1