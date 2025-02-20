'''
    A
   A B
  A B C
 A B C D
A B C D E
'''
n = int(input('Enter Number of Rows : '))
for i in range(1,n+1):
    c = 65
    for j in range(1,(n+1)-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(c),'',end='')
        c += 1
    print()