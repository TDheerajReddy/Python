# var1 = input()
# var2 = input('Enter a String: ')
# print("var1 =",var1)
# print("var2 = ",var2)           #It can concatenate the string OR real numbers with comma

# """
# anything = input("Enter a number: ")
# something = anything ** 2.0         #we must not use it as an argument of any arithmetic operation
# print(anything, "to the power of 2 is", something)
# """

# #Type Casting - Strings to Real Numbers
# anything = int(input("Enter a number: "))     #To convert string to Integer Or Float we use 'int()' OR 'float()' for Type Casting
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

#Type Casting - Real Numbers to Strings
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))           #It can print whole answer in decimal point


# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# # hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)


# #Concatenate the Strings '+'
# fname = input("May I have your first name, please? ")
# lname = input("May I have your last name, please? ")
# str1 = fname + lname
# print("Thank you.")
# print("\nYour name is " + fname + " " + lname + ".")
# print("\nYour name is ", str1)
# print("\nYour name is "+ str1)                      #See the difference b/w three


# #Replication '*'
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

#Lab-1
# input a float value for variable a here
# var1 = float(input('Enter a Number : '))
# # input a float value for variable b here
# var2 = float(input('Enter a Number : '))

# print('Addition = '+str(var1 + var2))
# print('Substraction = '+str(var1 - var2))
# print('Multiplication = '+str(var1 * var2))
# print('Diviion ='+str(var1 / var2))
# print("\nThat's all, folks!")

#Lab-2
# x = float(input("Enter value for x: "))
# y = 1/(x + 1/(x + 1/(x + 1/(x) ) ) )
# print("y =", y)

#Lab-3
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mins = mins + dura # find a total of all minutes
# hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
# mins = mins % 60 # correct minutes to fall in the (0..59) range
# hour = hour % 24 # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')

#Exercise 1
# x = int(input("Enter a number: ")) # The user enters 2
# print(x * "5")

#Exercise 2
x = input("Enter a number: ") # The user enters 2, 'input()' function takes String by default
ST=type(x)
print(ST)      