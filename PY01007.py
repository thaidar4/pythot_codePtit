import math

loop = int(input())

while loop > 0 :
    strInput = input()
    numList = [float(num) for num in strInput.split()]
    
    if 0 < numList[0] < numList[2] < 100000:
        t = math.log(numList[2] / numList[0]) / math.log(1 + numList[1]/100)
        t = math.ceil(t)
    print(t)
    loop -= 1