

'''
A B C D E
A B C D
A B C
A B
A 
'''
n = int(input('Enter Number of Rows : '))
for i in range(1,n+1):
    c = 65
    for j in range(1,(n+2)-i):
        print(chr(c),'',end='')
        c += 1
    print()