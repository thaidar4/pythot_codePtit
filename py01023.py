from collections import Counter

def prime(num):
    primeList = []
    i = 2

    while num > 1:
        if num % i == 0:
            primeList.append(i)
            num /= i
        else:
            i += 1

    return primeList

def convert(nums):
    counter = Counter(nums)
    result = []
    for num, count in counter.items():
        result.append(f"{num}^{count}")
    return " * ".join(result)

for loop in range(int(input())):
    num = int(input())
    primeList = prime(num)
    setFormat = convert(primeList)
    print('1 * '+setFormat)