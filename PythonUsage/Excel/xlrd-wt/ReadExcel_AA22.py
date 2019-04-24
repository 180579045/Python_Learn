import xlrd
import xlwt
from xlutils.copy import copy


book = xlrd.open_workbook('Datafile/EQ_Staff.xlsx')           # 打开一个excel
sheet = book.sheet_by_index(5)                                # 根据sheet页名字获取sheet
sheetaa22 = book.sheet_by_index(0)                            # 默认用第一个sheet做替换

refAT = {'': ''}
for i in range(sheet.nrows):
    if i == 0:
        continue
    refAT[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1])


writecp = copy(book)                                          # 利用copy函数复制一个Excel
ws = writecp.get_sheet(0)                                     # AA04表


for i in range(sheetaa22.nrows):
    if str(sheetaa22.row_values(i)[1]) in refAT:
        ret = refAT[str(sheetaa22.row_values(i)[1])]
        ws.write(i, 1, str(ret))
        print(ret)


writecp.save('book.xls')

