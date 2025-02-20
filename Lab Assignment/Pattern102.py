#Q 21 Pattern

'''
   *
  * *
 * * *
* * * *
'''

def triangle(n):
    # number of spaces
    k = n - 1
    # outer loop to handle number of rows
    for r in range(0, n):
        for s in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k -= 1
        for b in range(0, r+1):         
            print("* ", end="")     
        print()

n =int(input('Enter number of Rows : '))
triangle(n)