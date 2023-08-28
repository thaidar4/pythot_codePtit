strg = input()
res = ""
count = 0

strg = strg[::-1]
for i in strg:
    if count == 3:
        count = 0
        res += ","
    count += 1
    res += i

print(res[::-1])