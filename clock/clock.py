import datetime
from datetime import datetime

def today():
    #年月日
    today=datetime.date.today()
    d1=today.strftime("%y_%m_%d")
    return d1

def now():
    #時分秒
    now=datetime.date.today()
    ns=now.strftime("%H h %M m %S s")
    return ns


