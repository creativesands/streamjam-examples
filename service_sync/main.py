import asyncio
from streamjam import StreamJam

from .components.services import CustomSocketService, CounterService


app = StreamJam(
    name="service_sync",
    services={
        'SocketService': CustomSocketService.configure(),
        'CounterService': CounterService.configure(n=0)
    }
)


if __name__ == '__main__':
    asyncio.run(app.serve())
