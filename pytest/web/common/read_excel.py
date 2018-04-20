'''
Created on 2018年4月20日/上午10:00:10

@author: joker.zhang
'''
import xlrd
from web.Config import config

def read_all_data(sheet_name):
    excle_file = xlrd.open_workbook(config.excel_path)
    login_sheet = excle_file.sheet_by_name(sheet_name)
    nrows = login_sheet.nrows
    print(nrows)
    list_all_data =[]
    for row in range(1, nrows):
        list_temp = login_sheet.row_values(row)
        tuple_temp = tuple(list_temp)
        list_all_data.append(tuple_temp)
    
    return list_all_data