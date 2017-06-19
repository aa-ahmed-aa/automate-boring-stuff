#! python3
# excelTest.py - Test and open excel sheets
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

print(sheet.cell(row=1, column=2).value)