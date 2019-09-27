from package3.C1 import Student
student1=Student("乐乐",11)
student1.do_homework("数学")
student2=Student("毛毛",12)
student2.do_homework("语文")
print(student1.name)  # 打印对象student1的属性name：乐乐
print(student2.name)  # 打印对象student2的属性name：毛毛
print(Student.name)   # 打印类 Student 的属性 name：nike
print(Student.__dict__) # 打印类的所有的变量