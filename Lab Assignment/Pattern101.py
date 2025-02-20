#Q 7 Pattern
'''
*
* *
*   *
*     *
*********

n = 5
'''

def triangle(n):
    for i in range(n):
        # printing spaces
       

        # printing stars
        for k in range(2 * i + 1):
            # print star at start and end of the row
            if k == 0 or k == 2 * i:
                print('*', end='')
            else:
                if i == n - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()

n =int(input('Enter number of Rows : '))
triangle(n)