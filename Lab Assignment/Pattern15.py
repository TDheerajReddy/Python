

'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
n = int(input('Enter Number of Rows : '))
for i in range(1,n+1):
    num = 5
    for j in range(1,(n+2)-i):
        print(num,'',end='')
        num -= 1
    print()