import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(2)                                # 根据sheet页名字获取sheet
sheetaa04 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refAM = {'': ''}
refAN = {'': ''}
refAI = {'': ''}
refCG = {'': ''}
refZ2 = {'': ''}
for i in range(sheet.nrows):
    if i == 0:
        continue
    refAM[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    refAN[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    refAI[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    refCG[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])
    refZ2[str(sheet.row_values(i)[10])] = str(sheet.row_values(i)[11])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[3]) in refZ2:
        ret = refZ2[str(sheetaa04.row_values(i)[3])]
        ws.write(i, 3, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[4]) in refAM:
        ret = refAM[str(sheetaa04.row_values(i)[4])]
        ws.write(i, 4, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[5]) in refAN:
        ret = refAN[str(sheetaa04.row_values(i)[5])]
        ws.write(i, 5, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[10]) in refAI:
        ret = refAI[str(sheetaa04.row_values(i)[10])]
        ws.write(i, 10, str(ret))
        print(ret)


for i in range(sheetaa04.nrows):
    if str(sheetaa04.row_values(i)[11]) in refCG:
        ret = refCG[str(sheetaa04.row_values(i)[11])]
        ws.write(i, 11, str(ret))
        print(ret)

writecp.save('book.xls')

