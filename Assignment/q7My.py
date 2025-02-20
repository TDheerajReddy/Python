def myFunc(args):
    args[2]=9

l = [4,'6','7',2]
T = (4,'6','7',2)
myFunc(l)
print(l)
print(type(l))
print(type(T))
#myFunc(T)      #immutable
# print(T)