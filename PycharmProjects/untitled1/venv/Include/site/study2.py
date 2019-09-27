# if False:
#     pass
# else:
#     print("ok")
#     print("hao")

# for i in range(0,10,2):
#     print(i)            # 换行输出
#     print(i, end="")    # 不换行输出
#     print(i, end="|")   # 不换行输出，每个字符之间用|隔开

# for j in range(10,0,-2):
#     print(j,end=",")  # 输出 10,8,6,4,2,

a=[1,2,0,4,5,6,7,8,9]
for i in range(0,len(a),2):
    print(a[i],end="|")