# Append/Writting a file
f = open('E:\Deepak\python\File Handling\message.txt', 'a')
# append mode is also create file if file does not exist
# adn 'append' mode is write a file from last cursor(last line ends.)

f.write('hope')
f.write('pole')
f.write('DEEPAK')

print('Message Written')
f.close()