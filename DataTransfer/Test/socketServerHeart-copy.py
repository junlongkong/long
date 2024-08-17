from utils import config
import asyncio
import websockets
import time

# 心跳检查间隔（秒）
HEARTBEAT_INTERVAL = 5

# 保存所有的连接
active_connections = set()

if __name__ == '__main__':

    webport = config.Configuration.websocket_webport

    # 保活连接的协程任务
    async def keep_alive(websocket):
        await websocket.send(str(time.time()))  # 发送当前时间作为响应
        active_connections.add(websocket)  # 将新的连接添加到活跃连接集合中

    # 处理连接的协程任务
    async def handler(websocket, path):
        print("Client coming")

        keepalive_task = asyncio.create_task(keep_alive(websocket))
        try:
            while True:
                # 接收消息
                data = await websocket.recv()
                print(f"Received: {data}")
                # 处理消息...
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
        finally:
            active_connections.remove(websocket)  # 从活跃连接集合中移除已关闭的连接
            keepalive_task.cancel()

    # 启动WebSocket服务器
    start_server = websockets.serve(handler, "localhost", webport)
    print(f"webport: {webport} is listening")

    # 创建一个asyncio事件循环
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()



