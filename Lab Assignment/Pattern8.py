'''
    5
   4 5
  3 4 5
 2 3 4 5
1 2 3 4 5
'''
n = 5
num = 6
for i in range(1,n+1):
    temp=num - 1
    num -= 1
    for j in range(1,(n+1)-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(temp,'',end='')
        temp += 1
    print()