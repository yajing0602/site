import xlrd
#打开excel
data=xlrd.open_workbook("C:\\Users\\TTT\\PycharmProjects\\untitled2\\data.xlsx")
#打开表单
table=data.sheet_by_name(u"user")
#获取总行数
nrows=table.nrows
#获取总列数
ncols=table.ncols
#获取第一行的值-存在列表中
a=table.row_values(0)  #['username', 'password']
#获取第一列的值
b=table.col_values(0)


