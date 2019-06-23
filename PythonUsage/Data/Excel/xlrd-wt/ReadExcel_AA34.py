import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(9)                                # 根据sheet页名字获取sheet
sheetaa34 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refBP = {'': ''}
refBJ = {'': ''}
refII = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    refBP[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    refBJ[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    refII[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa34.nrows):
    if str(sheetaa34.row_values(i)[1]) in refBP:
        ret = refBP[str(sheetaa34.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


for i in range(sheetaa34.nrows):
    if str(sheetaa34.row_values(i)[2]) in refBJ:
        ret = refBJ[str(sheetaa34.row_values(i)[2])]
        ws.write(i, 2, str(ret))
        print(ret)


for i in range(sheetaa34.nrows):
    if str(sheetaa34.row_values(i)[3]) in refII:
        ret = refII[str(sheetaa34.row_values(i)[3])]
        ws.write(i, 3, str(ret))
        print(ret)


writecp.save('book.xls')

