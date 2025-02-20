#List
# Negative Indexing is possible

li1 = ["Hellow",24,'Dheeraj',1998,4]
print(li1[2])
print(li1[-2])     # count from right side starts from  -1

print()
# Slicing
print(li1[:])      # or    print(list)     Print all elements
print(li1[0:2])

print()
#List can have another List

li2 = [4,[2,1,3],"D"]
print(li2)
print(type(li2))

print()

li3 = ['kGF','1','a','A',' ']
#To short a list
li3.sort(reverse=True)      # OR li3.sort(reverse=True) for decending order  //Sort must have same datatype
print(li3)

print()

li4 = li1 + li2         # OR print(li1 + li2)
print(li4)

print()

#To POP the last element from a List and displayed POP element //AND it effect the Original List
print(li4.pop())
print('li4 =',li4)

print()

#To append the List element at last of the List //AND it effect the Original List
li3.append(li1)
print('li3 = ',li3)

print()

#To extend the List element at
li5 = [1, 5, 10]; li6 = [3, 6, 9]
li5.extend(li6)
print(li5)

print()

#To Count occurence of a element in a List
print(li4.count(2))     # print(li4.count(4))

# Multiply List elements
print(li5 * 3)
a = [1,1,2] * 3         # multiply list 3 times like a string multiplication
print(a)        # OR print([1,1,2] * 3)
print()

# Slicing
li7 = [1,2,3,4,5,6,7,8,9]
#my_List[start:end:gap]
print('li7 =',li7[::])
print(li7[3:9])
print(li7[3:9:2])       # print every 2nd element
print(li7[3:9:3])       # print every 3rd element
print(li7[3:9:8])       # 4
print(li7[9:11])        # only blank brackets print
print(li7[:4])          # only 4 elements print
print(li7[::2])         # print every 2nd elementt
print(li7[::-1])        # print in reverse order
print(li7[::-3])        # print in reverse order and ever 3rd element print
print(li7[:1:-3])       # print to index value 1 in positive, but in reverse order
print(li7[1:1:1])       # only blank brackets print because its same
print(li7[0:1:-2])      # only blank brackets print # it reverse, but limit at index number 1

print()
x,y,z = [1,3,2]
print(x,y,z)

print(li7[:-4])         # print 0 to -4 in ascending order
