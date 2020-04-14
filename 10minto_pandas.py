'''
import pandas as pd
#第二步：读取数据
iris = pd.read_csv('F:\\temporary_file\\python_excel\\location_100.csv')#读入数据文件
class_list = list(iris['buildingname'].drop_duplicates())#获取数据class列，去重并放入列表
# 第三步：按照类别分sheet存放数据
writer = pd.ExcelWriter('F:\\temporary_file\\python_excel\\location.xlsx')#创建数据存放路径
for i in class_list:
    iris1 = iris[iris['buildingname']==i]
    iris1.to_excel(writer,i)
writer.save()#文件保存
writer.close()#文件关闭
'''


import pandas as pd
import numpy as np
#demo_excel=pd.ExcelFile('F:\\temporary_file\\python_excel\\location.xlsx')
df = pd.read_csv('F:\\temporary_file\\python_excel\\location_100.csv', encoding='utf-8',sep=',')
print(df)















