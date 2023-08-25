loop = int(input())

while loop > 0 :
    strg = input()
    strgList = []
    i = 0

    while i < len(strg):
        if strg[i].isalpha():
            strgList.append(strg[i])
            Char = strg[i]
        else:
            Char_repeat = Char * int(strg[i])
            strgList.append(Char_repeat)
            strgList.remove(Char)
        i +=1

    strgResult = "".join(strgList)
    print(strgResult)

    loop -= 1