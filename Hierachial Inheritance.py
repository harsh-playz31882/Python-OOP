class Person:
    def __init__(self, nm, ag):
        self.name=nm
        self.age=ag
    def show(self):
        print('This is person display method')


class Employee(Person):
    def __init__(self, nm, ag, sal):
        super.__init__(nm,ag)
        self.salary=sal
    def show2(self):
        print('This is Employee display method')

class Student(Person):
    def __init__(self,nm,ag,m):
        super.__init__(nm,ag)
        self.marks=m
    def show3(self):
        print('This is Student display method')

s1  = Student('Rohit', 21, 99)
e1 = Employee('Raj', 24, 50000)
p1 = Person('Ravi', 23)

s1.show3()
