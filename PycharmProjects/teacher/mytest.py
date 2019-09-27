from appium import webdriver
from login import *
import unittest
driver = None
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = init_device()
        login(driver,'13100000999','123456')

    def setUp(self):
        pass

    def tearDown(self):
        """返回主页"""
        global driver
        driver.press_keycode(4)

    def test_kecheng_desc_fail(self):
        """测试课程详情页-课程介绍对不上"""
        global driver
        title,price = check_kecheng(driver)
        title_des = find_title_desc(driver).get_attribute("text")
        price_des = find_price_desc(driver).get_attribute("text")
        introduce = find_introduce_desc(driver).get_attribute("text")
        self.assertEqual(introduce,"课程绍","课程介绍控件有误")
        self.assertEqual(title_des,title,"课程标题有误")
        self.assertEqual(price_des,price,"课程价格有误")

    def test_kecheng_desc_pass(self):
        """测试课程详情页-课程介绍能对上"""
        global driver
        title,price = check_kecheng(driver)
        title_des = find_title_desc(driver).get_attribute("text")
        price_des = find_price_desc(driver).get_attribute("text")
        introduce = find_introduce_desc(driver).get_attribute("text")
        self.assertEqual(introduce,"课程介绍","课程介绍控件有误")
        self.assertEqual(title_des,title,"课程标题有误")
        self.assertEqual(price_des,price,"课程价格有误")


if __name__ == '__main__':
    unittest.main()