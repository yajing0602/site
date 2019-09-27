class People():
    sum=0
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.__money=money  # 私有属性，被引入时，继承不了，但他们的set，get函数可以继承

    def get_money(self):
        return self.__money

    def set_money(self,money):
        self.__money=money

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def do_homework(self):
        print("这是父类的作业")