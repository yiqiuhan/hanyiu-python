class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'我叫：{self.name}，我今年{self.age}岁')

class Student(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender

class Doctor(Person):
    def __init__(self,name,age,dep):
        super().__init__(name,age)
        self.dep=dep

stu=Student(name='han',age=18,gender="男")
stu.show()


doctor=Doctor(name="shen",age=20,dep="yangpu")


doctor.show()