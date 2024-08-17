import time
import threading
import websocket

# WebSocket服务器的URL
ws_url = "ws://localhost:8765"

# 心跳间隔（秒）
heartbeat_interval = 10

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def send_heartbeat(*args):
        while True:
            time.sleep(heartbeat_interval)
            ws.send("heartbeat")  # 发送心跳

    thread = threading.Thread(target=send_heartbeat)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()