com=0 
cop=0  
while(1):
    num = int(input("Enter the number"))
    if (num!=-1):
        con=0
        for a in range(2,num):
            if num%a==0:
                con+=1
        if con>=1:
            print(num, "is Composite Number")
            com+=1
        else:
            print(num, "is Prime Number")
            cop+=1
    else:
        break
print("total number of prime numbers:",cop)
print("total number of composite numbers:",com)