import asyncio
import nats
import time
from nats.errors import ConnectionClosedError, TimeoutError, NoServersError
from utils import config

async def operation(msg):

    nc = await nats.connect("nats://127.0.0.1:4222")
    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    sub = await nc.subscribe(config.Configuration.nats_topic, cb=message_handler)

    #time.sleep(2)  # 暂停5秒
    await nc.publish(config.Configuration.nats_topic, msg)


if __name__ == '__main__':
    #asyncio.run(operation(b'Hello World !!!!!'))
    tasks = [operation(b'Hello World !!!!!')]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_forever()
    #loop.close()