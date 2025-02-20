print(2+2)      #Addition
print(3-2);      '''Substraction'''
print(2*3)      #Multiplication
print(2**3)     #Power/Exponent
print(3/2)      #Floating point division
print(3//2)     #Integer/Floor division
print(3%2)      #Modulo / Modulus

x = 2 + 2j    #Complex Numbers,applicable for only j or J  OR x= 2+ 2J
print(x)
_ = 98
print(_)
print(_ + x)

x = 2e3     #Scientific Notation    OR x=2E3       Capital or Small
print(x)
i = 9
type(i)     #this command only run on python interpreter Tells the class name of variable
s ="hellow " + "Python"
print(s)
s ='"Python 1"'
print(s)
s ="'Python 2'"
print(s)
s ='Python 3'
print(s)

s = 'ha' * 7
print(s)
s = '7' * 7
print(s)

message = 'Namasthe'
name = 'Prakhar Saxena'
msg1 = 'pappu'
msg2 = 'ji'

print('{}! dear !{}'.format(name,message))      #below Python version 3.6
print('{2} {3} {1} {0}'.format(msg2, name, message, msg1))      #With index value, if many strings are there
print(f'{message} dear {name}')                 # 3.6 and above Python versions

#Multiple Assignments / Chain Assignment
x = y = z = 10
print(x,y,z)        #Comma defaultly put space