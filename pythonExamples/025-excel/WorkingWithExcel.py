__author__ = 'Gaurav.Khanna'

from openpyxl import load_workbook
import os.path

wb = load_workbook(r'C:\GK\Selenium\PHIX_Trunk\assets\prod\tests\Broker.xlsx', "r")
x = wb.get_sheet_names()
for a in x:
    if a == '3.0':
        print(a)