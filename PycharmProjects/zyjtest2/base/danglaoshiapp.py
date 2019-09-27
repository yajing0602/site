import  re
import random
class TeacherApp():
    def __init__(self,s):
        self.s=s
        self.header = {"Content-Type": "application/json"}

    def login_app(self,username,password):
        url="http://10.9.17.250:8080/danglaoshi-web-app/user/login"
        datas={"deviceType":1,
               "password":password,
               "userName":username,
               "versionName":"3.3.6",
               "versionCode":77}
        response=self.s.post(url,headers=self.header,json=datas)
        return  response


    def get_sessionid_userid(self,response):
        sessionid=re.findall(r"\"sessionId\":\"(.*?)\",",response.text) # 正则表达式提取出来的值时列表
        userid=re.findall(r"\"userId\":\"(.*?)\",",response.text)
        return sessionid+userid  #列表相加还是列表


    def def_mycourse(self,siduid):
        sessionid=siduid[0]
        print(sessionid)
        userid=siduid[1]
        print(userid)
        self.header["sessionId"]=sessionid
        self.header["userId"]=userid
        url="http://10.9.17.240:12600/api/celery/userCourse/list"
        response=self.s.get(url,headers=self.header)
        return response

    def get_courseid(self,response):
        courseid = re.findall(r"\"courseId\":(\d+),", response.text)
        return  courseid  #返回装有课程id的列表

    def cousrse_detail(self,siduid,couserid1):
        sessionid=siduid[0]
        userid=siduid[1]
        self.header["sessionId"]=sessionid
        self.header["userId"]=userid
        courseid=random.choice(couserid1)  #随机获取列表中的一个值
        url = "http://10.9.17.240:12600/api/celery/userCourse/detail?courseId="+courseid
        response = self.s.get(url,headers=self.header)
        return response