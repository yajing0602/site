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
from sendEmail import sendEmail
def all_case():
    #待执行用例的目录
    case_dir="C:\\Users\\TTT\\PycharmProjects\\zyjtest1\\case"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            testcase.addTest(test_case)
    return testcase

if __name__ == "__main__":
    report_path = "C:\\Users\\TTT\\PycharmProjects\\zyjtest1\\report\\result.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='当老师接口自动化测试报告',
                                           description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()
    # sendEmail()