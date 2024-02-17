class Student():
    #类属性，定义在类中，方法外的变量
    school="上海教育"

    def __init__(self,xm,nl):
        self.name=xm
        self.age=nl

    #定义在类中的函数，称为方法
    def show(self):
        print(f'my name is:{self.name},age is {self.age}')

stu=Student(xm='han',nl=18)
stu2=Student(xm='han1',nl=181)

#动态绑定属性
stu.gender="男"
print(stu.name,stu.age,stu.gender)

#动态绑定方法
def introduce():
    print("我是一个动态方法")
stu2.fun=introduce
stu2.fun()

stu.show()

lst=[stu,stu2]
for item in lst:
    item.show()