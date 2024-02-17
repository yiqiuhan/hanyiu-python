class Student():
    #类属性，定义在类中，方法外的变量
    school="上海教育"

    def __init__(self,xm,nl):
        self.name=xm
        self.age=nl

    #定义在类中的函数，称为方法
    def show(self):
        print(f'my name is:{self.name},age is {self.age}')

    @staticmethod
    def sm():
        #print(self.name)
        print('这是一个静态方法，不能调用实例属性和方法')
              
    @classmethod
    def cm(cls):
        print('这是一个类方法，不能调用实例属性和方法')

#创建类方法
stu = Student(xm='han',nl=18)
#实例属性，使用对象名调用
print(stu.name,stu.age)
#类属性，直接使用类名
print(Student.school)

#实例方法，使用对象名打点调用
stu.show()

#直接使用类名调用cm和sm
Student.cm()
Student.sm()