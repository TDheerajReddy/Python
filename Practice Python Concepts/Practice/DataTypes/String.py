str1= 'Hellow Dheeraj'
print(str1)
print()

# To see a list of all built-in functions
#print(dir(str1))
        #OR
#We can also apply 'dir()' function on data type
print(dir(type(str1)))
print()
#to see help text of a built-in function-
help('hash')

# To change the case
print(str1.upper())
print(str1.lower())
#Toogle Case
print(str1.swapcase())
print()
# Count instance of substring
print(str1.count('e'))

print(str1.find('e')) #Return index of first occurrence of seaching substring   //indexing starts from 0
print(str1.find('e',9)) #Search from 9th index value

#Replace
print(str1.replace('e','i',2))  # 2 is the number of substring

#Sort String
res = ''.join(sorted(str1))
print(res)