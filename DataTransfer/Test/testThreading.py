import asyncio
import threading
import websockets

async def echo(websocket, path):
    #async for message in websocket:
        #await websocket.send(message)
    print("0000000")

def start_websocket_server():
    start_server = websockets.serve(echo, "localhost", 8765)
    #asyncio.run(start_server)


# 创建并启动线程
thread = threading.Thread(target=start_websocket_server)
thread.start()