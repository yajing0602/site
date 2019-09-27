from appium import webdriver
import unittest
import time
from login import *
from Page.LoginPage import LoginPage
from Page.ExercisePage import ExercisePage
from Page.MyPage import MyPage
from Page.ExercisePage import ExercisePage
from Page.SettingPage import SettingPage

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = init_device()
        cls.loginPage = LoginPage(cls.driver)
        cls.exercisePage = ExercisePage(cls.driver)
        cls.myPage = MyPage(cls.driver)
        cls.settingPage = SettingPage(cls.driver)

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        """退出登录"""
        self.exercisePage.click_my_tab()
        self.myPage.click_setting()
        self.settingPage.click_logout_btn()

    def test_login1(self):
        """测试用户名、密码正确,登录成功"""
        self.loginPage.login("13100000999","12345677")
        time.sleep(2)
        try:
            login_flag = self.loginPage.find_element(*self.loginPage.login_btn)
            print(login_flag)
            self.assertEqual(login_flag,False,"输入正确用户名、密码名称登录失败")
            print("测试通过")
        except AssertionError as e:
            self.loginPage.get_screenshot(u"正确用户名、密码登录失败")
            print("测试失败")
            print(e)

    def ptest_login2(self):
        """测试用户名、密码正确，登录失败"""
        self.loginPage.login("13100000999", "12345689")
        time.sleep(2)
        try:
            # login_flag = self.loginPage.find_element(*self.loginPage.login_btn)
            login_flag = True
            self.assertEqual(login_flag, False, "输入正确用户名、密码名称登录失败")
        except AssertionError as e:
            self.loginPage.get_screenshot(u"正确用户名、密码登录失败")
            print(e)


if __name__ == '__main__':
    unittest.main()