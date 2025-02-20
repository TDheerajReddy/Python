# '__init__()' in-built funtion
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #user-Defined Class
    def myFunc(self):
        print('My Name is '+self.name)       # '+'can only concatenate str (not "int") to str
        print('My Age is',self.age)

obj1 = Person('Dheeraj',24)
print(obj1.name)
print(obj1.age)
obj1.myFunc()