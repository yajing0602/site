from selenium import  webdriver
import  time
driver=webdriver.Chrome()

driver.get("http://139.199.115.28:8080/#/home")

driver.add_cookie({"name":"token","value":"b5355fd32eb38c287dfc3ef30m8e3c13x25"})

driver.refresh()

time.sleep(5)
user=driver.find_element_by_xpath("//span[@aria-haspopup=\"list\"]//span")

username=user.text

if username=="zhaoyajing":
    print("登录成功")
else:
    print("登录失败")