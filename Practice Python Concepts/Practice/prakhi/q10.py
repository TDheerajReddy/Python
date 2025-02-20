# read list of integer from user
# display the count of occurence of each number
#create 2 new list containing the even or odd numbers from the original list
l=[]
l2 = []
l3 = []

n=int(input("please enter number of values in list="))
for i in range (n):
    ele=int(input())
    l.append(ele)
print(l)

print(l.count(5))

for i in range (n):
    print(l.count(l[i]))

for i in l:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
print(l2)
print(l3)