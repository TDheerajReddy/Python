print('Equality :- ')       # the equal to operator (==)
print(2==2)
print(2==2.)    # Python is able to convert the integer value into its real equivalent, and consequently
print(1==2)

"""
The question will be as follows:

black_sheep == 2 * white_sheep


Due to the low priority of the == operator, the question shall be treated as equivalent to this one:

black_sheep == (2 * white_sheep)
"""


print()

var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)


print('\nInequality :- ')     # the not equal to operator (!=)
var = 0
print(var != 0)
var = 1
print(var != 0)

print('\nComparision Operator :- ')
print(' Greater Than -')
black_sheep = 4
white_sheep = 9
print(2 > 2.)               # Greater than
print(2 > 1)
print(black_sheep > white_sheep)

print('\n Less Than -')
print(2 < 2.)               # Less than
print(2 < 1)
var = black_sheep < white_sheep     # We can print this also , to use an arbitrary variable
print(var)

print('\n Greater than or Equal to -')
centigrade_outside = 1
print(centigrade_outside >= 0.0)        # Greater than or Equal to

print('\n Less than or Equal to -')     # Less than or Equal to
print(centigrade_outside <= 0.0)

# Lab
n = int(input())
print(not(n<100))       #do opposite of the operator, put 'not' keyword, This is 'Less Than' sign