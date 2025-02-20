def sum(n):
    return lambda x: x+n
o1=sum(4)
print(o1(4))

o2=sum(3)
print(o2(4))