#Set
A={'a','s','c','d'}
B={'e','i','n','s','u','t'}
print('Set A : ',A,'\nSet B : ',B)
#Operations on Sets :-
#Difference
print(A - B)        #includes set 'A' values except Intersection Values
print(B - A)        #includes set 'B' values except Intersection Values

#Union
print(A | B)        # includes all Set 'A' and Set 'B' values without duplication.

#Intersection
print(A & B)        # includes only intersection/common values

#Symmetric Difference
print(A ^ B)        # includes all Set 'A' and Set 'B' values except Intersection values.


