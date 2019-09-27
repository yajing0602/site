from bs4 import BeautifulSoup
import sys
report=open("D:\\zyj\\tools\\apireport\\html\\HtmlReport.html",encoding='UTF-8')  # 读取html文件
soup=BeautifulSoup(report,"html.parser")
soup.prettify()
tag=soup.find_all("tr")
print(tag[2].contents)
p=tag[2].contents
rate=p[3].string
if rate=="100.00%":
    sys.exit(0)
else:
    sys.exit(1)
#job构建失败是无法运行下去才会失败，能正常运行都不会失败的，你可以把不满足条件时作为python运行出错的条件，
# 如sys.exit（1）该方法中包含一个参数status，默认为0，表示正常退出，也可以为1，表示异常退出






