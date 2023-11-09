n = input()
line = [0] * 15

def permu(s):
    if len(s) == len(n):
        print(s)
        return
    for i in range(len(n)):
        if line[i] == 0:
            line[i] = 1
            permu(s + n[i])
            line[i] = 0

permu('')
