number = input()
digits = [int(digit) for digit in number]
a = len(digits) - 1

while a >= 1:
    if digits[a] >= 5:
        digits[a-1] += 1
    digits[a] = 0
    a -= 1

new_number = int(''.join(map(str, digits)))
print(new_number)