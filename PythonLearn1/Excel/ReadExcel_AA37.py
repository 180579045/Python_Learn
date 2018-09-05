import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(10)                               # 根据sheet页名字获取sheet
sheetaa37 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

ref01 = {'': ''}
ref02 = {'': ''}
ref03 = {'': ''}
ref04 = {'': ''}
ref05 = {'': ''}
ref06 = {'': ''}
ref07 = {'': ''}
ref08 = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    ref01[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    ref02[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    ref03[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    ref04[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])
    ref05[str(sheet.row_values(i)[8])] = str(sheet.row_values(i)[9])
    ref06[str(sheet.row_values(i)[10])] = str(sheet.row_values(i)[11])
    ref07[str(sheet.row_values(i)[12])] = str(sheet.row_values(i)[13])
    ref08[str(sheet.row_values(i)[14])] = str(sheet.row_values(i)[15])

writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[1]) in ref01:
        ret = ref01[str(sheetaa37.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[2]) in ref02:
        ret = ref02[str(sheetaa37.row_values(i)[2])]
        ws.write(i, 2, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[6]) in ref03:
        ret = ref03[str(sheetaa37.row_values(i)[6])]
        ws.write(i, 6, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[7]) in ref04:
        ret = ref04[str(sheetaa37.row_values(i)[7])]
        ws.write(i, 7, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[8]) in ref05:
        ret = ref05[str(sheetaa37.row_values(i)[8])]
        ws.write(i, 8, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[14]) in ref06:
        ret = ref06[str(sheetaa37.row_values(i)[14])]
        ws.write(i, 14, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[15]) in ref07:
        ret = ref07[str(sheetaa37.row_values(i)[15])]
        ws.write(i, 15, str(ret))
        print(ret)


for i in range(sheetaa37.nrows):
    if str(sheetaa37.row_values(i)[19]) in ref08:
        ret = ref08[str(sheetaa37.row_values(i)[19])]
        ws.write(i, 19, str(ret))
        print(ret)

writecp.save('book.xls')

