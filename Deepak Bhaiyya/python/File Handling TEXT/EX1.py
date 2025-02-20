# Read a file
f = open('E:\Deepak\python\File Handling\message.txt') # if we don't mention the mode, then it will take the read mode
# f = open('message.txt')   # if the code and text file is in same folder, then we don't mention full path.
# print(f.read())
f.seek(1) #The seek() method sets the current file position/cursor in a file stream. / #The seek() method also returns the new postion.
# print(f.readline()) # only one line read, if we print multiple commands the it will print multiple lines.
# print(f.readline())
# print(f.readlines())  # retun in the list format
print(f.read())

f.close()