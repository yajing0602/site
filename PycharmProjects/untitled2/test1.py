import requests
import re
def aa():
    url="http://10.9.17.250:8080/danglaoshi-web-app/user/login"
    datas={"deviceType":1,
           "password":"e10adc3949ba59abbe56e057f20f883e",
           "userName":"13100000213",
           "versionName":"3.3.6",
           "versionCode":77}
    response=requests.post(url,headers={"Content-Type": "application/json"},json=datas)
    print(response.text)
    sessionid = re.findall(r"\"sessionId\":\"(.*?)\",", response.text)
    userid = re.findall(r"\"userId\":\"(.*?)\",", response.text)
    print(sessionid)  # 正则表达式提取的值是个列表
    print(userid)
    return sessionid+userid  # 列表相加

p=aa()
print(p[0])
print(p[1])

#-----------------------------------------------------------------------

td ={'words_result': [{'words': '卡包/名片夹钥匙包/零钱包票证包皮具套装钱包'},
                      {'words': '公文包皮带电脑包双肩包单包拉杆箱旅行包'},
                      {'words': '洗漱包野餐包/登山包腰包/胸包/挎包帆布包'},
                      {'words': '太阳帽'}]}
a=""
list1=td.values()
for i in list1:
    for j in i:
        print(list(j.values()))                 # dict_values转换为list
        print("".join(list(j.values())))        # list转换为str
        a+="".join(list(j.values()))
print(a)

# a=""
# for i in td["words_result"]:
#        b=i["words"]
#        a+=b
# print(a)
