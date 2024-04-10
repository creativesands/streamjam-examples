import asyncio
from streamjam import StreamJam

from .services.multiplayer import MultiplayerService

app = StreamJam(
    name="click_monger",
    services={
        'MultiplayerService': MultiplayerService.configure()
    },
    host='0.0.0.0'
)


if __name__ == '__main__':
    asyncio.run(app.serve())
