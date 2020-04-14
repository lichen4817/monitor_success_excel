import os
import sys
import pandas as pd
from openpyxl import load_workbook
##git
inputdir=input('需要处理的文件路径:')
inputname=input('需要处理的文件名:')
outputdir=input('需要输出的路径名:')


os.system("python ./monitor_result_sheet1.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet2.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet3.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet4.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet5.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet6.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet7.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet8.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet9.py %s %s %s"%(inputname,inputdir,outputdir))
os.system("python ./monitor_result_sheet10.py %s %s %s"%(inputname,inputdir,outputdir))

