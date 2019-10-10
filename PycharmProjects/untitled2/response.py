import requests
import  re
url = "http://10.9.17.240:12600/api/celery/courseSchedule/list?courseId=2812"
header ={"Content-Type": "application/json","sessionId":"f1213e01-e282-4df8-949c-1af2394c5a7a","userOrgId":"n/gVxHpel5q="}
response=requests.get(url,headers=header)

# 返回结果是字符串类型
print(response.text)
print(type(response.text))
# 字符串类型要通过正则表达式去提取,返回结果是列表
msg=re.findall("\"msg\":\"(.*?)\",",response.text)
print(msg)
result=msg[0]
print(result)

# 返回结果是字节类型
print(response.content)
print(type(response.content))
# 将字节转换为字符串，再通过正则提取
responsetext=str(response.content, encoding='utf-8')
print(responsetext)

# 返回结果是dict
print(response.json())
print(type(response.json()))
# 通过json串提取
print(response.json()["msg"])
