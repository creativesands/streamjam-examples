import random
import asyncio
import websockets
from collections import defaultdict
from streamjam import Service, SocketService


class CustomSocketService(SocketService):
    async def on_connect(self, ws: websockets.WebSocketServerProtocol) -> str:
        print('Accepting connection on:', ws.path)
        return ws.path
    

class MultiplayerService(Service):
    def __init__(self):
        self.scores = defaultdict(int)
        self.opponents: dict[str, str] = dict()
        self.last_player = None
        self.game_tasks = set()

    async def join_game(self, pid):
        self.scores[pid] = 0
        if self.last_player is not None:
            # make current player, last player's opponent
            self.opponents[self.last_player] = pid
            self.opponents[pid] = self.last_player
            self.last_player = None
            # start game between players
            self.game_tasks.add(asyncio.create_task(self.start_game(pid, self.opponents[pid])))
        else:
            self.last_player = pid

    async def start_game(self, pid1, pid2):
        print('* READY to start game')
        self.dispatch('countdown', 5, recipients=[pid1, pid2])
        for i in range(5):
            await asyncio.sleep(1)
            self.dispatch('countdown', 4 - i, recipients=[pid1, pid2])
        
        self.dispatch('start-game', recipients=[pid1, pid2])
        
        for _ in range(2):
            x, y  = random.random() * 70, random.random() * 70
            await asyncio.sleep(random.randint(1, 3))
            self.dispatch('start-bonus', (x, y), recipients=[pid1, pid2])
            await asyncio.sleep(2)
            self.dispatch('stop-bonus', recipients=[pid1, pid2])


    async def update_score(self, pid, increment: int):
        self.scores[pid] += increment
        self.dispatch('opponent-score-update', self.scores[pid], recipients=[self.opponents[pid]])
        if self.scores[pid] >= 200:
            self.dispatch('end-game', True, recipients=[pid])
            self.dispatch('end-game', False, recipients=[self.opponents[pid]])
