#Q1
# import cmath
#x = int(input("Enter the number of Values : "))

#Calculator
a = int(input("Enter a value : "))
b = int(input("Enter a value : "))
i = input("Enter a operator : ")


def cal(i):
    if i == '+':
        print(a+b)
    elif i == '-':
        print(a-b)
    elif i == '*':
        print(a*b)
    elif i == '/':
        print(a/b)
    elif i == '//':
        print(a//b)
    elif i == '%':
        print(a%b)
    elif i == '**':
        print(a**b)
    else:
        print('Invalid Operator!!!')

cal(i)      #Function Call

# # complex numbers
# c = complex(a,b)
# print(c)
# print('Real part of Complex Number is :',c.real)
# print('Imaginary part of Complex Number is :',c.imag)
# #x = 2+3j
# #print(x)

# # Display Type of Variable
# print(type(c))

# # Doc string of Built-in Functions
# #print(dir(c))
# help(delattr)