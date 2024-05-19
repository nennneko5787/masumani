from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import socketio

from paths import index

fastapi = FastAPI()
fastapi.include_router(index.router)
fastapi.mount("/static", StaticFiles(directory="static"), name="static")

@fastapi.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, fastapi)

@sio.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')

@sio.event
def disconnect(sid):
    print('disconnected', sid)
