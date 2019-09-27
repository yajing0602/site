from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class BasePage:
    def __init__(self,driver):
        self.driver = driver


    def find_element(self, *loc):  # *loc任意数量的位置参数（带单个星号参数）
        """定位元素"""
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            # print('页面未找到%s元素' % (loc))
            return False

    def click_element(self,*loc):
        """点击元素"""
        self.find_element(*loc).click()

    def input_element(self,value,*loc):
        """往元素里输入value值"""
        element = self.driver.find_element(*loc)
        element.clear()
        element.send_keys(value)

    def get_element_text(self,*loc):
        """获取元素的text"""
        return self.find_element(*loc).text()

    def press_back(self):
        """点击back键"""
        self.driver.press_keycode(4)

    def press_home(self):
        """点击home键"""
        self.driver.press_keycode(3)

    def press_menu(self):
        """点击menu键"""
        self.driver.press_keycode(82)

    def press_volume_up(self):
        """点击音量+键"""
        self.driver.press_keycode(24)

    def press_volume_down(self):
        """点击音量-键"""
        self.driver.press_keycode(25)

    def swipe_up(self):
        """向上滑动"""
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = int(0.5*width)
        start_y = int(0.75*height)
        end_x = int(0.5*width)
        end_y = int(0.25*height)
        self.driver.swipe(start_x,start_y,end_x,end_y)

    def swipe_down(self):
        """向下滑动"""
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = int(0.5 * width)
        start_y = int(0.25 * height)
        end_x = int(0.5 * width)
        end_y = int(0.75 * height)
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def get_screenshot(self,name=u"截图"):
        """截图并保存文件到Data/screenshot/文件夹下，文件名为当前时间+name"""
        # fq = "..\\Data\\screenshot"
        fq = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\Data\\screenshot\\'
        now_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
        type = r'.png'
        #加上时间，就没办法保存截图，目前暂时不知道怎么回事
        filename = fq + name + type
        self.driver.get_screenshot_as_file(filename)
        print("截图成功")



