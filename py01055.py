def check_conditions(num):
    if len(num) % 2 != 0:
        if num[0] != num[1]:
            even_digits = num[::2]
            if all(digit == even_digits[0] for digit in even_digits):
                return True
    return False

for loop in range(int(input())):
    num = input()
    if check_conditions(num):
        print("YES")
    else: print("NO")
