'''
A
BB
CCC
DDDD
EEEEE
'''
n = int(input('Enter Number of Rows : '))
c = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(c),end='')
    c = c + 1
    print()