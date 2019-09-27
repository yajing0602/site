from selenium.webdriver.common.by import By
from BasePage import BasePage

class SettingPage(BasePage):
    """----------------------元素位置信息--------------------"""
    #退出登录按钮
    logout_btn = (By.ID,"com.ruicheng.teacher:id/bt_logout")

    """----------------------操作元素--------------------"""
    def click_logout_btn(self):
        self.click_element(*self.logout_btn)


    """功能业务操作"""
    def logout(self):
        """退出登录"""
        self.click_logout_btn()