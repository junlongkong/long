from utils import config
import asyncio
import websockets
import time
import nats
from natsMiddle import operationNats
from mongoDB import insertData

# 心跳检查间隔（秒）
HEARTBEAT_INTERVAL = 5

# 保存所有的连接
active_connections = set()

#websocket
webport = config.Configuration.websocket_webport

#mongo-init
client = insertData.MongoDatabase(config.Configuration.mongodb_url).get_connection()
oper = insertData.MongoOperations(client, config.Configuration.mongodb_dbname, config.Configuration.mongodb_collection)
oper2 = insertData.MongoOperations(client, config.Configuration.mongodb_dbname, config.Configuration.mongodb_collection2)

# 保活连接的协程任务
async def keep_alive(websocket):
    await websocket.send(str(time.time()))  # 发送当前时间作为响应
    active_connections.add(websocket)  # 将新的连接添加到活跃连接集合中

# 处理连接的协程任务
async def handler(websocket, path):
    print("websocket Client coming")

    keepalive_task = asyncio.create_task(keep_alive(websocket))
    try:
        nc = await nats.connect("nats://127.0.0.1:4222")

        while True:
            # 接收消息
            data = await websocket.recv()
            print(f"websocket Received: {data}")
            # 处理消息...
            #await operationNats.operation(b'hello world .....')
            await nc.publish(config.Configuration.nats_topic, bytes(data, 'utf-8'))

    except websockets.exceptions.ConnectionClosed:
        print("websocket Client disconnected")
    finally:
        active_connections.remove(websocket)  # 从活跃连接集合中移除已关闭的连接
        keepalive_task.cancel()


async def listening():
    print("nats listening running")

    nc2 = await nats.connect("nats://127.0.0.1:4222")

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("nats Received a message on '{subject} {reply}': {data}".format(subject=subject, reply=reply, data=data))

        #插入MongoDB中
        # 插入数据-test
        position = {"unique_key" : "bond_position","option_position" : "500","open_position" : "500","short_position" : "500","close_position" : "500",
                    "user_id" : "kongjunlong","account" : "account_02_01"}
        oper.insert_data(position)

        order = {"unique_key": "order_monitor","security_id": "210222.IB","security_name": "21国开22","trade_date": "20240511",
            "trade_breed": "Bond","trade_place": "CFETS","status": "Send","time": "2024-05-22 18:02:15"}
        oper2.insert_data(order)

    try:
        # 订阅消息
        print(f"nats ready to subscribe")
        await nc2.subscribe(config.Configuration.nats_topic, cb=message_handler)
        while True:
            await asyncio.sleep(1)

    except nc2.is_closed:
        print("nas Client disconnected")
    finally:
        # 从活跃连接集合中移除已关闭的连接
        await nc2.close()

# 启动WebSocket服务器
async def websocket_init():
    start_server = await websockets.serve(handler, "localhost", webport)
    print(f"websockets webport: {webport} is listening")


# 创建一个asyncio事件循环
loop = asyncio.get_event_loop()
tasks = [loop.create_task(listening()),loop.create_task(websocket_init())]
res = loop.run_until_complete(asyncio.wait(tasks))

#loop.run_until_complete(start_server)
loop.run_forever()





