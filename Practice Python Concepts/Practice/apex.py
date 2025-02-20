l1 = [1,2,3]
l2 = [6,7]
l1.append((7,8))        # takes exactly one argument
#l1.append(7,8)          # ERROR: takes exactly one argument
print(l1)

l1.extend(l2)
print(l1)