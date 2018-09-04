import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(3)                                # 根据sheet页名字获取sheet
sheetaa04 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refBQ = {'': ''}
refAF = {'': ''}
refX6 = {'': ''}
refBL = {'': ''}
refCQ = {'': ''}
refSC = {'': ''}
refJQ = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    refBQ[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    refAF[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    refX6[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    refBL[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])
    refCQ[str(sheet.row_values(i)[8])] = str(sheet.row_values(i)[9])
    refSC[str(sheet.row_values(i)[10])] = str(sheet.row_values(i)[11])
    refJQ[str(sheet.row_values(i)[12])] = str(sheet.row_values(i)[13])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[1]) in refBQ:
        ret = refBQ[str(sheetaa04.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[3]) in refAF:
        ret = refAF[str(sheetaa04.row_values(i)[3])]
        ws.write(i, 3, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[4]) in refX6:
        ret = refX6[str(sheetaa04.row_values(i)[4])]
        ws.write(i, 4, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[7]) in refBL:
        ret = refBL[str(sheetaa04.row_values(i)[7])]
        ws.write(i, 7, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[8]) in refCQ:
        ret = refCQ[str(sheetaa04.row_values(i)[8])]
        ws.write(i, 8, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[11]) in refSC:
        ret = refSC[str(sheetaa04.row_values(i)[11])]
        ws.write(i, 11, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[12]) in refJQ:
        ret = refJQ[str(sheetaa04.row_values(i)[12])]
        ws.write(i, 12, str(ret))
        print(ret)

writecp.save('book.xls')

