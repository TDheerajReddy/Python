# See below Wxample
# ** keyword arguments.
# a keyword argument consists of three elements: a "keyword" identifying the argument ('end' here); an equal sign (=); and a value assigned to that argument;
# any keyword arguments have to be put after the last positional argument (this is very important)


print("My name is", "Python.", end=" ")  # "end" keyword and equal to sign(=) and value assigned to it
print("Monty Python.")
"""
* As you can see, the end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments.

* The default behavior reflects the situation where the end keyword argument is implicitly used in the following way: end="\n".
"""

print()

# The "keyword argument" that can do this is named 'sep' (like separator).
#The print() function now uses a dash, instead of a space, to separate the outputted arguments.
#Note: the sep argument's value may be an empty string, too. Try it for yourself.
print("My", "name", "is", "Monty", "Python.", sep="-")
print()


# Mixed 'Keyword Aurgument'
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print()

#Test 1
print("Programming","Essentials","in",sep="***",end="...")
print("Python")
print()

#Test 2
print(" " * 3,"*")
print(" " * 2,"*","*")
print(" " * 1,"*"," " * 1,"*")
print(" " * 0,"*"," " * 3,"*")
print("*"*3," " * 1,"*"*3)
print(" "*1,"*"," "*1,"*\n"," "*0,"*"," "*1,"*")
print(" "*1,"*" * 5)