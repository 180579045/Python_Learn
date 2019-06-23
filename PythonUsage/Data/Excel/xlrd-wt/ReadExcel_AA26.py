import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(7)                                # 根据sheet页名字获取sheet
sheetaa26 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refAQ = {'': ''}
refAP = {'': ''}
refA2 = {'': ''}
refIC = {'': ''}
refHQ = {'': ''}
refAZ = {'': ''}

for i in range(sheet.nrows):
    if i == 0:
        continue
    refAQ[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])
    refAP[str(sheet.row_values(i)[2])] = str(sheet.row_values(i)[3])
    refA2[str(sheet.row_values(i)[4])] = str(sheet.row_values(i)[5])
    refIC[str(sheet.row_values(i)[6])] = str(sheet.row_values(i)[7])
    refHQ[str(sheet.row_values(i)[8])] = str(sheet.row_values(i)[9])
    refAZ[str(sheet.row_values(i)[10])] = str(sheet.row_values(i)[11])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


# 替换
for i in range(sheetaa26.nrows):
    if str(sheetaa26.row_values(i)[1]) in refAQ:
        ret = refAQ[str(sheetaa26.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


for i in range(sheetaa26.nrows):
    if str(sheetaa26.row_values(i)[2]) in refAP:
        ret = refAP[str(sheetaa26.row_values(i)[2])]
        ws.write(i, 2, str(ret))
        print(ret)


for i in range(sheetaa26.nrows):
    if str(sheetaa26.row_values(i)[3]) in refA2:
        ret = refA2[str(sheetaa26.row_values(i)[3])]
        ws.write(i, 3, str(ret))
        print(ret)


for i in range(sheetaa26.nrows):
    if str(sheetaa26.row_values(i)[5]) in refIC:
        ret = refIC[str(sheetaa26.row_values(i)[5])]
        ws.write(i, 5, str(ret))
        print(ret)


for i in range(sheetaa26.nrows):
    if str(sheetaa26.row_values(i)[8]) in refHQ:
        ret = refHQ[str(sheetaa26.row_values(i)[8])]
        ws.write(i, 8, str(ret))
        print(ret)


for i in range(sheetaa26.nrows):
    if str(sheetaa26.row_values(i)[12]) in refAZ:
        ret = refAZ[str(sheetaa26.row_values(i)[12])]
        ws.write(i, 12, str(ret))
        print(ret)


writecp.save('book.xls')

