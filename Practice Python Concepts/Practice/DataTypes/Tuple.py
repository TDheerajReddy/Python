# Tuple - 
T1 = ('a',1, 2, 3.5,'D')
print(T1[0])
print(T1[-1])       # Negative Indexing is possible

# Slicing
print(T1[1:3])
print(T1[:])       #OR print(T1) Access all data from Tuple


# Multiply Tuple elements
print(T1 * 3)

#To Count occurence of a element in a Tuple
print(T1.count('d'))
print()

# Methods showing of specific data type
print(dir(T1))
print()
print(type(T1))
print()

#print(help('help'))
#print(help('add'))

#Unpacking of Tuple
f, x, y , z , l = T1
print(f, l, x, y, z)
f, *y, l = T1
print(f, l, y)
print(f, l, *y)

print(T1.index('D'))

string = "geeksforgeeks" 
T2 = tuple(string)
print(T2)

#NOT a tuple it is a string
thistuple = ("apple")
print(type(thistuple))
thistuple = ("banana",)
print(type(thistuple))
thistuple = "banana",
print(type(thistuple))

#tuple1 = tuple(1)       # TypeError: 'int' object is not iterable       # tuple constructor
#print(tuple1)


# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')
# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])    #my_tuple[start:end:gap]

print(my_tuple[::-6])    #my_tuple[start : end : gap]


# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])     #my_tuple[start:end:gap]


