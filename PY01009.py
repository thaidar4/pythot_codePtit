string = str(input())
upCount = 0
lowCount = 0

for char in string:
    if char.isupper():
        upCount += 1
    elif char.islower():
        lowCount += 1

if lowCount >= upCount :
    string = string.lower()
else:
    string = string.upper()

print(string)