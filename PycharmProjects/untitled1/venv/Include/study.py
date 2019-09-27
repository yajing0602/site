# print(2/2)   # 1.0   单斜杠自动转换为float
# print(1/2)   # 0.5
# print(2//2)  # 1     双斜杠取整
# print(1//2)  # 0
# print(1%2)   # 1     百分号取余
# print("hello"+"world")   #输出helloworld
# print("hello"*3)         #输出hellohellohello
# s='hello我'
# print(len(s))            #输出 6
# print(s[5])              #输出 我
# print(s[0:-3])
# s="hello python java c# ruby"
# print(s[-4::])  #输出 ruby

# a= [1,2.333,True,'aaaa',(1,'hello',0.7,),[(1, 2),{2, 4}],{1,3,4}]
# a.append("zyj")
# print(a)  # [1, 2.333, True, 'aaaa', (1, 'hello', 0.7), [(1, 2), {2, 4}], {1, 3, 4}, 'zyj']


# a= [1,2.333,True,'aaaa',(1,'hello',0.7,),[(1, 2),{2, 4}],{1,3,4}]
# a.insert(1,"zyj")
# print(a)  #[1, 'zyj', 2.333, True, 'aaaa', (1, 'hello', 0.7), [(1, 2), {2, 4}], {1, 3, 4}]

# a= [1,2.333,True,'aaaa',(1,'hello',0.7,),[(1, 2),{2, 4}],{1,3,4}]
# a[-1]="zyj"  #修改下标为-1位置的值为"zyj"
# print(a)  # [1, 2.333, True, 'aaaa', (1, 'hello', 0.7), [(1, 2), {2, 4}], 'zyj']

# a= [1,2.333,True,'aaaa',(1,'hello',0.7,),[(1, 2),{2, 4}],{1,3,4}]
# a.pop()   # 删除最后一个元素
# print(a)  # [1, 2.333, True, 'aaaa', (1, 'hello', 0.7), [(1, 2), {2, 4}]]
# a.pop(1)  # 删除下标为1的元素
# print(a)  # [1, True, 'aaaa', (1, 'hello', 0.7), [(1, 2), {2, 4}]]

# c = [2, 4, 5, 7, 9, 0]
# print(max(c))  # 输出列表最大值 9
# print(min(c))  # 输出列表最小值 0
# c.reverse()    # 倒置输出
# print(c)       # [0, 9, 7, 5, 4, 2]
# c.sort()       # 从小到大排序
# print(c)       # [0, 2, 4, 5, 7, 9]
# c.clear()      # 清空列表中的元素，变为空列表
# print(c)       # []

a=3
b=a
a=1
print(b)  # 3

a=[1,3,5]
b=a
a[0]=False
b[1]=True
print(b)  # [False, True, 5]
print(a)  # [False, True, 5]
