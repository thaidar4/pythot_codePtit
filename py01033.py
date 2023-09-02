import math
import itertools

def checkGcd(start, end):
    numList = list(range(start, end+1))
    combinations = itertools.combinations(numList, 3)

    for combination in combinations:
        a, b, c = combination
        if math.gcd(a, b) == math.gcd(b, c) == math.gcd(c, a) == 1:
            print(combination)

start, end = map(int, input().split())
checkGcd(start, end)
