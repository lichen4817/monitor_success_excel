import pandas as pd
import numpy as np
impt_xlsx_resource=pd.read_excel('F:\\pptest\\screen_monitor_0411.xlsx',sheet_name='销售城市')
sheet2_dataframe = impt_xlsx_resource[(impt_xlsx_resource.媒体 == 'smart') & (impt_xlsx_resource.套装 == '不分套装') & (impt_xlsx_resource.城市 != '无匹配') ].pivot_table(
    index='城市',
    values=['可售安装总数', '推送成功总数', '分钟统计推送成功且七天平均>20h'],aggfunc={'可售安装总数':np.sum,'推送成功总数':np.sum,'分钟统计推送成功且七天平均>20h':np.sum})
sheet2_dataframe=sheet2_dataframe.sort_values('可售安装总数',ascending=False)
print(sheet2_dataframe)