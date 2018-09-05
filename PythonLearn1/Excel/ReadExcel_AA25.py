import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(6)                                # 根据sheet页名字获取sheet
sheetaa25 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refCB = {'': ''}
ref03 = {'': ''}
ref09 = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    refCB[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    ref03[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    ref09[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa25.nrows):
    if str(sheetaa25.row_values(i)[1]) in refCB:
        ret = refCB[str(sheetaa25.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


for i in range(sheetaa25.nrows):
    if str(sheetaa25.row_values(i)[3]) in ref03:
        ret = ref03[str(sheetaa25.row_values(i)[3])]
        ws.write(i, 3, str(ret))
        print(ret)


for i in range(sheetaa25.nrows):
    if str(sheetaa25.row_values(i)[4]) in ref09:
        ret = ref09[str(sheetaa25.row_values(i)[4])]
        ws.write(i, 4, str(ret))
        print(ret)


for i in range(sheetaa25.nrows):
    if str(sheetaa25.row_values(i)[5]) in ref09:
        ret = ref09[str(sheetaa25.row_values(i)[5])]
        ws.write(i, 5, str(ret))
        print(ret)

writecp.save('book.xls')

