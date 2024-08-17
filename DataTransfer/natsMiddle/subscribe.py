from nats.aio.client import Client as NATS
from utils import config
import os


class natsOperation:
    def __init__(self, natsUrl, natsTopic):
        self.natsUrl = natsUrl
        self.natsTopic = natsTopic
        # 创建一个NATS客户端实例
        self.nats_client = NATS()
        # 连接到NATS服务器
        self.nats_client.connect(natsUrl)

    # 定义一个回调函数，用于接收消息
    def msg_handler(msg):
        print(f"Received message: {msg.data.decode()}")

    def subscribe(self):
        # 订阅一个主题
        self.nats_client.subscribe(self.natsTopic, self.msg_handler)
        # 等待一段时间以接收消息
        self.nats_client.wait(1)

    def publish(self, msg):
        # 发布一条消息
        self.nats_client.publish(self.natsTopic, msg)

    def close(self):
        # 关闭客户端连接
        self.nats_client.close()

if __name__ == '__main__':
    natsUrl = config.Configuration.nats_url
    natsTopic = config.Configuration.nats_topic

    # 使用类实例调用实例方法
    oper = natsOperation(natsUrl, natsTopic)

    # pub数据
    student = {"name": "Alice", "student_id": 12345, "age": 20, "gender": "female"}
    oper.publish(student)

    # sub数据
    results = oper.subscribe()
    # 打印查询结果
    for result in results:
        print(result)
