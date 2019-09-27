from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://test.api2.danglaoshi.net:3001/course/list")
driver.add_cookie({"name":"sid","value":"s%3AaZDRAZT2cT-U83UIXOPjoEDFa3oGd57B.UtMLs9VnZuyr8EAH38h9ymRK45bI%2BINUk%2Fz59N8H8mM"})
driver.get("http://test.api2.danglaoshi.net:3001/course/list")

driver.find_element_by_xpath("//button[@onclick=\"window.location.href='/course/addCourse'\"]").click()
# 定位选择按钮，并从本地选择文件
driver.find_element_by_xpath("//input[@id=\"courseThumbnailInput\"]").send_keys(r"C:\Users\TTT\Desktop\2028.jpg_wh300.jpg")
#定位上传按钮，点击上传文件
driver.find_element_by_xpath("//*[@id=\"addCourseForm\"]/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/a").click()
