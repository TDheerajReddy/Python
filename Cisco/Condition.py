# The comparison (or the so-called relational) operators

# Example 1
print("Example 1")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

"""For One Line Instruction, Not for Multi Line Instruction -
Note: if any of the if-elif-else branches contains just one instruction, you may code it in a more comprehensive form (you don't need to make an
indented line after the keyword, but just continue the line after the colon).
"""
# Example 2
print("\nExample 2")
if number1 > number2: larger_number = number1
else: larger_number = number2
print("The larger number is:", larger_number)

# Example 3
# Read three numbers
print("\nExample 3")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

if number2 > largest_number:
    largest_number = number2
# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3
print("The largest number is:", largest_number)


# Read three numbers.
print("\n'max' built-in function")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
largest_number = max(number1, number2, number3)         # 'max' & 'min' is the Built-in function
smallest_number = min(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)
print("The smallest number is:", smallest_number)

# Lab 1
print('\nLab :-')
str = input('Enter a String: ')
if 'Spathiphyllum' == str:
    print("Yes - Spathiphyllum is the best plant ever!")
elif 'spathiphyllum' == str: 
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ",str)

# Lab 2


# Lab 3
year = int(input("Enter a year: "))	
if 1582 <= year:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print('Leap Year')
            else:
                print('Common Year')
        else:
            print('Leap Year')
    else:
        print('Common Year')
else:
    print('Not within the Gregorian calendar period')



# Exersise - 1
print('\nExersise 1 -')
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

# Exersise - 2
print('\nExersise 2 -')
x = "1"
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

# Exersise - 3
print('\nExersise 3 -')
x = 1
y = 1.0
z = "1"
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
