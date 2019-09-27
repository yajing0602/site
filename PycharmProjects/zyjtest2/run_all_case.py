# import  unittest
# from case import TestNewGoods
# import HTMLTestRunner
# from  case2 import TestApp
# suit=unittest.TestSuite()
# loader=unittest.TestLoader()
# suit.addTest(loader.loadTestsFromTestCase(TestNewGoods))
# suit.addTest(loader.loadTestsFromTestCase(TestApp))
# with open("test.html","bw+")as file:
#     Runner=HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="新建商品api测试报告",description="测试登录、新建课程和课时")
#     Runner.run(suit)
import unittest
import HTMLTestRunner
import os
import requests
from ruamel import yaml
# import yaml
from sendEmail import sendEmail
curpath = os.path.dirname(os.path.realpath(__file__))
#登录后台管理系统返回token值
def login_manager(user="13096995875",psw="123456"):
    url="http://10.9.17.240:12500/manage/kzm/login"
    datas={"_t":1565855209660,"username":user,"password":psw,"uuid":"0c850164-abfc-492d-8535-a173f455d6fc","captcha":"646556"}
    resonse=requests.post(url,headers={"Content-Type": "application/json"},json=datas)
    token=resonse.json()["data"]["token"] #通过字典取值提取到token值
    return token

def write_yaml(value):
    '''把获取到的token值写入yaml'''
    ypath = os.path.join(curpath,"config","config.yaml")
    #需要写入的内容
    t={"token":value}
    #写入yaml文件
    with open(ypath,"w",encoding="utf-8") as f:
        yaml.dump(t,f,Dumper=yaml.RoundTripDumper)


# 最好把一个系统的用例写在一个项目比如（后台管理系统写一个项目，app端写一个项目，不要混在一起，此处是为了学习）
# 当前知识针对后台管理系统对token进行全局设计
# 应该将app端针对sessionid和userid也做一个全局变量设计
def all_case(rule="test*.py"):
    #待执行用例的目录
    case_path=os.path.join(os.path.dirname(__file__),"case")
    discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    return  discover

def run_case(all_case,reportName="report"):
    curpath = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(curpath, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path): os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result.html")
    print("report path:%s" % report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                              verbosity=2,
                                              title=u'当老师python接口自动化测试报告',
                                              description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    token=login_manager("admin","admin")
    write_yaml(token)
    allcases=all_case()
    run_case(allcases)
    sendEmail()