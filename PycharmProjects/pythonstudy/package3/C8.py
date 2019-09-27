# a=1
# b=0
# c=a/b          # 出现异常
# print("haha")  # 代码不会被执行

# a=1
# b=0
# try:
#     c=a/b
# except ZeroDivisionError :
#     print("除数不能为0")
# print("haha") # 抛出了异常，代码会被执行
#
#
# a=1
# b=0
# try:
#     c=a/b
#     print(c)
# except Exception as e:
#     print("除数不能为0")
#     print(e)  # division by zero
# else:
#     print("else语句")
# finally:
#     print("finally语句")
# print("haha") # 抛出了异常，代码会被执行

try:
    raise Exception("错误代码")
except Exception as e:  # 在python3.0中用as代替逗号
    print(e)

