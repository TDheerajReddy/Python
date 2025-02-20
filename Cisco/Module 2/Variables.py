var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
#print(Var)         #It is not a case-sensitive, cause an error
print(var)

print()
V = "3.8.5"
print("Python version: " + V)   #Only string variable is concatenate      #You can use the print() function and combine text and variables using the '+' operator to output strings and variables

print()
var = 1
var = var + 1       #Assigning new values
print(var)

print()
var = 100
var = 200 + 300     #Assigning new values
print(var)

print()
"""
the length of the hypotenuse (i.e., the longest side of a right-angled triangle, the one opposite of the right angle) using the Pythagorean theorem.
(2.4.1.6)
"""
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5        # We use ** instead of square root.
print("c =", c)             #Only string variable is concatenate

#Lab-1
print()

john = 3
mary = 5
adam = 6
print(john,',',mary,',',adam)
total_apples = john + mary + adam
print("Total number of apples:",total_apples)

print()
var = 4
x = 4
i = 4
j = 4
rem = 4
x *= 2          #variable = variable op expression  ➡    variable op= expression
print('x = ',x)
i += 2 * j
var /= 2
rem %= 10
j -= (i + var + rem)
x **= 2
print('i = ',i
    ,'\nvar = ',var
    ,'\nrem = ',rem
    ,'\nj = ',j
    ,'\nx = ',x)


#Lab-2
    #   1 mile is equal to approximately 1.61 kilometers
print()
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 3), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Lab-3
    #evaluate the following expression:     3x3 - 2x2 + 3x - 1
print()
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)


#Exercise-2
    # my_var
    # m
    # 101
    # averylongvariablename
    # m101
    # m 101
    # Del
    # del
"""
All are errors
"""

#Exercise-3
print()
a = '1'
b = "1"
print(a + b)