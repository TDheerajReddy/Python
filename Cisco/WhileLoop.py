# While Loop
"""while True:
    print("Hello Py")"""       #Press CTRL + C for "KeyboardInterrupt" exception

# Program 1 - 
print('\nProgram 1 - ')
largest_number = -999999999
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
# Print the largest number.
print("The largest number is:", largest_number)

# Program 2 - 
print('\nProgram 2 - ')
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
odd_numbers = 0
even_numbers = 0
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


# Program 3 - 
print('\nProgram 3 - ')
odd_numbers = 0
even_numbers = 0
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution.
while number:
    if number % 2:      # Check if the remainder  equal to 1
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Program 4 - 
print('\nProgram 4 - ')
counter = 5
while counter != -2:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# Program 5 - 
print('\nProgram 5 - ')
counter = 5
while counter:          # Check if the counter is equal to 0
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

