from openpyxl import Workbook
data = [
    ["tid","mode","type","amount"],
    [1001,"cash", "deposit", 10000],
    [1002,"cheque", "withdrawal", 10000],
    [1003,"cash", "deposit", 20000],
    [1004,"upi","transfer",4000]
]
wb = Workbook()
activesheet = wb.active
activesheet.title="write file"

for row in data:
    activesheet.append(row)

wb.save("bank.xlsx")
print("The data is written successfully")