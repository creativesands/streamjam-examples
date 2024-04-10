import websockets
from streamjam import SocketService


class CustomSocketService(SocketService):
    async def on_connect(self, ws: websockets.WebSocketServerProtocol) -> str:
        """
        Example of a custom on_connect method that uses the path of the websocket as the session id.
        This is the default implementation of on_connect of SocketService anyway.
        """
        print('Accepting connection on:', ws.path)
        return ws.path
