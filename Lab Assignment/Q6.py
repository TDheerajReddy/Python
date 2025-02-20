# Program to check if a number is prime or not
num = int(input('Enter a Number: '))

flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

# check if flag is True
if flag:
    print(num, "is NOT a Prime Number")
elif num == 1:
    print(num, "is NOT a Prime Number")
else:
    print(num, "is a Prime Number")