#write a progaram to check the number is palindrome or not 
def palindromecheker(m):
    temp=m
    rev=0

    while(m>0):
        deg=m%10
        rev=rev*10+deg
        m=m//10

    if(temp==rev):
        print("number is PALINDROME : ",rev)
    else:
        print("number is NOT Palindrome : ",rev)

n=int(input("Enter a number : "))
palindromecheker(n)