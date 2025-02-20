#import math
ls=[]
def fun(*numbers):
    for number in numbers:
        if(number.isnumeric()):
            ls.append(number)
        else:
            print(number," is not a number")
fun('4','1','6','9','8','hello')
'''
#print(ls)
#ls=list(set(ls))
'''
ls.sort()
print(ls)
print("second largest element is",ls[-2])