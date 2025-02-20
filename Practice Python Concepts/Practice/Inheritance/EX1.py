class Person:#Super class / Parent Class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    #user-Defined Class
    def printName(self):
        print('My Name is',self.fname,self.lname)

class Student(Person): # 'Person' is the Parent Class # No '__init__()' functionof child class
    pass


obj1 = Student('T.Dheeraj','Reddy') #Child class Object
# Access the properties of the Parent Class
print(obj1.fname,obj1.lname)
obj1.printName()