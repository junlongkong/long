# -*- coding: utf-8 -*-
#import configparser

class Configuration:
    #dolphindb
    mongodb_url = "mongodb://localhost:27017/"
    mongodb_dbname = "test"
    mongodb_collection = "accountPosition"
    mongodb_collection2 = "orderMonitor"
    mongodb_user = ""
    mongodb_password = ""
    #dolphindb
    dolphindb_ip = "127.0.0.1"
    dolphindb_port = 8848
    dolphindb_dbname = "test_stream"
    dolphindb_actionName = "test"
    dolphindb_user = "admin"
    dolphindb_password = "123456"
    #nats
    nats_url = "nats://127.0.0.1:4222"
    nats_topic = "test"
    #websocket
    websocket_webport = 8765
