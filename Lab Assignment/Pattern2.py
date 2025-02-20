'''
A
AB
ABC
ABCD
ABCDE
'''
n = int(input('Enter Number of Rows : '))
for i in range(1,n+1):
    c = 65
    for j in range(1,i+1):
        print(chr(c),end='')
        c = c + 1
    print()