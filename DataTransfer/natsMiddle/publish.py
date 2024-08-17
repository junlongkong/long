from nats.aio.client import Client as NATS

# 创建一个NATS客户端实例
nats_client = NATS()

# 连接到NATS服务器
nats_client.connect("nats://127.0.0.1:4222")

# 等待一段时间以接收消息
#nats_client.wait(1)

# 关闭客户端连接
#nats_client.close()