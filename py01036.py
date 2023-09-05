for loop in range (1, int(input()) + 1):
    N = int(input())
    s = 0

    if N % 2 == 0:
        for i in range(2, N + 1, 2):
            s += 1 / i
    else:
        for i in range(1, N + 1, 2):
            s += 1 / i

    print(format(s, ".6f"))


