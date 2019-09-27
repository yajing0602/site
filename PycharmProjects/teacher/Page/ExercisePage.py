from appium import webdriver
from selenium.webdriver.common.by import By
from BasePage import BasePage
from login import *

class ExercisePage(BasePage):

    #报考类型按钮
    lerning_type = (By.ID,"com.ruicheng.teacher:id/tv_learning_period")
    #消息图标
    notice_icon = (By.ID, "com.ruicheng.teacher:id/iv_home_notice")
    #banner
    banner = (By.XPATH,"//*[@id='com.ruicheng.teacher:id/bannerViewPager']/android.widget.ImageView")
    #模考大赛
    mokao = (By.XPATH,"//*[@id='com.ruicheng.teacher:id/rl_home_mokao']/android.widget.TextView")
    #历年真题
    zhenti = (By.XPATH, "//*[@id='com.ruicheng.teacher:id/rl_home_zhenti']/android.widget.TextView")
    # 错题练习
    cuoti = (By.XPATH, "//*[@id='com.ruicheng.teacher:id/rl_home_cuoti']/android.widget.TextView")
    #错题收藏
    colection = (By.XPATH,"//*[@id='com.ruicheng.teacher:id/rl_home_collection']/android.widget.TextView")
    #我的标签
    my_tab = (By.ID,"com.ruicheng.teacher:id/foot_user")

    def click_lerning_type(self):
        """点击报考类型按钮"""
        self.click_element(*self.lerning_type)

    def click_my_tab(self):
        """点击我的标签"""
        self.click_element(*self.my_tab)

    def get_lerning_type_text(self):
        return self.find_element(*self.lerning_type).text()


if __name__ == '__main__':
    driver = init_device()
    login(driver, '13100000999', '123456')
    execisePage = ExercisePage(driver)
    execisePage.click_lerning_type()
    driver.press_keycode(4)
    text = execisePage.get_lerning_type_text()
    print(text)