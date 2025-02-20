# read a list of numbers and divide into even and odd list
li = list( map( int, input('Enter Series of Random Numbers : ').split()))
evenList = list()
oddList = list()
for i in li:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print('Even List\t:\t',evenList)
print('Odd List\t:\t',oddList)