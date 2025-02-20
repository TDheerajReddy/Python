##it will create a file automatically
# f = open('testFile1.txt','w')
# f.close()

# f = open('testFile2','a')
# f.close()

# f = open('testFile3.txt','x')
# f.close()


## for reading a File
# f = open('testFile1.txt','r')
# print(f.read())     # for read full file

# print(f.read(10))     # for read first 10 character from file

# print(f.readline())     # for reading one line only
# print(f.readline())     # for read second line, then repeate the line
# print(f.readline(5))     # for reading number of characters from current line only

# for x in f:                # Print all lines from the file
#     print(x)

# print(f.readlines())        # read all lines from the file and return in the form of the LIST
# f.close()                   # for close the file



## Append the file - Insering Data
# f = open('testFile1.txt','a')
# f.write('\nMy Best Friend is Somya & Prakhar.\nMy favorite colour is pink.\n')
# print('Data is Entered in the File.')
# f.close()
# f = open('testFile1.txt','r')
# for x in f:
#     print(x)
# f.close()




# Overwrite the flie
# f = open('testFile2','w')
# f.write('Hellow, My Name is T.Dheeraj Reddy.')
# print('Data is Overwitten in the File.')
# f.close()

# f = open('testFile2','r')
# print(f.read())
# f.close()




# Reading Image - Not Working
# f = open('Screenshot1.png','r')
# for x in f:
#     print(x)
# f.close()