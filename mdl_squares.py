import datetime as dt
import pymssql

#   获取对应的游标
def getConnectCursor():
    connect = pymssql.connect(server='10.216.9.14',port='1433',user='BD_Reader',password='E45ADE21-2192',database='DB_FAMCenter')
    cursor = connect.cursor()
    return cursor

cursor=getConnectCursor()

def getallDate(begindate):
    alldate=list()
    alldate.append(begindate)
    for startdate in range(2):
        date1 = dt.datetime.strptime(begindate,'%Y-%m-%d')
        begindate = (date1+dt.timedelta(days=7)).strftime('%Y-%m-%d')
        alldate.append(begindate)
    return alldate
print(getallDate('2019-01-07'))
dateToSql = list(getallDate('2019-06-17'))
print(dateToSql)
for startdate in dateToSql:
    cursor.execute("""     
             select buliding_no bd,begindate,count(distinct framedia_no) fn,sum(interval) adlength from (
							select begindate,seqno,framedia_no,buliding_no,interval from (
							select j.*,k.buliding_no,k.framedia_no from 
                            (
                                select framedia_no,buliding_no,city_no,case when device_style='[智能]32寸数码' then 304 when device_style='[智能]25寸数码'  then 303  when device_style='[一体机]19寸数码' then 288 else 0 end as devicestyle_id  from  tbb_BuildingInfo where 
                                 city_name='安宁' and (device_style = '[智能]32寸数码' or device_style = '[智能]25寸数码'  or device_style = '[智能]55寸数码' or device_style = '[一体机]19寸数码' )
                            ) k
                             inner join 
                            (
                            select c.*,d.framediano from 
                                (
                                select *
                                from schedule_screen_FDM_History where begindate='"""+startdate+"""'  and fromtype in (1,2,9,10)   and datepart(hh,endtime) = 23 
                                 ) c 
                                inner join 
                                  (
                                  select a.* from   
                                  ( select * from Center_tb_SchNo_FDM where begindate ='"""+startdate+"""' ) a 
                                  inner join 
                                  (
                                  select citycode,begindate as bd,max(Id) as maxupid 
                                  from Center_Upload 
                                  where     bysystem='FDM' and begindate='"""+startdate+"""' 
                                   and IsNeedSK=1  group by citycode,cityname,begindate
                                  ) b on a.cityno=b.citycode and a.upid = b.maxupid
                                ) d on c.citycode = d.cityno and c.upid = d.upid 
                                and (CAST(c.framedialist as varchar) = cast(d.framedialist1 as varchar) 
                                     or (c.framedialist=0 and d.FramediaList1=c.Package)
                                )
                                where devicestyleid in (304,303,288,342)
                            ) j on k.framedia_no = j.framediano and k.devicestyle_id = j.devicestyleid and k.city_no = j.citycode ) x group by seqno,framedia_no,buliding_no,interval,begindate) y group by buliding_no,begindate
                    
                    """)
    filename="maruidong.csv"
    with open(filename,'a+') as object:
        for row in cursor:
            object.write(str(row[0])+','+str(row[1]) +',' + str(row[2]) + ',' + str(row[3]) +'\n')
            object.flush()
    print(startdate)