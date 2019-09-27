class Student():
    sum1=0
    name=""
    age=""
    def __init__(self,name1,age):
        self.name=name1          # 给对象变量赋值
        self.age=age
        self.__score=0

    def do_homework(self):
        self.do_english_homework() # 实例方法内部调用
        print(str(self.age)+"岁的"+self.name+"做了"+self.work+"作业！")
    def do_english_homework(self):
        self.work="英语"
    def __dafen(self,score):
        if score<0:   # 在方法中可以对用户输入的值进行校验，提高安全性
            return "分数不能是负数"
        self.__score=score
        return self.__score

student1=Student("乐乐",11)
student2=Student("毛毛",12)
# result=student1.dafen(100)  # 要修改对象变量的值，需要使用方法修改，才能提高安全性
student1.__score=-1      # 此处相当于给student1增加了一个实例变量__score,并不是调用私有属性，所以打印不报错
print(student1.__score)  # 输出-1，不报错，因为student1有__score这个变量
# print(student2.__score)  # 报错，因为student2没有自己的变量__score，所以调用的__score就是类中的私有属性，所以会报错
print(student1.__dict__)  # {'name': '乐乐', 'age': 11, '_Student__score': 0, '__score': -1}
print(student2.__dict__)  # {'name': '毛毛', 'age': 12, '_Student__score': 0}


