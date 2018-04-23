'''
Created on 2018年4月20日/上午9:47:10

@author: joker.zhang
'''
import xlrd
from web.Common.read_excel import read_all_data

list2 = read_all_data()
print(list2)


# excle_file = xlrd.open_workbook(u'C:\\Users\\17TRACK\\eclipse-workspace\\TestPython\\pytest\\testdata\\testData.xlsx')
# sheetname = excle_file.sheets()
# first_sheet_name =excle_file.sheet_by_index(1)
# nrows = first_sheet_name.nrows
# ncols = first_sheet_name.ncols
# first_row_values = first_sheet_name.row_values(0)
# second_row_values = first_sheet_name.row_values(1)
# tup1 = tuple(second_row_values)

