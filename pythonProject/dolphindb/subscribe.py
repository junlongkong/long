from threading import Event
import dolphindb as ddb
import pandas as pd
import numpy as np
s=ddb.session()
#设定本地端口20001用于订阅流数据
s.enableStreaming(20001)
def handler(lst):
    print(lst)
# 订阅DolphinDB(本机8848端口)上的OHLC流数据表
# offset -1: 实时，0: 从头订阅
s.subscribe("127.0.0.1", 8848, handler, "OHLC","python_api_subscribe",-1)
Event().wait()