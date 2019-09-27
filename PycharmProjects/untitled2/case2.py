import requests
import unittest
import warnings
from danglaoshiapp import TeacherApp
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