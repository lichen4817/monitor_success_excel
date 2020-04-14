#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment, Border, Side
import numpy as np
import xlrd as xd
import xlwt as xw
from win32com.client import constants as c
import string
import sys
inputname=sys.argv[1]
inputdir=sys.argv[2]
outputdir=sys.argv[3]

#获取文件名
date_file=inputname[len(inputname)-9:len(inputname)-5]
#确定结果sheet名
result_sheetname='LCD分套装点位推送及回传数据分析'+date_file+'销售用'
impt_xlsx_resource = pd.read_excel(inputdir + inputname, sheet_name='销售城市')
impt_xlsx_resource.replace('不分套装', '合计', inplace=True)
sheet4_dataframe = impt_xlsx_resource[(impt_xlsx_resource.媒体 == 'lcd') & (impt_xlsx_resource.套装 != '无套装') & (impt_xlsx_resource.城市 != '无匹配')].pivot_table(
    index=['城市', '套装'],
    values=['可售安装总数', '全设备推送成功率', '小时统计推送成功且七天平均>20h比率'])


# 重命名字段名
sheet4_dataframe.rename(columns={'可售安装总数': '可售点位数',
                                 '全设备推送成功率': '全部设备推送成功率',
                                 '小时统计推送成功且七天平均>20h比率': '可在线监测比'}, inplace=True)
#获取各城市套装数
suit_no=sheet4_dataframe.pivot_table(index='城市',values='可售点位数',aggfunc=len)
suit_no.rename(columns={'可售点位数':'套装数'},inplace=True)

#制定套装index
suit_index={'套装':['合计','A1套','A2套','A3套','A4套'],
            'suitindex':[1,2,3,4,5]
             }
suit_index=pd.DataFrame(suit_index)

# 根据指定index顺序排序
sheet4_dataframe=sheet4_dataframe.reset_index('套装')
data_normal={'城市':['全国','上海','北京','成都','杭州','深圳','广州','重庆','天津','武汉','昆明','大连','南京','青岛','合肥','济南','长沙','石家庄','长春','哈尔滨','沈阳','厦门','苏州','贵阳','西安','郑州','福州','无锡','东莞','太原','温州','海口','烟台','宁波','泉州','兰州','佛山','中山','珠海','柳州','洛阳','晋江','绵阳','廊坊','漳州','西宁','昆山','常德','宜昌','桂林','惠州','芜湖','鄂尔多斯','石狮','江阴','汕头','沧州','常熟','西双版纳','三明','南通','威海','张家港','台州','泸州','德阳','泰州','临沂','滁州','蒙自','襄阳','衡水','遵义','惠安','绍兴','义乌','宜宾','嘉兴','安庆','曲靖','楚雄','湖州','瑞安','南安','平湖','济宁','玉溪','湘潭','泰安','三亚','清镇','大理','凯里','丽江','九江','扬州','安宁','北碚','仁怀','邢台','个旧','唐山','安顺','咸阳','都江堰','新郑','荥阳','乐清','秦皇岛','太仓','慈溪','巢湖','涪陵','永川','邯郸','保定'],
             'no':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115]}
data_normal=pd.DataFrame(data_normal)

#融合多表并去除单套合计数据
merge_1 = pd.merge(sheet4_dataframe, data_normal, left_on='城市', right_on='城市' , how='inner', sort=False)
merge_2 = pd.merge(merge_1, suit_no, left_on='城市', right_on='城市' , how='inner', sort=False)
merge_3 = pd.merge(merge_2, suit_index, left_on='套装', right_on='套装' , how='inner', sort=False)
merge_3=merge_3[(merge_3['套装数']>2) |  ((merge_3['套装数'] == 2) & (merge_3['套装'] != '合计') ) | ((merge_3['套装数'] == 1) & (merge_3['套装'] == '合计') )]


#对融合后的表处理，保留所需结果字段
merge_result =merge_3.pivot_table(index=['城市','套装'],values=['可售点位数','全部设备推送成功率','可在线监测比','no','suitindex'])
merge_result= merge_result.sort_values(by=['no','suitindex'])
merge_result['可在线监测比'] = merge_result['可在线监测比'].apply(lambda x: format(x, '.2%'))
merge_result['全部设备推送成功率'] = merge_result['全部设备推送成功率'].apply(lambda x: format(x, '.2%'))
merge_result.drop(['no','suitindex'],axis=1,inplace=True)

# 重置列的顺序
order = ['可售点位数','全部设备推送成功率','可在线监测比']
merge_result = merge_result[order]

##返回行数
row_1 = merge_result.shape[0]
##返回列数
column_1 = merge_result.shape[1]


merge_result.to_excel(outputdir + 'monitor_reuslt' + date_file +'.xlsx',sheet_name=result_sheetname)


##修改样式,遍历A-Z列
workbook = load_workbook(outputdir + 'monitor_reuslt' + date_file +'.xlsx')
ali = Alignment(horizontal='centerContinuous', vertical='center')
font = Font(name='微软雅黑', size=12, bold=False, italic=False)
border = Border(left=Side(border_style='thin'), bottom=Side(border_style='thin'), top=Side(border_style='thin'),
                right=Side(border_style='thin'))
sheet = workbook.active
first_change = 1
for column_no in string.ascii_uppercase:
    for row_no in range(1, row_1 + 2):
        c = str(column_no) + str(row_no)
        cell = sheet[c]
        cell.font = font
        cell.alignment = ali
        cell.border = border
    first_change += 1
    if first_change > column_1 + 2:
        break
#改变格式后的文件反写会对应sheet
workbook.save(filename=outputdir + 'monitor_reuslt' + date_file +'.xlsx')
print(result_sheetname + ' Success !')
