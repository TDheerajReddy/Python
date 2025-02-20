# List Operations
myList = [1,2,3,'RealMe','is the best']
li1 = ['7i',8,'8i']
myList2 = ['h','k','a','A','k']
myList3 = [3,5,7,9,1]

#append - add a single value at end of list
print('\nappend() method :- ')
myList.append(6)
myList.append('i')
myList.append(['i',2])
myList.append(6j)   # Complex Number
myList.append(li1)   # append list
print(myList)

# extend - add multiple values at end of list
print('\nextend() method :- ')
myList.extend([5,2,'str'])
print(myList)

print('\ninsert() method :- ')
myList.insert(1,'10')     # syntax -  li.insert(position,element)
print(myList)

print('\nremove() method :- ')
myList.remove('i') # syntax - li.remove(value)    
myList.remove(['i',2]) # syntax - li.remove(value)    

print(myList)

print('\npop() method :- ')
myList.pop()        # pop element from last
print(myList.pop())
myList.pop(3)       # pop element from index value
print(myList)       # syntax - li.pop(index)

print('\nreverse() method :- ')
myList.reverse() # syntax - li.reverse()  - it effects the original list
print(myList)

print('\nmax() method :- ')     # applied on same homogeneous(similar) type data/value
print(max(myList2),max(myList3))

print('\nmin() method :- ')
print(min(myList2),min(myList3))

print('\ncount() method :- ')
print(myList2.count('k'))

print('\nindex() method :- ')
print(myList)
print(myList.index(6j))         # syntax - myList.index(value)
#print(myList.index(0,0,'s'))

print('\nsort() method :- ')    # applied on same homogeneous(similar) type data/value      # effect on original string
myList2.sort()
print(myList2)
myList3.sort(reverse=True)      # syntax - list.sort(reverse=True|False, key=Fun)  key - Optional. A function to specify the sorting criteria(s)
print(myList3)

print('\nclear() method :- ')
myList3.clear()                 # clear the list, effect on original list
print(myList3)

print('\nsplit() method :- ')
mL = ['Sachin', 'Ramesh', 'Tendulkar']
print(mL[0][0] +'.'+mL[1][0] + ' '+mL[2])


