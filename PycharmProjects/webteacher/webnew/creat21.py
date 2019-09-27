from selenium import webdriver
import time
import datetime
driver=webdriver.Chrome()
driver.get("http://10.9.17.240:8080/#/login")
driver.find_element_by_xpath("//input[@placeholder=\"用户名\"]").send_keys("13096995875")
driver.find_element_by_xpath("//input[@placeholder=\"密码\"]").send_keys("123456")
driver.find_element_by_xpath("//input[@placeholder=\"验证码\"]").send_keys("1111111")
driver.find_elements_by_class_name("w-percent-100")[1].click()
driver.maximize_window()
time.sleep(5)
# 点击商品管理
driver.find_element_by_xpath("//div/aside/div/ul/li[14]/div").click()
time.sleep(3)
# 点击商品列表
driver.find_elements_by_xpath("//div//aside//div//ul//li[14]/ul//li")[0].click()
# 点击新增按钮
time.sleep(3)
driver.find_elements_by_xpath("//div[@class=\"el-form-item__content\"]//button//span")[1].click()
# 输入商品名称
driver.find_elements_by_xpath("//input[@placeholder=\"商品名称\"]")[1].send_keys("21天打卡-"+datetime.datetime.now().strftime('%Y%m%d'))
# 点击关联分类
driver.find_elements_by_xpath("//input[@placeholder=\"请输入关键词\"]")[1].click()
# 选择分类
time.sleep(3)
driver.find_element_by_xpath("//body/div[4]/div/div/ul/li[1]").click()
driver.find_element_by_xpath("//div[@data-gramm=\"false\"]").click()
# 上传缩略图
time.sleep(3)
driver.find_elements_by_xpath("//div[@class=\"upload-demo\"]//input")[0].send_keys(r"C:\Users\TTT\Desktop\pic\2230.jpg_wh300.jpg")
# 上传详情图
driver.find_elements_by_xpath("//div[@class=\"upload-demo\"]//input")[1].send_keys(r"C:\Users\TTT\Desktop\pic\file-371f23c82f194136be7d3c729100291f.png")
# 上传背景图
driver.find_elements_by_xpath("//div[@class=\"upload-demo\"]//input")[2].send_keys(r"C:\Users\TTT\Desktop\pic\file-fe9aac86707a4a6ba2407d9e3f57df3f.png")
# 上传描述
driver.find_element_by_xpath("//button[@class=\"ql-image\"]").click()