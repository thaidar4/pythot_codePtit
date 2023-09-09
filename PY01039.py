def solve(n):
    if n[0] == n[1]:
        return "NO"
    for i in range(2, len(n)):
        if n[i] != n[i % 2]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = list(input())
    print(solve(n))
