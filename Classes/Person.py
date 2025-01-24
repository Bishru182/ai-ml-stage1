class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print("my name:",self.name)
        print("age:",self.age)

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def func(self):
        print("student's name:",self.name)
        print("student's id:",self.id)