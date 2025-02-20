#       +, -, *, /, //, %, **           //Precedence Order
# Exponent = '**' in Python
print('Exponent :- ')
print(2 ** 3)       #if both operands are in Int then result is also in Int
print(2 ** 3.)      # if one of the operand are in Float then result is also in Float
print(2. ** 3)
print(2. ** 3.)

print('Multiplication :- ')
print(2 * 3)
print(2. * 3)

print('Division :- ')
print(6 / 3)
print(3 / 6)            # Result will be always in Float
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


print('Integer Division :- ')

"""
NOTE
Integer division can also be called floor division. You will definitely come across this term in the future.
"""

print(6 // 3)
print(6 // 3.)           # if one of the operand are in Float then result is also in Float

print(6 // 4)
print(6. // 4)           # The result is in Float but it doesn't give the exact ans, reason is below

"""
The result is two negative twos. The real (not rounded) result is -1.5 in both cases. However, the results are the subjects of rounding.
The rounding goes toward the 'lesser integer value', and the lesser integer value is -2, hence: -2 and -2.0.
"""
print(-6 // 4)
print(6. // -4)

print("Modulo/Remainder :- ")
print(14 % 4)
print(12 % 4.5)




"""
As you probably know, division by zero doesn't work.
Do not try to:-
perform a division by zero                      #print(6 / 0)
perform an integer division by zero             #print(6 // 0)
find a remainder of a division by zero.         #print(6 % 0)
"""

print('\nAddition :- ')
print(-4 + 4)
print(-4. + 8)                  #Binary
print(+2)                       #Unary

print('\nSubtraction :- ')
print(-4 - 4)
print(4. - 8)                   #Binary
print(-1.1)                     #Unary
"""
In subtracting applications, the minus operator expects two arguments: the left (a minuend in arithmetical terms) and right (a subtrahend).
"""

print('\nPrecedence :- ')
print(2 + 3 * 5)
print(9 % 6 % 2)                #left to right  (left-sided binding)
print(2 ** 2 ** 3)              #the exponentiation operator uses right-sided binding   (right to left).

print(2 * 3 % 5)        #1      # Both operators (* and %) have the same priority, so the result can be guessed only when you know the binding direction.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)      # 10.0


print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

