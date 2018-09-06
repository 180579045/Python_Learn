import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(11)                                # 根据sheet页名字获取sheet
sheetaa39 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refZ2 = {'': ''}
refZU = {'': ''}
refZX = {'': ''}
refIA = {'': ''}
ref03 = {'': ''}
refZ0 = {'': ''}
refRF = {'': ''}
refZJ = {'': ''}
refZY = {'': ''}
refZN = {'': ''}
refZP = {'': ''}
refCK = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    refZ2[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    refZU[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    refZX[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    refIA[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])
    ref03[str(sheet.row_values(i)[8])] = str(sheet.row_values(i)[9])
    refZ0[str(sheet.row_values(i)[10])] = str(sheet.row_values(i)[11])
    refRF[str(sheet.row_values(i)[12])] = str(sheet.row_values(i)[13])
    refZJ[str(sheet.row_values(i)[14])] = str(sheet.row_values(i)[15])
    refZY[str(sheet.row_values(i)[16])] = str(sheet.row_values(i)[17])
    refZN[str(sheet.row_values(i)[18])] = str(sheet.row_values(i)[19])
    refZP[str(sheet.row_values(i)[20])] = str(sheet.row_values(i)[21])
    refCK[str(sheet.row_values(i)[22])] = str(sheet.row_values(i)[23])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[7]) in refZ2:
        ret = refZ2[str(sheetaa39.row_values(i)[7])]
        ws.write(i, 7, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[11]) in refZU:
        ret = refZU[str(sheetaa39.row_values(i)[11])]
        ws.write(i, 11, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[13]) in refZU:
        ret = refZU[str(sheetaa39.row_values(i)[13])]
        ws.write(i, 13, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[44]) in refZU:
        ret = refZU[str(sheetaa39.row_values(i)[44])]
        ws.write(i, 44, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[17]) in refZX:
        ret = refZX[str(sheetaa39.row_values(i)[17])]
        ws.write(i, 17, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[18]) in refIA:
        ret = refIA[str(sheetaa39.row_values(i)[18])]
        ws.write(i, 18, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[24]) in ref03:
        ret = ref03[str(sheetaa39.row_values(i)[24])]
        ws.write(i, 24, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[35]) in refZ0:
        ret = refZ0[str(sheetaa39.row_values(i)[35])]
        ws.write(i, 35, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[37]) in refRF:
        ret = refRF[str(sheetaa39.row_values(i)[37])]
        ws.write(i, 37, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[38]) in refZJ:
        ret = refZJ[str(sheetaa39.row_values(i)[38])]
        ws.write(i, 38, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[39]) in refZY:
        ret = refZY[str(sheetaa39.row_values(i)[39])]
        ws.write(i, 39, str(ret))
        print(ret)


for i in range(sheetaa39.nrows):
    if str(sheetaa39.row_values(i)[62]) in refCK:
        ret = refCK[str(sheetaa39.row_values(i)[62])]
        ws.write(i, 62, str(ret))
        print(ret)


writecp.save('book.xls')

