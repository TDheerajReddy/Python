#Q3 Indexing Positive, Negative & Slicing

l1 = [5,1,15,9,4,10,6,12,7,14]
#l[start:end:gap]
# Positive Indexing
print(l1[3])
# Negative Indexing
print(l1[::-4])
print(l1[:-4:])
print(l1[-4::])
print(l1[-4::-1])
print(l1[-4])

print()

#Slicing
print(l1[:])
print(l1[2:7])

print(l1[1:9:2])        # print every second element


