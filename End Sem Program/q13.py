# Area of Triangle by herons formula
a = float(input('Please Enter the First side of "a" Triangle: '))
b = float(input('Please Enter the Second side of "b" Triangle: '))
c = float(input('Please Enter the Third side of "c" Triangle: '))
s = (a + b + c) / 2
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(" The Area of a Triangle is %0.2f"%Area)