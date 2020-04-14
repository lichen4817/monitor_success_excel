import pandas as pd

xl = pd.ExcelFile('F:\\paiqitest\\123.xlsx')
sheet_name=xl.sheet_names
e='F:\\paiqitest\\summer.csv'
for i in sheet_name:
    s=pd.read_excel(xl,sheet_name=i)
    s.to_csv(e,mode='a',index=0,header=True)
