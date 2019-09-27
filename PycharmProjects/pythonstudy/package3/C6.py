from package3.C5 import People
class Student(People):  # 继承People类
    def __init__(self,name,age,stuid,money):
        super(Student,self).__init__(name,age,money)  # 继承父类的构造方法，super是代表父类的一个关键字
        self.stuid = stuid  # 子类可以由一些自己独有的属性或者方法
    def set_stuid(self,stuid):
        self.stuid=stuid

    def do_homework(self):
        print("这是子类的作业")
        super(Student, self).do_homework() # super也可以调用构造方法以外的普通的方法