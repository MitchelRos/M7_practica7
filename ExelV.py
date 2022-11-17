import openpyxl

def exel():
    n=openpyxl.workbook
    m=n.active
    cell1=m.cell(row=1, column=1)
    cell1.value=