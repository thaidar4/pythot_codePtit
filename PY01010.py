loop = int (input())


while(loop > 0 and loop <= 20):
    string = input()
    soSanh = []
    
    if len(string) >= 4 and len(string) <= 18:
        soSanh.append(string[:2])  
        soSanh.append(string[-2:]) 

    if soSanh[0] == soSanh[1]:
        print("YES")
    else:
        print("NO")
    
    loop -= 1
