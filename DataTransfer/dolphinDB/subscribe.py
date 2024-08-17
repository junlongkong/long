from threading import Event
from utils import config
import dolphindb as ddb
import numpy as np
import os

class DolphinDatabase:
    def get_session(self):
        # 创建连接
        self.session = ddb.session()
        self.session.enableStreaming()
        return self.session

class DolphinOperations:
    def __init__(self, session):
        self.session = session

    def handler(self,lst):
        print(lst)

    def subscribe(self, dolphindbIp, dolphindbPort, dolphindbDbname, dolphindbActionName):
        # 订阅
        self.session.subscribe(dolphindbIp, dolphindbPort, self.handler, dolphindbDbname, dolphindbActionName)
        #s.subscribe("192.168.1.103",8921,handler,"trades","action",0,False,np.array(['000905']),)
        #print('waiting data coming')
        Event().wait()

    def unsubscribe(self, dolphindbIp, dolphindbPort, dolphindbTableName, dolphindbActionName):
        # 取消订阅
        self.session.unsubscribe(dolphindbIp,dolphindbPort,dolphindbTableName,dolphindbActionName)

if __name__ == '__main__':
    # 使用类实例调用实例方法
    sessionTemp = DolphinDatabase().get_session()
    oper = DolphinOperations(sessionTemp)

    oper.subscribe(config.Configuration.dolphindb_ip, config.Configuration.dolphindb_port,
                   config.Configuration.dolphindb_dbname, config.Configuration.dolphindb_actionName)


