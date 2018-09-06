import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(12)                               # 根据sheet页名字获取sheet
sheetaa43 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

ref01 = {'': ''}
ref02 = {'': ''}
ref03 = {'': ''}
ref04 = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    ref01[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    ref02[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    ref03[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    ref04[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])

writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa43.nrows):
    if str(sheetaa43.row_values(i)[3]) in ref01:
        ret = ref01[str(sheetaa43.row_values(i)[3])]
        ws.write(i, 3, str(ret))
        print(ret)


for i in range(sheetaa43.nrows):
    if str(sheetaa43.row_values(i)[5]) in ref02:
        ret = ref02[str(sheetaa43.row_values(i)[5])]
        ws.write(i, 5, str(ret))
        print(ret)


for i in range(sheetaa43.nrows):
    if str(sheetaa43.row_values(i)[8]) in ref03:
        ret = ref03[str(sheetaa43.row_values(i)[8])]
        ws.write(i, 8, str(ret))
        print(ret)


for i in range(sheetaa43.nrows):
    if str(sheetaa43.row_values(i)[10]) in ref04:
        ret = ref04[str(sheetaa43.row_values(i)[10])]
        ws.write(i, 10, str(ret))
        print(ret)



writecp.save('book.xls')

