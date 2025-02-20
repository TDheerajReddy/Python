# To read/ take input String from User
name = input("Enter yuour name : ")
# To read/ take input Integer and Other datatype from User
Integer = int(input("Enter your age : "))

print(f'Hellow {name}')
print("Your Age is ",Integer)

r,s = list(map(float,input("enter radius and side ").split()))      # multiple inputs with one input function
print("Radius of circle",r)
print("side of square",s)
a1=3.14*r*r 
a2=s*s
print("area of circle",a1)
print("area of square",a2)