import datetime
from datetime import datetime
import time

def today():
    #年月日
    today=datetime.now()
    d1=today.strftime("20%y年%m月%d日")
    return d1

def now():
    #時分秒
    now=datetime.now()
    ns=now.strftime("%H時%M分%S秒")
    return ns

def timezone():
    #現在地のタイムゾーンを取得
    now=datetime.now()
    nowtz=now.astimezone()
    heretz=nowtz.tzinfo
    tzn=heretz.tzname(nowtz)
    return tzn
