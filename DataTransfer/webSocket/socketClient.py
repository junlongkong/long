import asyncio
import websockets

def __init__(self):
    return None

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send('Hello, World!')
        response = await websocket.recv()
        print(f'Received: {response}')

asyncio.get_event_loop().run_until_complete(hello())