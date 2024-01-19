__author__ = 'Gaurav.Khanna'

from openpyxl import load_workbook

from os import path

wb = load_workbook(r'C:\GK\my-file.xlsx', "r")

x = wb.get_sheet_names()

for a in x:
    if a == '3.0':
        print(a)