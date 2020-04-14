#!/usr/bin/env python
# coding:utf-8

import os
import sys
import csv
import datetime
import urllib
import urllib.parse
import urllib.request
import subprocess

nowDay = datetime.datetime.now().strftime('%Y_%m_%d')
yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y.%m.%d")

DELETE_LOGS = "ls -ltr --full-time %s "
catalogyCityName = ['上海', '北京', '广州', '深圳', '成都', '杭州', '南京', '武汉', '长沙', '重庆']


def dingDingAlarm(nameType, errMsg, defaultKey='a0b8d7f306d8156d58a6f8db6d5fc019483e1d638f965ba83131c9a1fa57968b'):
    # url = 'http://172.19.100.1:16789/user/alarm/dingding' #aliyun
    url = 'http://10.216.62.11:16789/user/alarm/dingding'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    data = {
        'key': defaultKey,
        'software': nameType,
        'errormessage': errMsg
    }

    data = urllib.parse.urlencode(data)
    req = urllib.request.Request(url='%s%s%s' % (url, '?', data), headers=headers)
    response = urllib.request.urlopen(req).read()
    print(response)


def sendmail(subject, msg, receive, ccaddrs, filename):
    url = r'http://10.216.62.11:16789/user/alarm/automailpost'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    remote_dir = '/data/quyang/mail_file/mrd/'
    filename_new = ''
    filenames = filename.split(",")
    for items in filenames:
        os.system('scp ' + items + ' 10.216.62.11:' + remote_dir)
        print('scp ' + items + ' 10.216.62.11:' + remote_dir)
        filename = items.split("/")[-1]
        if filename_new.strip() == '':
            filename_new = remote_dir + filename
        else:
            filename_new = filename_new + ',' + remote_dir + filename

    print(filename_new)

    data = {
        'receive': receive,
        'cc': ccaddrs,
        'subject': subject,
        'msg': msg,
        'filename': filename_new
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, headers=headers, data=data)
    response = urllib.request.urlopen(req).read()
    print(response)


def getOneFileSize(dir_prefix):
    '''
    get empty file and put into array
    '''
    flag = 1
    status, stdout = subprocess.getstatusoutput(DELETE_LOGS % dir_prefix)
    stdout = stdout.split()
    fileSize = int(stdout[4])
    if (fileSize <= 10):
        if os.path.exists(dir_prefix):
            flag = 0

    return flag


def getAttachFileToMail(filname):
    print("========start getAttachFile===")
    fileNotEmpty = list()
    for fs in filname:
        size = getOneFileSize(fs)
        if size:
            fileNotEmpty.append(fs)
    stringa = ','.join(fileNotEmpty)
    print("=====file name======", stringa)
    return stringa


def createCsvFile():
    for cityname in catalogyCityName:
        filename = local_path + '/catalog_' + nowDay + '_' + cityname + '.csv'
        with open(filename, 'w') as f:
            csv.writer(f)


def writeCsvfile(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            # write lines
            writer.writerows(content)
    except Exception as e:
        print(str(e))


def splitCsvfile():
    for cityname in catalogyCityName:
        rowsarray = list()
        cityfilepath = local_path + '/catalog_' + nowDay + '_' + cityname + '.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                # reader = csv.reader(open(filename,'r'))
                for row in reader:
                    if row[0] == cityname:
                        rowsarray.append(tuple(row))
            # write to table_csv
            # print cityname.encode('utf-8'),"=====len(rowsarray)=======",len(rowsarray)
            writeCsvfile(cityfilepath, rowsarray)
        except Exception as e:
            print(str(e))


def getFile():
    File = list()
    for cityname in catalogyCityName:
        cityfilepath = local_path + '/catalog_' + nowDay + '_' + cityname + '.csv'
        File.append(cityfilepath)

    File.append(filename)

    return File


def get_context():
    global context
    context = '''
        <p style="font-size:18px">各位好:</p>
        <p style="font-size:18px">     下面是品牌品类每周一排查各个城市的广告信息,请及时处理，谢谢！</p>
    '''


def getMsg():
    global context
    msg = '''
        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta charset="utf-8" />
                <title>宝洁前天监播数据信息汇总--test</title>
            </head>
            <body>
                <style>
                    table { border-collapse: collapse}
                    th { border: 1px solid black;padding:10px 5px; text-align:center; font-size: 18px; font-weight: bolder; background-color:d9edf7; min-width:40px}
                    td { border: 1px solid black; padding:10px; min-width:40px}
                    .fail{background: pink}
                </style>
                ''' + context + '''
                <br>
                <br>

                <span style="font-size:16px">吕丽霞  Lixia Lv<br>
                集团大数据部<br>地址：上海江苏路369号兆丰世贸大厦27楼G座<br>手机：15900917832<br>
                E-Mail: lvlixia@focusmedia.cn<br>http://www.focusmedia.cn<br></span>

            </body>
        <html>
        '''

    return msg


if __name__ == "__main__":
    FILE = ''
    context = ''
    emptyFile = list()
    nameType = "品牌品类每周一数据："
    subject = '请查看品牌品类每周一排查信息' + nowDay
    sender = 'lvlixia@focusmedia.cn'
    toaddrs = 'lvlixia@focusmedia.cn'
    ccaddrs = 'lvlixia@focusmedia.cn,ruinianxia@focusmedia.cn,lichen@focusmedia.cn,yudeshui@focusmedia.cn'
    local_path = '/data/focusmedia/mrd/catalogy_fm/job/catalogy_fm'
    filename = local_path + '/catalog_fm_' + nowDay + '.csv'

    createCsvFile()
    splitCsvfile()
    FILE = getFile()
    for fs in FILE:
        getOneFileSize(fs)
    if emptyFile:
        errMsg = "有附件为空请及时查看！"
        dingDingAlarm(nameType, errMsg)
    else:
        try:
            errMsg = "邮件发送成功！"
            allFile = getAttachFileToMail(FILE)
            get_context()
            MSG = getMsg()
            sendmail(subject, MSG, toaddrs, ccaddrs, allFile)
            dingDingAlarm(nameType, errMsg)
        except:
            errMsg = "邮件发送失败！"
            dingDingAlarm(nameType, errMsg)