#  print(b)  b在package2的A3中定义，此处直接使用会报错
  # 不同包中的模块的导入：导入package2中的A3
# import A2                #导入同一个包中的模块
# import package2.A3 as Y
# print(Y.b)
# print(A2.c)
# # print(package2.A3.b)

# from  package2.A3 import b
# print(b)
#
# from package2 import A3
# print(A3.b)
#
# a=1.35642
# b=round(a,3)
# print(b)  #输出1.356

# def add(a,b):
#     c=a+b
#     return c
#     print(a)
# result=add(1,2)
# print(result)

# def add(a,b,c):
#     return a,b,c
# p=add(1,2,3)

# print(p[0],p[1],p[2])
#
# p1,p2,p3=add(1,2,3)
# print(p1,p2,p3)

# a,b,c=1,2,3
# print(a,b,c) # 输出1 2 3

# d=1,2,3
# print(type(d))  # 输出<class 'tuple'>
# a,b,c=d
# print(a,b,c)    # 输出 1 2 3

#
# def add(x,y):
#     c=x+y
#     print(c)
#
# add(y=2,x=3)


def student(name,age,collage="西安邮电"):
    print("我叫"+name+",今年"+str(age)+",在"+collage+"上大学")

student("静静",30)             # 非默认参数必须传参
student("刚刚",29)            # 默认参数不传值，就取默认参数的值：我叫刚刚,今年29,在西安邮电上大学
student("乐乐",21,"人民大学")  # 默认参数传参，会修改函数中的默认参数值：我叫乐乐,今年21,在人民大学上大学
