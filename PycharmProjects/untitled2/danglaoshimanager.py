import re
from domysql import MysqlUtil
class TeacherManager():
    def __init__(self,s):
        self.s=s
        self.header ={"Content-Type": "application/json"}

    #登录后台管理系统
    def login_manager(self):
        url="http://10.9.17.240:12500/manage/kzm/login"
        datas={"_t":1565855209660,"username":"13096995875","password":"123456","uuid":"0c850164-abfc-492d-8535-a173f455d6fc","captcha":"646556"}
        respnse=self.s.post(url,headers=self.header,json=datas)
        return respnse
    # 提取token
    def get_token(self,resonse):
        token=resonse.json()["data"]["token"] #通过字典取值提取到token值
        return token
    # 新建课程
    def create_course(self,tokens,coursename1):
        url = "http://10.9.17.240:12500/manage/celery/course/"
        self.header["token"] = tokens
        datas = {"id": "",
                 "name":coursename1,
                 "description": "",
                 "finishTime": "",
                 "subject": "1",
                 "level": "1",
                 "courseType": "0",
                 "examType": "1",
                 "haveServicePro": "0",
                 "scheduleWork": "0",
                 "startTime": 1569391200000,
                 "endTime": 1569398400000,
                 "expireTime": "",
                 "ascription": "1",
                 "scenes": "1",
                 "createTime": "",
                 "updateTime": "",
                 "createBy": "",
                 "updateBy": "",
                 "isGroup": "0",
                 "groupNum": "",
                 "scheduleNum": "",
                 "thumbImage": "http://dlsuser-test.oss-cn-beijing.aliyuncs.com/file-733a6cfbb4624dd68ffd3a0d57313f13.png",
                 "isScheduleGroup": "0",
                 "scheduleGroupNum": "",
                 "showClass": "0",
                 "viewClassNo": "0",
                 "jobProtect": "0"
                 }
        respnse=self.s.post(url,headers=self.header,json=datas)
        return respnse

    # 提取课程id
    def get_courseid(self,response):
        courseid = re.findall(r"\"data\":(\d+),",response.text)
        courseid = courseid[0]
        return courseid

    # 新建课时
    def create_course_schedule(self,courseid,tokens):
        url = "http://10.9.17.240:12500/manage/celery/courseschedule/"
        self.header["token"] = tokens
        datas = {"id": "",
                 "name": "course_6",
                 "startTime": 1569398400000,
                 "raiseHands": "0",
                 "endTime": 1569405600000,
                 "scene": 1,
                 "place": "",
                 "isTrial": "0",
                 "taskType": "0",
                 "description": "",
                 "createTime": "",
                 "createBy": "13096995875",
                 "updateTime": "",
                 "updateBy": "",
                 "supportType": 1,
                 "isScheduleGroup": "0",
                 "isLive": 1,
                 "isShowRedFlower": "0",
                 "courseId": courseid,  # 引用上一个接口提取的课程id（参数关联）
                 "videoKey": "",
                 "scenes": 1,
                 "teacherId": ""}
        respnse = self.s.post(url,headers=self.header,json=datas)
        return respnse

    #提取课时id
    def get_course_schedule_id(self,courseid,schedule_name):
        mysql = MysqlUtil()
        sql = "SELECT course_schedule_id FROM course_schedule_relation As A ,course_schedule As B  WHERE A.course_id="+courseid+" and  B.name='course_6' and A.course_schedule_id = B.id"
        schedule_id=mysql.mysql_getstring(sql)
        return  schedule_id

    #创建课时作业
    def create_schedule_work(self,tokens,schedule_id):
        url = "http://10.9.17.240:12500/manage/celery/courseexercise"
        self.header["token"] = tokens
        datas={
            "id":schedule_id,
            "courseId":0,
            "courseScheduleId":schedule_id,
            "title":"作业11",
            "startTime":1566203300374,
            "exerciseType":0,
            "createTime":1566203260000,
            "publishTime":1566203268000,
            "teacherId":"",
            "teacherName":"宋词",
            "state":1
            }
        response=self.s.post(url,headers=self.header,json=datas)
        return response