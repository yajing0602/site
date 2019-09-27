import  unittest
from case import TestNewGoods
import HTMLTestRunner
from  case2 import TestApp
suit=unittest.TestSuite()
loader=unittest.TestLoader()
# suit.addTest(loader.loadTestsFromTestCase(TestNewGoods))
suit.addTest(loader.loadTestsFromTestCase(TestApp))
with open("test.html","bw+")as file:
    Runner=HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="新建商品api测试报告",description="测试登录、新建课程和课时")
    Runner.run(suit)