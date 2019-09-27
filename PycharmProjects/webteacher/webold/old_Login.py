from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://test.api2.danglaoshi.net:3001/course/list")
driver.add_cookie({"name":"sid","value":"s%3ARv1WO0jkKaLjwB8rssIc40TnQjWofzEy.DXatrcskoXzXPX4Qvs72elCnj0GqncFUvO9ORh%2BIhYA"})
driver.get("http://test.api2.danglaoshi.net:3001/course/list")

