from appium import webdriver
import time

def init_device():
    """初始化设备、app，返回driver句柄"""
    desired_caps = {
                    'platformName': 'Android',
                    'deviceName': '127.0.0.1:21503',
                    'platformVersion': '5.1.1',
                    'appPackage': 'com.ruicheng.teacher',
                    'appActivity': 'Activity.LoginActivity',
                    'unicodeKeyboard': True, #此两行是为了解决字符输入不正确的问题
                    'resetKeyboard': True    #运行完成后重置软键盘的状态　　
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver

def login(driver,uname,pwd):
    """登录"""
    #定位账号输入框并填写账号
    driver.find_element_by_id("com.ruicheng.teacher:id/ll_usename").send_keys(uname)
    #点击 注册/登录按钮
    driver.find_element_by_id("com.ruicheng.teacher:id/bt_login").click()
    #定位密码输入框并输入密码
    driver.find_element_by_id("com.ruicheng.teacher:id/et_password").send_keys(pwd)
    #点击登录按钮
    driver.find_element_by_id("com.ruicheng.teacher:id/bt_login").click()
    #忽略


def find_title_list(driver):
    """定位课程列表的标题"""
    return driver.find_element_by_id("com.ruicheng.teacher:id/iv_title")

def find_price_list(driver):
    """定位课程列表的价格"""
    return driver.find_element_by_id("com.ruicheng.teacher:id/state")

def find_title_desc(driver):
    """定位课程详情页面的标题"""
    return driver.find_element_by_id("com.ruicheng.teacher:id/iv_title")

def find_price_desc(driver):
    """定位课程详情页面的价格"""
    return driver.find_element_by_id("com.ruicheng.teacher:id/tvv_price")

def find_introduce_desc(driver):
    """定位课程详情页面的课程介绍"""
    return driver.find_element_by_id("com.ruicheng.teacher:id/rb_des")



def check_kecheng(driver):
    """进入课程详情，并返回点击的课程标题"""
    #进入课程分页
    driver.find_element_by_id("com.ruicheng.teacher:id/v_tag2").click()
    #定位第一个课程，并获取课程名称、价格
    title = find_title_list(driver).get_attribute("text")
    price = find_price_list(driver).get_attribute('text')
    #点击课程，进入课程详情
    find_title_list(driver).click()
    return (title,price[1:])

if __name__ == '__main__':
    driver = init_device()
    login(driver,'13100000999','123456')
    title,price = check_kecheng(driver)
    print(title)
    print(price)
    title_des = find_title_desc(driver).get_attribute("text")
    price_des = find_price_desc(driver).get_attribute("text")
    introduce = find_introduce_desc(driver).get_attribute("text")
    print(title_des)
    print(price_des)
    print(introduce)