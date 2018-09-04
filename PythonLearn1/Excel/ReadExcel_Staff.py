import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet2 = book.sheet_by_index(0)                               # 把所有要替换的内容放到第一个Sheet中
sheet = book.sheet_by_name('staff')                           # 根据sheet页名字获取sheet


StaffInfo = {"":""}                                           # 工号字典
# 通过行号获取数据
for i in range(sheet.nrows):
    print(sheet.row_values(i))                                # 获取第n行的数据
    StaffInfo[str(sheet.row_values(i)[1])] = str(sheet.row_values(i)[0])


# 通过上边读取的字典，修改Excel中对应的内容：
writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)

for i in range(sheet2.nrows):
    if str(sheet2.row_values(i)[0]) in StaffInfo:
        ret = StaffInfo[str(sheet2.row_values(i)[0])]
        ws.write(i, 0, str(ret))
        print(ret)

writecp.save('book.xls')