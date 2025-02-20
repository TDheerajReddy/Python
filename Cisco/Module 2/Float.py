print(.4)       # We can write this also for '0.4
print(4.)       # We can write this also for '4.0'
print(0.4)
print(-4.)
print(300000000)
print(3E8)              # 'e' OR 'E' for exponential, '8' for 8 zeros =  3 x 10⁸ 

"""
Note:
* the exponent (the value after the E) has to be an integer
* the base (the value in front of the E) may be an integer.
"""

print(6.62607E-34)      #A physical constant called "Planck's constant" (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34

"""
Note: the fact that you've chosen one of the possible forms of coding float values doesn't mean that Python will present it the same way.

Python may sometimes choose different notation than you.


For example, let's say you've decided to use the following float literal:

0.0000000000000000000001

When you run this literal through Python:
"""
print(0.0000000000000000000001)     #the result is 1e-22
# Python always chooses the more economical form of the number's presentation, and you should take this into consideration when creating literals.