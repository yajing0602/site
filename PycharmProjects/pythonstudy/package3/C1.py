class Student():
    sum1=0
    name="nike"   # 定义类变量name和age
    age="20"
    def __init__(self,name1,age):
        self.name=name1   # 定义实例变量通过self.name来定义；并进行初始化
        self.age=age
        print(self.name)  # 输出：乐乐
        print(self.__class__.sum1)  # 打印类变量sum1的值
        print(Student.sum1)         # 打印类变量sum1的值

    def do_homework(self,work):
        work1=work
        print(str(self.age)+"岁的"+self.name+"做了"+work1+"作业！")

student1=Student("乐乐",11)
print(Student.sum1)
print(Student.sum1)
