import pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt

adlength_list=[5,15,30]
freq_list=[60,120,180,240,300,360,420,480,540,600,660,900]
c=0


for adlen in adlength_list:
    for freq in freq_list:
        df2= pd.DataFrame({ '城市' : '上海',
                            '天数' : pd.Series(range(1,29),index=list(range(1,29)),dtype='float32'),
                            '套装' : 'A3',
                            '描述' : adlen,
                            '频次' : freq
                           })
        df3= pd.DataFrame({'城市': '上海',
                            '天数': pd.Series(range(1, 29), index=list(range(1, 29)), dtype='float32'),
                            '套装': 'A4',
                            '描述': adlen,
                            '频次': freq
                          })
        c=c+1
        d=str(c)
        x=str(adlen)
        y=str(freq)
        a='F:\\paiqitest\\ParameterA3A4SH'+d +'.xlsx'
        e='F:\\paiqitest\\result.csv'

        f1='ParameterA3A4SH'+d+'.xlsx'
        f2='reachA3A4SH_'+ x +'_'+ y +'.csv'
        f3='squareA3A4SH_'+ x +'_'+ y +'.csv'
        df4= pd.DataFrame({'dj1': f1,
                           'dj2': f2,
                           'dj3': f3
                          },index=[0])

        df4.to_csv(e,mode='a',index=0,header=False)

        pd.concat([df2,df3]).sort_values('天数').to_excel(a,index=False)