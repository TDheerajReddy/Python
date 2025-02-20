'''
    E
   D E
  C D E
 B C D E
A B C D E
'''
n = 5
num = 65 + 5
for i in range(1,n+1):
    temp=num - 1
    num -= 1
    for j in range(1,(n+1)-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(temp),'',end='')
        temp += 1
    print()