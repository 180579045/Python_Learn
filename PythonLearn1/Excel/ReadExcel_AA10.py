import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(4)                                # 根据sheet页名字获取sheet
sheetaa10 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refAJ = {'': ''}
refSB = {'': ''}
refZK = {'': ''}
refZ3 = {'': ''}
refCL = {'': ''}
refAH = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    refAJ[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    refSB[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    refZK[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    refZ3[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])
    refCL[str(sheet.row_values(i)[8])] = str(sheet.row_values(i)[9])
    refAH[str(sheet.row_values(i)[10])] = str(sheet.row_values(i)[11])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[1]) in refAJ:
        ret = refAJ[str(sheetaa10.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[2]) in refSB:
        ret = refSB[str(sheetaa10.row_values(i)[2])]
        ws.write(i, 2, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[4]) in refAJ:
        ret = refAJ[str(sheetaa10.row_values(i)[4])]
        ws.write(i, 4, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[6]) in refZK:
        ret = refZK[str(sheetaa10.row_values(i)[6])]
        ws.write(i, 6, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[7]) in refZ3:
        ret = refZ3[str(sheetaa10.row_values(i)[7])]
        ws.write(i, 7, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[9]) in refCL:
        ret = refCL[str(sheetaa10.row_values(i)[9])]
        ws.write(i, 9, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[14]) in refAH:
        ret = refAH[str(sheetaa10.row_values(i)[14])]
        ws.write(i, 14, str(ret))
        print(ret)


for i in range(sheetaa10.nrows):
    if str(sheetaa10.row_values(i)[15]) in refAJ:
        ret = refAJ[str(sheetaa10.row_values(i)[15])]
        ws.write(i, 15, str(ret))
        print(ret)

writecp.save('book.xls')

