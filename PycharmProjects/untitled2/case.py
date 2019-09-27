import requests
import unittest
import ddt
import warnings
from readdata1 import readExcel
from danglaoshimanager import TeacherManager
data1 = readExcel("C:\\Users\\TTT\\PycharmProjects\\untitled2\\data.xlsx","coursename1")
case1=data1.dict_data()
@ddt.ddt
class TestNewGoods(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.teachermanager=TeacherManager(s)
        warnings.simplefilter("ignore", ResourceWarning)
    #登录
    def test01_login(self):
        u'''测试后台登录'''
        result=self.teachermanager.login_manager()
        expected=result.json()["msg"]
        print(result.json())
        self.assertEqual(expected,"success")

    # 新建课程
    @ddt.data(*case1)
    @ddt.unpack
    def test02_new_course(self,coursename):
        u'''测试新建课程'''
        login_result = self.teachermanager.login_manager()
        token=self.teachermanager.get_token(login_result)
        result=self.teachermanager.create_course(token,coursename)
        expected=result.json()["msg"]
        self.assertEqual(expected,"success")


    #新建课时
    @ddt.data(*case1)
    @ddt.unpack
    def test03_newschedule(self,coursename):
        u'''测试新建课时'''
        result1=self.teachermanager.login_manager()
        token=self.teachermanager.get_token(result1)
        result2=self.teachermanager.create_course(token,coursename)
        courseid=self.teachermanager.get_courseid(result2)
        result=self.teachermanager.create_course_schedule(courseid,token)
        expected=result.json()["msg"]
        self.assertEqual(expected,"success")

    # 新建课时作业
    @ddt.data(*case1)
    @ddt.unpack
    def test04_creat_schedule_work(self,coursename):
        result1 = self.teachermanager.login_manager()
        token = self.teachermanager.get_token(result1)
        result2 = self.teachermanager.create_course(token,coursename)
        courseid = self.teachermanager.get_courseid(result2)
        result3= self.teachermanager.create_course_schedule(courseid,token)
        schedule_id=self.teachermanager.get_course_schedule_id(courseid,"course_6")
        result=self.teachermanager.create_schedule_work(token,schedule_id)
        expected=result.json()["msg"]
        self.assertEqual(expected,"success")


    def tearDown(self):
        pass
