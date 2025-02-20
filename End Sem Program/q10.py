l=[12,75,150,145,180,525,50]
for i in range(len(l)):
   if l[i]>500:
       break
   elif l[i]>150:
       continue
   elif l[i]%5==0:
       print("number divisiable by 5",l[i])