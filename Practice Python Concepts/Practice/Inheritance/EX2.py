class Person:#Super class / Parent Class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    #user-Defined Class
    def printName(self):
        print('My Name is',self.fname,self.lname)

class Student(Person): # 'Person' is the Parent Class
    def __init__(self,fname,lname):
        # Person.__init__(self,fname,lname) # Call the '__init__()' funtion of the parent class
        super().__init__(fname,lname) # Automatically pass the 'self' # Call the '__init__()' funtion of the parent class
        self.colour = 'Purple'



obj1 = Student('T.Dheeraj','Reddy') #Child class Object
# Access the properties of the Parent Class
print(obj1.fname,obj1.lname)
obj1.printName()
print(obj1.colour)