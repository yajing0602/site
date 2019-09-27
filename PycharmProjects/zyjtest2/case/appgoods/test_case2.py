# import requests
# import unittest
# import warnings
# import re
# class TestApp(unittest.TestCase):
#     def setUp(self):
#         self.s = requests.session()
#         self.header ={"Content-Type": "application/json","sessionId" : "bf61bfa6-f040-41ed-bdc9-d8fbdc0acd4a","userId":"xW1p/SfQrRe="}
#         warnings.simplefilter("ignore", ResourceWarning)
#
#     #我的课程列表
#     def test_login_app(self):
#         u'''app我的课程列表'''
#         url="http://10.9.17.240:12600/api/celery/userCourse/list"
#         respnse=self.s.get(url,headers=self.header)
#         expected=respnse.json()["msg"]
#         print(respnse.text)
#         self.assertEqual(expected,"success")
#
#     #打开一个课程详情
#     def test_courseDetail(self):
#         u'''app我的课程详情'''
#         url="http://10.9.17.240:12600/api/celery/userCourse/list"
#         datas={"versionName":"3.3.5","password":"e10adc3949ba59abbe56e057f20f883e","deviceId":"1D1AFBDE-E81D-4FC2-96B3-4AB622CD0863","loginType":"0","deviceType":"2","userName":"13100000123","versionCode":"78"}
#         respnse=self.s.get(url,headers=self.header)
#         courseid = re.findall(r"\"courseId\":(\d+),",respnse.text)
#         url="http://10.9.17.240:12600/api/celery/userCourse/detail?courseId="+courseid[0]
#         respnse = self.s.get(url,headers=self.header)
#         expected = respnse.json()["msg"]
#         print(respnse.text)
#         self.assertEqual(expected,"success")
import requests
import unittest
import warnings
from base.danglaoshiapp import TeacherApp
class TestApp(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.teacherapp=TeacherApp(s)
        warnings.simplefilter("ignore",ResourceWarning)
    #登录App
    def test01_login_app(self):
        u'''测试登录app'''
        response=self.teacherapp.login_app("13100000213","e10adc3949ba59abbe56e057f20f883e")
        expected=response.json()["code"]
        self.assertEqual(expected,200)

    #我的课程列表
    def test02_mycourse(self):
        u'''app我的课程列表'''
        response1=self.teacherapp.login_app("13100000214","e10adc3949ba59abbe56e057f20f883e")
        siduid=self.teacherapp.get_sessionid_userid(response1)
        response=self.teacherapp.def_mycourse(siduid)
        expected=response.json()["msg"]
        print(response.text)
        self.assertEqual(expected,"success")


    #打开一个课程详情
    def test03_courseDetail(self):
        u'''app我的课程详情'''
        response1 = self.teacherapp.login_app("13100000215", "e10adc3949ba59abbe56e057f20f883e")
        siduid = self.teacherapp.get_sessionid_userid(response1)
        response2 = self.teacherapp.def_mycourse(siduid)
        courseid=self.teacherapp.get_courseid(response2)
        response=self.teacherapp.cousrse_detail(siduid,courseid)
        expected = response.json()["msg"]
        print(response.text)
        self.assertEqual(expected,"success")