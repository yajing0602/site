# import requests
# import unittest
# import warnings
# import re
# class TestNewGoods(unittest.TestCase):
#     def setUp(self):
#         self.s = requests.session()
#         self.header ={"Content-Type": "application/json"}
#         warnings.simplefilter("ignore", ResourceWarning)
#     #登录
#     def test_login(self):
#         u'''测试后台登录'''
#         url="http://10.9.17.240:12500/manage/kzm/login"
#         datas={"_t":1565855209660,"username":"13096995875","password":"123456","uuid":"0c850164-abfc-492d-8535-a173f455d6fc","captcha":"646556"}
#         respnse=self.s.post(url,headers=self.header,json=datas)
#         expected=respnse.json()["msg"]
#         print(respnse.json())
#         self.assertEqual(expected,"success")
#
#     # 新建课程
#     def test_new_course(self):
#         #登录
#         u'''测试新建课程'''
#         url = "http://10.9.17.240:12500/manage/kzm/login"
#         datas = {"_t": 1565855209660, "username": "13096995875", "password": "123456",
#                  "uuid": "0c850164-abfc-492d-8535-a173f455d6fc", "captcha": "646556"}
#         respnse=self.s.post(url, headers=self.header, json=datas)
#         self.token=respnse.json()["data"]["token"] #通过字典取值提取到token值
#         tokens=self.token
#
#         #新建课程
#         url="http://10.9.17.240:12500/manage/celery/course/"
#         self.header["token"]=tokens
#         datas={"id":"",
#         "name":"ZYJ_0919_我的课程UI优化02",
#         "description":"",
#         "finishTime":"",
#         "subject":"1",
#         "level":"1",
#         "courseType":"0",
#         "examType":"1",
#         "haveServicePro":"0",
#         "scheduleWork":"0",
#         "startTime":1568959200000,
#         "endTime":1569736800000,
#         "expireTime":"",
#         "ascription":"1",
#         "scenes":"1",
#         "createTime":"",
#         "updateTime":"",
#         "createBy":"",
#         "updateBy":"",
#         "isGroup":"0",
#         "groupNum":"",
#         "scheduleNum":"",
#         "thumbImage":"http://dlsuser-test.oss-cn-beijing.aliyuncs.com/file-733a6cfbb4624dd68ffd3a0d57313f13.png",
#         "isScheduleGroup":"0",
#         "scheduleGroupNum":"",
#         "showClass":"0",
#         "viewClassNo":"0",
#         "jobProtect":"0"
#         }
#         respnse = self.s.post(url,headers=self.header,json=datas)
#         expected=respnse.json()["msg"]
#         self.assertEqual(expected,"success")
#
#
#
#     #新建课时
#     def test_newschedule(self):
#         u'''测试新建课时'''
#         #登录
#         url = "http://10.9.17.240:12500/manage/kzm/login"
#         datas = {"_t": 1565855209660, "username": "13096995875", "password": "123456",
#                  "uuid": "0c850164-abfc-492d-8535-a173f455d6fc", "captcha": "646556"}
#         respnse = self.s.post(url, headers=self.header, json=datas)
#         self.token = respnse.json()["data"]["token"]  # 通过字典取值提取到token值
#         tokens = self.token
#         #新建课程
#         url = "http://10.9.17.240:12500/manage/celery/course/"
#         self.header["token"] = tokens
#         datas = {"id": "",
#                  "name": "ZYJ_0919_我的课程UI优化02",
#                  "description": "",
#                  "finishTime": "",
#                  "subject": "1",
#                  "level": "1",
#                  "courseType": "0",
#                  "examType": "1",
#                  "haveServicePro": "0",
#                  "scheduleWork": "0",
#                  "startTime": 1568959200000,
#                  "endTime": 1569736800000,
#                  "expireTime": "",
#                  "ascription": "1",
#                  "scenes": "1",
#                  "createTime": "",
#                  "updateTime": "",
#                  "createBy": "",
#                  "updateBy": "",
#                  "isGroup": "0",
#                  "groupNum": "",
#                  "scheduleNum": "",
#                  "thumbImage": "http://dlsuser-test.oss-cn-beijing.aliyuncs.com/file-733a6cfbb4624dd68ffd3a0d57313f13.png",
#                  "isScheduleGroup": "0",
#                  "scheduleGroupNum": "",
#                  "showClass": "0",
#                  "viewClassNo": "0",
#                  "jobProtect": "0"
#                  }
#         respnse = self.s.post(url, headers=self.header, json=datas)
#         # 正则表达式提取字符串中的课程id
#         courseid=re.findall(r"\"data\":(\d+),",respnse.text)
#         self.courseid=courseid[0]
#
#         #新建课时
#         url = "http://10.9.17.240:12500/manage/celery/courseschedule/"
#         # header = {"Content-Type": "application/json", "token": tokens}
#         self.header["token"] = tokens
#         datas={"id":"",
#         "name":"course_6",
#         "startTime":1568959200000,
#         "raiseHands":"0",
#         "endTime":1568966400000,
#         "scene":1,
#         "place":"",
#         "isTrial":"0",
#         "taskType":"0",
#         "description":"",
#         "createTime":"",
#         "createBy":"13096995875",
#         "updateTime":"",
#         "updateBy":"",
#         "supportType":1,
#         "isScheduleGroup":"0",
#         "isLive":1,
#         "isShowRedFlower":"0",
#         "courseId":self.courseid, #引用上一个接口提取的课程id（参数关联）
#         "videoKey":"",
#         "scenes":1,
#         "teacherId":""}
#         respnse = self.s.post(url,headers=self.header,json=datas)
#         expected=respnse.json()["msg"]
#         self.assertEqual(expected,"success")
#
#
#     def tearDown(self):
#         pass
import requests
import unittest
import ddt
import warnings
from comm.read_token import get_token

from base.danglaoshimanager import TeacherManager
from comm.readdata1 import readExcel
data1 = readExcel("C:\\Users\\TTT\\PycharmProjects\\zyjtest1\\comm\data.xlsx","coursename1")
case1=data1.dict_data()
data2 = readExcel("C:\\Users\\TTT\\PycharmProjects\\zyjtest1\\comm\\data.xlsx","schedulename1")
case2=data2.dict_data()

@ddt.ddt
class TestNewGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token=get_token()
        print("当前token值",cls.token)

    def setUp(self):
        s = requests.session()
        self.teachermanager=TeacherManager(s)
        warnings.simplefilter("ignore",ResourceWarning)

    # 新建课程
    @ddt.data(*case1)
    @ddt.unpack
    def test02_new_course(self,coursename):
        u'''测试新建课程'''
        result=self.teachermanager.create_course(self.token,coursename)
        expected=result.json()["msg"]
        self.assertEqual(expected,"success")


    #新建课时
    @ddt.data(*case2)
    @ddt.unpack
    def test03_newschedule(self,schedulename):
        u'''测试新建课时'''
        result2=self.teachermanager.create_course(self.token,"自动化课程00")
        courseid=self.teachermanager.get_courseid(result2)
        result=self.teachermanager.create_course_schedule(courseid,schedulename,self.token)
        expected=result.json()["msg"]
        self.assertEqual(expected,"success")

    # 新建课时作业
    # @ddt.data(*case1)
    # @ddt.unpack
    def test04_creat_schedule_work(self):
        result2 = self.teachermanager.create_course(self.token,"自动化课程10")
        courseid = self.teachermanager.get_courseid(result2)
        result3= self.teachermanager.create_course_schedule(courseid,"course_6",self.token)
        schedule_id=self.teachermanager.get_course_schedule_id(courseid,"course_6")
        result=self.teachermanager.create_schedule_work(self.token,schedule_id)
        expected=result.json()["msg"]
        self.assertEqual(expected,"success")


    def tearDown(self):
        pass
