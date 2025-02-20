# map Function :- apply same function/operation to all elements of a iterative object.
def multiplyByTwo(number):
    return(number*2)
number = [1,2,3,4,5,16,7,8,9,10]
print(list(map(multiplyByTwo, number)))