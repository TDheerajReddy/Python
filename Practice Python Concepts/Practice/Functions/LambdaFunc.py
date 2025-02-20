#Lambda Function / Anonymous Function :- it has no name, for small funtions
#Syntax :- lambda <argument>:<expresion/condition>
L = [1,12,3,14,5,16,7,18,9,20]

l = list(filter(lambda number:number%2 != 1, L))                #Through filter() function
print(l)

#Read a list
x = list((map(lambda number: int(number),input('Enter list elements : \n').split())))       #Through map() function
print(x)

print('\n====================================================================================================\n')
def myfun(n):
    return lambda a : a*n

double_fun=myfun(2)     #Sequence 1
triple_fun=myfun(3)     #Sequence 2
print(double_fun(9))    #Sequence 1
print(triple_fun(4))    #Sequence 2


