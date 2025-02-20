# Q5 input a Paragraph, count Vovels & Consonents and Number of Words

st = input('Enter a Paragraph : ')
s=st.lower()           # effect on original string

print(s)
#s1=set(s)       # set has not Duplicate letters
#print(s1)
#s=str(s1)
#print(s)
#countV = s.count('a') + s.count('e') +s.count('i') + s.count('o') + s.count('u')

vowels = ['a', 'e', 'i', 'o', 'u']
countV = 0
countC = 0

for x in s:
    if x in vowels:
        countV += 1
    elif x != ' ':
        countC += 1

print("Vowels: ", countV)
print("Consonants: ", countC)

# Count Number of Words
# default separator: space
result = len(s.split())     # Word count
print("There are",result,"words.")