import xlrd
class readExcel():
    def __init__(self,excelPath,sheetName):
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        #获取第一行的key
        self.keys=self.table.row_values(0)
        self.rowNum=self.table.nrows
        self.colNum=self.table.ncols


    def dict_data(self):
        if self.rowNum<=1:
            print("总行数小于1")
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):
                s={}
                # 从第二行取对应的value值
                values=self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r

# if __name__ == "__main__":
#     filepath = "C:\\Users\\TTT\\PycharmProjects\\untitled2\\data.xlsx"
#     sheetName = "coursename1"
#     data = readExcel(filepath,sheetName)
#     case=data.dict_data()
#     print(case)