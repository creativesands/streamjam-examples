import asyncio
from streamjam import StreamJam

from .components.services import CustomSocketService, MultiplayerService

app = StreamJam(
    name="click_monger",
    services={
        'SocketService': CustomSocketService.configure(),
        'MultiplayerService': MultiplayerService.configure()
    }
)


if __name__ == '__main__':
    asyncio.run(app.serve())
