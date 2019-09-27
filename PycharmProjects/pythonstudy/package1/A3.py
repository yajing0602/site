class Student():
    name="joy"
    age=10
    def base(self):    # 类里面所有的方法第一个参数都是self
        print("name:"+self.name)  # 调用类的变量时，用self.
        print("age:"+str(self.age)) # self代表实例对象本身

