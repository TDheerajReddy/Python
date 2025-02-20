# Writting a file
f = open('E:\Deepak\python\File Handling\message.txt', 'w') # clear previouse data and then it will write.
# write mode is also create file if file does not exist
f.write('YoY\n123456789\nasdfghj\n')
f.write('pool')
f.seek(6)
f.write('DEEPAK')
print('Message Written')
f.close()