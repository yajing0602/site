from selenium.webdriver.common.by import By
from BasePage import BasePage

class MyPage(BasePage):
    """----------------------元素位置信息--------------------"""
    #设置图标
    setting_icon = (By.ID,"com.ruicheng.teacher:id/rl_setting")

    """----------------------操作元素--------------------"""
    def click_setting(self):
        self.click_element(*self.setting_icon)