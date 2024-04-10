import asyncio
from streamjam import StreamJam

from .services.socket import CustomSocketService
from .services.multiplayer import MultiplayerService

app = StreamJam(
    name="click_monger",
    services={
        'SocketService': CustomSocketService.configure(),
        'MultiplayerService': MultiplayerService.configure()
    },
    host='0.0.0.0'
)


if __name__ == '__main__':
    asyncio.run(app.serve())
