import asyncio
import json

from quart import Quart, websocket

app = Quart(__name__)
STATE = {}
loop = asyncio.get_event_loop()
UPDATED = asyncio.Queue(loop=loop)


@app.route('/<int:user>')
async def index(user):
    global UPDATED
    UPDATED.put_nowait(user)
    return 'hello'


@app.route('/update/<int:user>')
async def update(user):
    global UPDATED
    UPDATED.put_nowait(user)
    return 'udpated!!'


@app.websocket('/ws')
async def ws():
    global UPDATED
    while True:
        await UPDATED.get()
        await websocket.send(json.dumps({'type': 'state', **STATE}))
        UPDATED.task_done()


if __name__ == "__main__":
    app.run(loop=loop, host='0.0.0.0', port='5000')
