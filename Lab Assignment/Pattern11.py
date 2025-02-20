

'''
    *
   ***
  *****
 *******
*********
'''
n = int(input('Enter Number of Rows : '))
for i in range(1,n+1):
    for j in range(1,(n+1)-i):
        print(' ',end='')
    for j in range(0,(2*i)-1):
    #       OR
    #for j in range(1,((2*i)+1)-1):
        print('*',end='')
    print()