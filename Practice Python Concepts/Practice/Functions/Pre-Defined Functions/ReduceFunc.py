from functools import reduce    #Import this function, it is depricated since python 3
#reduce function:
'''
    The reduce (fun,seq) function is used to apply a particular
    function passed in its argument to all of the list
    elements mentioned in the sequence passed along.
'''
number = [1,12,3,14,5,16,7,18,9,20]
def addition(number1, number2) :
    return number1 + number2
R = reduce(addition,number)         #Syntax :- reduce(<function>,<iteraterable Object>) return reduced single value
print(R)