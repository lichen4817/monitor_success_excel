'''
import os
import codecs
import sys


def main(file1, file2 ):
    """将gbk编码的文件转为utf8编码的文件
    :param file1: gbk编码的文件
    :param file2: utf8编码的文件
    :return:
    """
    # 读取原文
    with open(file1, "r", encoding="gbk") as f:
        results = f.readlines()
    # 开始遍历读取结果，并写到新的文件中
    with codecs.open(file2, "w", encoding="utf-8") as f:
        for result in results:
            f.write(result)
    print("转码成功！转码后文件为:", file2)
'''
import os
import sys
import re
import math
import datetime
import time



b=datetime.datetime.today()
print(b)
print(b.year)
print(b.month)
print(b.day)
print(b.hour)
print(b.minute)
print(b.second)
print(b.microsecond)
print(b.fold)
print()
