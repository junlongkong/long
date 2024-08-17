import datetime
import threading

from mongoDB import insertData
from natsMiddle import subscribe
from webSocket import socketServerHeart
from dolphinDB import subscribe
from utils import config
import nats

if __name__ == "__main__":
    current_time = datetime.datetime.now()
    print("main: " + str(current_time))

    # #dolphin
    # sessionTemp = subscribe.DolphinDatabase().get_session()
    # oper = subscribe.DolphinOperations(sessionTemp)
    #
    # oper.subscribe(config.Configuration.dolphindb_ip, config.Configuration.dolphindb_port,
    #                config.Configuration.dolphindb_dbname, config.Configuration.dolphindb_actionName)
    #
    # # mongodb
    # client = insertData.MongoDatabase(config.Configuration.mongodb_url).get_connection()
    # oper = insertData.MongoOperations(client, config.Configuration.mongodb_dbname, config.Configuration.mongodb_collection)
    #
    # # 插入数据
    # student = {"name": "Alice", "student_id": 12345, "age": 20, "gender": "female"}
    # oper.insert_data(student)
    #
    # # 查询数据
    # query = {'unique_key': 'bond_position'}
    # results = oper.query_data(query)
    # # 打印查询结果
    # for result in results:
    #     print(result)


    # 在新线程中运行函数
    #thread = threading.Thread(target=socketServerHeart, args=(socketInstance, "Thread-1",))
    #thread.start()

    print("main all component init over")

