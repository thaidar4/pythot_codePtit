for loop in range(int(input())):
    num = input()
    numSum = sum(int(digit) for digit in num if digit.isdigit())

    if str(numSum) == str(numSum)[::-1] and numSum > 9:
        print("YES")
    else:
        print("NO")
