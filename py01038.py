for loop in range(int(input())):
    
    num = int(input())

    if num % 7 != 0 :
        for i in range(1000):
            revNum = int(str(num)[::-1])
            num += revNum
            if num % 7 == 0:
                print(num)
                break
            else : 
                continue
            if i == 999 :
                print("-1")
    else : print(num)
            
