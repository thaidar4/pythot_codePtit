def count(num):
    num = str(num)  
    sum = 0 
    product = 1
    check0 = False
    for i in range(len(num)):
        if i % 2 == 0:  
            sum += int(num[i])
        elif  i % 2 != 0 and int(num[i]) != 0: 
            product *= int(num[i])
            check0 = True
        
    if check0 == False :
        product = 0
    print (sum , product)
    


for loop in range(int(input())):
    num = input()
    count(num)
