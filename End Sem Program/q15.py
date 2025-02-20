# Find greatest number
a = float(input('enter First number:  '))
b = float(input('enter second number:  '))
c = float(input('enter third number:  '))
if(a>b) and (a>c):
    print("First number is greater")
elif(b>a) and (b>c):
    print("Second number is greater")
else:
    print("Third number is greater")