# Dictionary - Collection of key-value pairs
# Indexing by it's KEY
D1 = {1:'Dheeraj', 2:5.6, 3 : "XYZ", 4 : [1, 3, 5]}
print(D1)
print(D1[3],'\n')

D2 = {  'name' : 'Dheeraj',
        'Age' : 24, 
        'Subjects': ['Competetive C++','ADBMS','AWS','R-Programming','Python']
    }
print(D2)
print(D2['Subjects'])
print(type(D2))

print(D2.keys())
print(D2.values())

del D2['Age']       #Delete key
print('\n"Age" Key Deleted\n')
print(D2.keys())
#print(D2['Age'])
print('Age' in D2)      # Syntax :- <key> in Dict_Name
print('Subjects' in D2)

