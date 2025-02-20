#Read a file
# E:\Deepak\python\File Handling\message.txt
f = open('E:\Deepak\python\File Handling\message.txt', 'r') 
# read mode is not creating a file if file does not exist

# print(f.read())
# print(f.readline()) # only read one line
# print(f.readline(5)) # read the 5 character of a line including space.
# print(f.readline())
# print(f.readline())
# print(f.readlines())

for x in f: # Read the file through loop.
    print(x)

# f.write('pool') # Error read does not support write() function

f.close()
