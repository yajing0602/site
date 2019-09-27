import requests
import re
class NewGoods():
    s = requests.session()
    header ={"Content-Type": "application/json"}
    #登录
    def login(self):
        url="http://10.9.17.240:12500/manage/kzm/login"
        # header={"Content-Type":"application/json"}
        datas={"_t":1565855209660,"username":"13096995875","password":"123456","uuid":"0c850164-abfc-492d-8535-a173f455d6fc","captcha":"646556"}
        respnse=self.s.post(url,headers=self.header,json=datas)
        print(respnse.json())
        self.token=respnse.json()["data"]["token"] #通过字典取值提取到token值
        return respnse.json()["msg"]


    #新建课程
    def new_course(self):
        tokens=self.token
        print(tokens)
        url="http://10.9.17.240:12500/manage/celery/course/"
        # header={"Content-Type":"application/json","token":tokens}
        self.header["token"]=tokens
        datas={"id":"",
        "name":"ZYJ_0919_我的课程UI优化02",
        "description":"",
        "finishTime":"",
        "subject":"1",
        "level":"1",
        "courseType":"0",
        "examType":"1",
        "haveServicePro":"0",
        "scheduleWork":"0",
        "startTime":1568959200000,
        "endTime":1569736800000,
        "expireTime":"",
        "ascription":"1",
        "scenes":"1",
        "createTime":"",
        "updateTime":"",
        "createBy":"",
        "updateBy":"",
        "isGroup":"0",
        "groupNum":"",
        "scheduleNum":"",
        "thumbImage":"http://dlsuser-test.oss-cn-beijing.aliyuncs.com/file-733a6cfbb4624dd68ffd3a0d57313f13.png",
        "isScheduleGroup":"0",
        "scheduleGroupNum":"",
        "showClass":"0",
        "viewClassNo":"0",
        "jobProtect":"0"
        }
        respnse = self.s.post(url,headers=self.header,json=datas)
        print(respnse.text)
        #正则表达式提取字符串中的课程id
        courseid=re.findall(r"\"data\":(\d+),",respnse.text)
        print(courseid[0])
        return courseid[0]  # 返回课程id
    #新建课时
    def newschedule(self,courseids):
        tokens = self.token
        self.courseid=courseids
        url = "http://10.9.17.240:12500/manage/celery/courseschedule/"
        # header = {"Content-Type": "application/json", "token": tokens}
        self.header["token"] = tokens
        datas={"id":"",
        "name":"course_6",
        "startTime":1568959200000,
        "raiseHands":"0",
        "endTime":1568966400000,
        "scene":1,
        "place":"",
        "isTrial":"0",
        "taskType":"0",
        "description":"",
        "createTime":"",
        "createBy":"13096995875",
        "updateTime":"",
        "updateBy":"",
        "supportType":1,
        "isScheduleGroup":"0",
        "isLive":1,
        "isShowRedFlower":"0",
        "courseId":self.courseid, #引用上一个接口提取的课程id（参数关联）
        "videoKey":"",
        "scenes":1,
        "teacherId":""}
        respnse = self.s.post(url,headers=self.header,json=datas)
        print(respnse.text)






newgoods=NewGoods()
newgoods.login()
couserids=newgoods.new_course()
newgoods.newschedule(couserids)
