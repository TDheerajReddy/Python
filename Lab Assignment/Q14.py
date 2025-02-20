# Armstrong number
n = int(input('Enter a Number: '))
n2 = n
temp = 0
p=len(str(n2))
while n!=0:
    remainder = n%10
    temp += (remainder**p)
    n //= 10

if n2 == temp:
    print(n2,'is a Armstrong Number')
else:
    print(n2,'is Not a Armstrong Number!!!')