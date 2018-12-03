##Python常用的时间处理
python 中 time 有三种格式：

float,  
struct tuple(time.struct_time 或 datetime.datetime),  
str

常用的：

```
float --> struct tuple:   time.localtime( float )

struct time tuple --> str: time.strftime(format, struct time tuple)

str --> struct time tuple: time.strptime(str, format)

struct time tuple --> float : time.mktime(struct time tuple)

struct time tuple --> datetime: datetime(*time_tuple[0:6])
```
 
```
float --> datetime: datetime.datetime.fromtimestamp( float )

datetime --> str: datetime.strftime(format, datetime)

str --> datetime: datetime.strptime(str, format)

datetime --> struct time tuple: datetime.timetuple()
```
 

###Note:

time 是 float 为基础，小数点后是毫秒，整数部分是秒。（Java 是毫秒，所以，python_time*1000 == Java_time）

datetime 是int, 略去了毫秒部分。datetime tuple 少于 struct_time

####1. 当前时间
```>>> import time
>>> time.time()
1450681042.751

>>> time.localtime(time.time())
time.struct_time(tm_year=2015, tm_mon=12, tm_mday=21, tm_hour=15, tm_min=0, tm_sec=2, tm_wday=0, tm_yday=355, tm_isdst=0)

>>> time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
'2015-12-21 15:01:28'


>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2015, 12, 21, 14, 58, 38, 279000)

>>> datetime.today()
datetime.datetime(2015, 12, 21, 14, 59, 20, 204000)

>>> now = datetime.now()
>>> now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond

>>> now.isocalendar() # 2015年 第52周 星期一
(2015, 52, 1)

>>> now.isoweekday() # 星期几，1：Monday; 而 now.weekday() 返回值从0开始
```

####2. 日期字符串--> 日期
```>>> s='2015-12-21 15:01:28'
>>> timeTuple = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
datetime.datetime(2015, 12, 21, 15, 1, 28)

>>> datetime.datetime.strftime('%Y/%m/%d %H:%M:%S', timeTuple)


>>> s='2015-12-21 15:01:28'
>>> timeTuple = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
time.struct_time(tm_year=2015, tm_mon=12, tm_mday=21, tm_hour=15, tm_min=1, tm_sec=28, tm_wday=0, tm_yday=355, tm_isdst=-1)

>>> time.strftime('%Y/%m/%d %H:%M:%S',timeTuple)
```

```
python中时间日期格式化符号：
  %y 两位数的年份表示（00-99）
  %Y 四位数的年份表示（000-9999）
  %m 月份（01-12）
  %d 月内中的一天（0-31）
  %H 24小时制小时数（0-23）
  %I 12小时制小时数（01-12） 
  %M 分钟数（00=59）
  %S 秒（00-59）
  
  %a 本地简化星期名称
  %A 本地完整星期名称
  %b 本地简化的月份名称
  %B 本地完整的月份名称
  %c 本地相应的日期表示和时间表示
  %j 年内的一天（001-366）
  %p 本地A.M.或P.M.的等价符
  %U 一年中的星期数（00-53）星期天为星期的开始
  %w 星期（0-6），星期天为星期的开始
  %W 一年中的星期数（00-53）星期一为星期的开始
  %x 本地相应的日期表示
  %X 本地相应的时间表示
  %Z 当前时区的名称
  %% %号本身
```

####3. 时间戳
```
>>> time.mktime(time.strptime(s,'%Y-%m-%d %H:%M:%S'))
1450681288.0
>>> int(time.time())

# timestamp to time tuple in UTC
timestamp = 1226527167.595983
time_tuple = time.gmtime(timestamp)
print repr(time_tuple)

# timestamp to time tuple in local time
timestamp = 1226527167.595983
time_tuple = time.localtime(timestamp)
print repr(time_tuple)
```

####4. 日期相加减
```import datetime

now = datetime.datetime.now() # datetime.datetime(2015, 12, 16, 15, 6, 37, 420000)
dayOfweek = datetime.datetime.isoweekday()
if dayOfweek == 1: # Monday
    last_time = now + datetime.timedelta(days=-3)
else:
    last_time = now + datetime.timedelta(days=-1)
```

str转datetime格式举例: 首先在views中引入下方代码 import datetime

下方为转换代码 start_time = '2017年8月5日' datetime_value = datetime.datetime.strptime(start_time, '%Y年%m月%d日') 得到的datetime_value即为可以进行比较的python时间格式

代码如下:
start_time_format = datetime.datetime.strptime(start_time, '%Y年%m月%d日')
    end_time_format = datetime.datetime.strptime(end_time, '%Y年%m月%d日')

    creat_on = Order.objects.all()
    start_datetime  = start_time_format.replace(tzinfo=None)  **(!!!! 如不写会报offset-naive and offset-aware!!!!)** 
    end_datetime  = end_time_format.replace(tzinfo=None) ** (!!!!注意此处要进行格式转换!!!!)** 

    ids = ''
    for i in  creat_on:
        creat_on_timestr = i.created_on
        creat_datetime = creat_on_timestr.replace(tzinfo=None)

        if start_datetime <= creat_datetime and creat_datetime <= end_datetime:



       下方代码实现日期加一天
      end_time_format = end_time_format + datetime.timedelta(days= 1)
