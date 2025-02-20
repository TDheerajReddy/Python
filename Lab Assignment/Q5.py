#read a number and find sum of its digits
n = int(input('Enter a Number: '))
sum = 0
while n!=0:
    remainder = n%10
    sum += remainder
    n //= 10
print(sum)