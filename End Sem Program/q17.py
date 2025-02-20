# Find entered value in what type
num = input("Please Enter a string :")
if((num >= 'a' and num <= 'z') or (num >= 'A' and num <= 'Z')): 
    print("The Given word is an Alphabet") 
elif(num >= '0' and num <= '9'):
    print("The Given word is a Digit")
else:
    print("The Given word is a Special Character")