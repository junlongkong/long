import pymongo
import os
from utils import config

# 连接数据库
#client = pymongo.MongoClient("mongodb://localhost:27017/")
#db = client["test"]
#collection = db["accountPosition"]

class MongoDatabase:
    def __init__(self, url):
        self.client = pymongo.MongoClient(url)

    def get_connection(self):
        return self.client

    def close_connection(self):
        self.client.close()


class MongoOperations:
    def __init__(self, client, db, collection):
        self.collection = client[db][collection]

    def insert_data(self, data):
        # 执行插入数据的SQL语句
        self.collection.insert_one(data)

    def query_data(self, criteria):
        # 执行查询数据的SQL语句
        results = self.collection.find(criteria)
        return results


if __name__ == '__main__':
    # config = configparser.ConfigParser()
    # 获取当前文件所在目录的上一层目录的路径
    # parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    # 构建上一层目录中ini文件的路径
    # ini_file_path = os.path.join(parent_dir, "Config.ini")
    # config.read(ini_file_path, encoding="utf-8")
    # config.sections()  # 获取section节点

    # config.options('mongodb')  # 获取指定section 的options即该节点的所有键
    # mongoUrl1 = config['mongodb']['url']
    # mongoUrl = config.get("mongodb", "url")  # 获取指定section下的options
    # mongoDbname = config.get("mongodb", "dbname")  # 将获取到值转换为int型
    # mongoCollection = config.get("mongodb", "collection")  # 将获取到值转换为bool型

    # 使用类实例调用实例方法
    client = MongoDatabase(config.Configuration.mongodb_url).get_connection()
    oper = MongoOperations(client, config.Configuration.mongodb_dbname, config.Configuration.mongodb_collection)

    # 插入数据
    student = {"name": "Alice", "student_id": 12345, "age": 20, "gender": "female"}
    oper.insert_data(student)

    # 查询数据
    query = {'unique_key': 'bond_position'}
    results = oper.query_data(query)
    # 打印查询结果
    for result in results:
        print(result)
