# display multiplication of a number and display upto that number
n = int(input('Enter a Number : '))
i=1
while i <= n:
    ans = n * i
    print(n,'X',i,'=',ans)
    i += 1