# for-else Loop
L = [1,1,2,3,5,8,13,21]
for x in L:
    if x == 8:
        break # try 'continue' keyword also
    print(x)
else:
    print('Loop completely executed')