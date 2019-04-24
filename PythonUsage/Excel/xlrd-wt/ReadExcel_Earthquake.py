import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet2 = book.sheet_by_index(0)                               # 根据顺序获取sheet
sheet = book.sheet_by_name('staff')                           # 根据sheet页名字获取sheet

print('该Excel，Staff中总共包含' + str(sheet.ncols) + '列；'
      '总共包含' + str(sheet.nrows) + '行')                    # 获取excel里面有多少列\

print('第一行数据是：' + str(sheet.row_values(0)))             # 获取第一行

#for i in sheet.get_rows():
    # print(i)                                                 # 获取每一行的数据


StaffInfo = {"":""}
# 通过行号获取数据
for i in range(sheet.nrows):
    print(sheet.row_values(i))                                # 获取第n行的数据
    StaffInfo[str(sheet.row_values(i)[1])] = str(sheet.row_values(i)[0])



# 通过列号获取数据
print(sheet.col_values(1))                                    # 取第一列的数据
for i in range(sheet.ncols):
    print(sheet.col_values(i))                                # 获取第n列的数据



# 通过上边读取的字典，修改Excel中对应的内容：
writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(1)

for i in range(sheet2.nrows):
    if str(sheet2.row_values(i)[0]) in StaffInfo:
        ret = StaffInfo[str(sheet2.row_values(i)[0])]
        ws.write(i, 0, str(ret))
        print(ret)

writecp.save('book.xls')