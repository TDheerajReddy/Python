'''
*******
 *   *
  * *
   *
'''
n = int(input('Enter Number of Rows : '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(' ',end='')
    for j in range(1, 2*((n+1)-i-1) ):
        if j == 1 or j == 2*((n+1)-i-1)-1 or i == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print()