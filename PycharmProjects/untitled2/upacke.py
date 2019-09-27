import  unittest
from  readdata1 import readExcel
import ddt
data1 = readExcel("C:\\Users\\TTT\\PycharmProjects\\untitled2\\data.xlsx","coursename1")
case1=data1.dict_data()
# case1=[{'coursename': '自动化课程01'}, {'coursename': '自动化课程02'}, {'coursename': '自动化课程03'}, {'coursename': '自动化课程04'}, {'coursename': '自动化课程05'}, {'coursename': '自动化课程06'}, {'coursename': '自动化课程07'}, {'coursename': '自动化课程08'}, {'coursename': '自动化课程09'}, {'coursename': '自动化课程10'}]

@ddt.ddt
class Testreaddate(unittest.TestCase):
    data1 = readExcel("C:\\Users\\TTT\\PycharmProjects\\untitled2\\data.xlsx", "coursename1")
    case1 = data1.dict_data()


    @ddt.data(*case1)
    @ddt.unpack
    def test_01(self,coursename):
        print(coursename)

if __name__=="__main__":
    unittest.main()