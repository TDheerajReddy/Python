# Print prime numbers in a given number
r1 = 2
r2 = int(input('Enter a number for Range: '))
for i in range(r1, r2+1):
    if i > 1:
        # check for factors
            for n in range(r1,i):
                if i == 2:
                    print(i)
                    break
                if (i%n) == 0:
                    break
            else:
                print(i)