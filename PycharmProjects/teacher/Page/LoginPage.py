from appium import webdriver
from selenium.webdriver.common.by import By
from BasePage import BasePage
from login import *

class LoginPage(BasePage):

    """---------------------元素位置信息----------------------------------"""
    #用户名
    username = (By.ID,"com.ruicheng.teacher:id/ll_usename")
    #注册/登陆按钮
    regiser_login_btn = (By.ID,"com.ruicheng.teacher:id/bt_login")
    #qq登陆按钮
    qq_btn = (By.ID,"com.ruicheng.teacher:id/tv_qq_login")
    # 微博登陆按钮
    qq_btn = (By.ID, "com.ruicheng.teacher:id/tv_weibo_login")
    # 微信登陆按钮
    qq_btn = (By.ID, "com.ruicheng.teacher:id/tv_weixin_login")
    #同意勾选框
    agree = (By.ID,"com.ruicheng.teacher:id/tv_agree")
    #用户协议
    protoc = (By.ID,"com.ruicheng.teacher:id/tv_protocol")
    #左上角返回按钮
    back_btn = (By.ID,"com.ruicheng.teacher:id/iv_back")
    # 密码
    password = (By.ID, "com.ruicheng.teacher:id/et_password")
    # 登录按钮
    login_btn = (By.ID, "com.ruicheng.teacher:id/bt_login")
    # 忘记密码
    forget_password = (By.ID, "com.ruicheng.teacher:id/tv_forget_password")
    #发送验证码弹框标题
    content_title = (By.ID,"com.ruicheng.teacher:id/md_content")
    # 发送验证码弹框取消按钮
    cancle_btn= (By.ID, "com.ruicheng.teacher:id/md_buttonDefaultNegative")
    # 发送验证码弹框确定按钮
    cancle_btn = (By.ID, "com.ruicheng.teacher:id/md_buttonDefaultPositive")
    #密码为空或小于6位的提示（目前没有描述，只能定位到控件）
    pwd_null_notice = (By.XPATH,"//android.view.View")
    # 手机号错误的提示（目前没有描述，只能定位到控件）
    phone_wrong_notice = (By.XPATH, "//android.view.View")

    """------------------------元素操作-----------------------------"""
    def input_username(self,uname):
        """输入用户名"""
        self.input_element(uname,*self.username)

    def input_password(self,pwd):
        """输入密码"""
        self.input_element(pwd,*self.password)

    def click_register_login(self):
        """点击注册/登录按钮"""
        self.click_element(*self.regiser_login_btn)

    def click_login(self):
        """点击登录按钮"""
        self.click_element(*self.login_btn)


    """----------------------功能业务操作--------------------------"""
    def login(self,uname,pwd):
        self.input_username(uname)
        self.click_register_login()
        self.input_password(pwd)
        self.click_login()



if __name__ == '__main__':
    driver = init_device()
    #login(driver, '13100000999', '123456')
    loginPage = LoginPage(driver)
    loginPage.login('13100000999', '123456')
    time.sleep(2)
    loginPage.get_screenshot("shot111")
