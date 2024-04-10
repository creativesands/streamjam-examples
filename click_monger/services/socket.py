import websockets
from streamjam import SocketService


class CustomSocketService(SocketService):
    async def on_connect(self, ws: websockets.WebSocketServerProtocol) -> str:
        print('Accepting connection on:', ws.path)
        return ws.path
