from package3.C6 import Student

student1=Student("毛毛",28,11,1111)
print(student1.name)
student1.set_name("兔兔")
print(student1.get_name())
student1.set_stuid(1000)
print(student1.stuid)
student1.set_money(123)  # 调用父类方法修改私有变量
print(student1.get_money())
print(student1.__dict__)
student1.do_homework()   # 如果子类和父类的方法名完全一样，就会先调子类的方法