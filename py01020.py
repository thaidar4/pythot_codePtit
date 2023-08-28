loop = int(input())

while loop > 0:
    num = str(input())
    check =[]
    check.append(num[-2:])
    if check[0] == '86':
        print('YES')
    else:
        print("NO")
    loop-= 1
