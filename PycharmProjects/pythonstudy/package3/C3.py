class Student():
    sum1=0
    name=""
    age=""
    def __init__(self,name1,age):
        self.name=name1          # 给对象变量赋值
        self.age=age

    def do_homework(self,work):
        work1=work
        print(str(self.age)+"岁的"+self.name+"做了"+work1+"作业！")

    @classmethod
    def add_sum(cls):  # cls代表当前类本身
        cls.sum1+=1    # 在类方法中修改类变量的值

    @staticmethod
    def add(x,y):
        c=x+y

student1=Student("乐乐",11)
Student.add_sum()   # 调用类方法
print("当前班级学生人数为：" + str(Student.sum1))
student2=Student("乐乐",11)
Student.add_sum()
print("当前班级学生人数为：" + str(Student.sum1))
