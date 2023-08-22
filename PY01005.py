

num = input()
numList = list(num)
count = 0


for check in numList:
    if check == '4' or check == '7':
        count += 1

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
