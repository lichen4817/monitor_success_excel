import xlrd
import xlwt
import csv
import xlsxwriter

book=xlrd.open_workbook('F:\\桌面\\临时数据需求\\19\\杭州智能屏上刊率\\北京智能屏楼宇表-20190717.xlsx')
#book=xlwt.Workbook()
a=book.sheet_names()
for i in a:
    print (i)


