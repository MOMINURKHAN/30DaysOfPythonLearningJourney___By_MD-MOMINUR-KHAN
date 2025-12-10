#checking some module's func with 'dir' func
import math
print(dir(math)) #it'll show all built-in func in any module

#let's explore datetime func and it's functionality
from datetime import datetime

now = datetime.now()

day = now.day
date = now.date()
astimezone = now.astimezone()
print(f"Date : {date} Day: {day} Now_time ; {now} ctime_string formal : {now.ctime()} \
      \nwith_timezone : {astimezone} hour : {now.hour} seconds : {now.second} fromtimestamp : {now.fromtimestamp(23423.0,tz=now.tzinfo)} \
      Timestamp : {now.timestamp()} {now.utctimetuple()}")

t = datetime.now()

print(f"t(datetime.now()) : {t}")

time = now.strftime("%m:%y:%d ,%H:%M:%S")
print(f"Time(strftime) : {time}")
date_string = "5 December 2019"
date_value = datetime.strptime(date_string,"%d %B %Y")
print(date_value)

now = now
new_year = datetime(year=2025,month=12,day=31)
print(new_year-now)

print((now.timestamp())/(24*60*60*30*12))

