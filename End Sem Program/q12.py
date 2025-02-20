#write a progaram to the number is checker prime,even,odd and composite
def evenodd(eo):
    if(eo%2 == 0):
       print(eo,"number is even")
    else:
       print(eo,"number is odd")
    
def prime(p):
    count=0
    for a in range(2,p):
        if p%a==0:
            count+=1
    if count>=1:
        print(p, "is Composite Number")
    else:
        print(p, "is Prime Number")

n = int(input("Enter a number to check : "))
evenodd(n)
prime(n)