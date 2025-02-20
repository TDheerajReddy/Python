try:
    # w = open('\hell.txt', 'w') # write to E: directory not in sub-folders
    w = open('hell.txt', 'w')
    w.write('SUCCESS1')
except: #I/O Error
    print('Can\'t write to the targetted file!!!')
else: # NOTE: 'else' is with 'except' block, not with 'if' block
    print('Can write in File.')
    w.write('SUCCESS2')     # Overrite
    # print('Can write in ROOT directory.')
    w.close()