


import datetime
def calculateWeek(current_day):
    mytoday = datetime.datetime.strptime(current_day, '%Y_%m_%d')
    current_week = mytoday.weekday() + 1
    week_enddate = (mytoday + datetime.timedelta(days=7 - current_week)).strftime('%Y_%m_%d')
    week_startdate = (mytoday - datetime.timedelta(days=current_week - 1)).strftime('%Y_%m_%d')
    return (week_startdate, week_enddate,current_week)

startday,endday,cw=calculateWeek('2020_03_15')
print(startday,endday,cw)
