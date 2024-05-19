from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import socketio

from paths import index

fastapi = FastAPI()
fastapi.include_router(index.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, fastapi)

@sio.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')

@sio.event
def disconnect(sid):
    print('disconnected', sid)
