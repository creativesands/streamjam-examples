import asyncio
from typing import Literal
from streamjam import Component, ServiceClient, ServiceEvent

from .services import MultiplayerService


class Root(Component):
    state: Literal["WAITING", "COUNTDOWN", "PLAYING", "FINISHED"] = "WAITING"
    click_counter: int = 0
    ready_countdown: int = 0
    current_bonus: int = 0
    timer: int = 10
    score: int = 0
    result: bool = False
    opponent_score: int = 0
    opponent_click_counter: int = 0
    bonus_x: float = 0.0
    bonus_y: float = 0.0

    multiplayer_service = ServiceClient(MultiplayerService, 'MultiplayerService')

    class UI:
        """@
        <div class="wrapper">
            <h1 class="logo"><span class="logo-click">Click</span><span class="logo-monger">Monger</span></h1>

            <div class="header">
                {#if state === 'WAITING'}
                    <div class="message">Waiting for an opponent to join...</div>
                {:else if state === 'COUNTDOWN'}
                    <div class="message">Prepare for your Click Battle!</div>
                {:else if state === 'PLAYING'}
                    <div class="timer">00:{String(timer).padStart(2, '0')}</div>
                {:else if state === 'FINISHED'}
                    <div class="message">Game Over. <button on:click={new_game}>New Match</button></div>
                {/if}
            </div>

            <div class="score-container">
                <div class="target-score">200</div>
                <div class="score-strip">
                    <div class="score-bg">
                        <div class="self" style="width: {Math.min(score/4, 50)}%"></div>
                        <div class="opponent" style="width: {Math.min(opponent_score/4, 50)}%"></div>
                    </div>
                    <div class="mid-line"></div>
                    <div class="scores">
                        <div>{score}</div>
                        <div>{opponent_score}</div>
                    </div>
                </div>
                <div class="stats">
                    <div>{click_counter/10} clicks/s</div>
                    <div>{opponent_click_counter/10} clicks/s</div>
                </div>
            </div>

            <button class="click-pad" disabled={state !== 'PLAYING'} on:click={handle_click}>
                {#if state === 'COUNTDOWN'}
                    <div class="countdown">
                        <p>{ready_countdown}</p>
                    </div>
                {:else if state === 'FINISHED'}
                    <span>You {result ? 'Won! 😎' : 'Lost! 🙄'}</span>
                {:else}
                    <div class="tap">TAP</div>
                {/if}
                {#if current_bonus > 0}
                    <button 
                        class="bonus-pad" 
                        style="left: {bonus_x}%; top: {bonus_y}%"
                        on:click|stopPropagation={handle_bonus_click}
                    >
                        +{current_bonus}
                    </button>
                {/if}
            </button>

            <div class="footer">
                <p class="rules">Keep clicking on the target. Click on the timed targets for bonus points.</p>
            </div>
        </div>

        <style>
        .wrapper {
            width: 75%;
            min-width: 350px;
            max-width: 800px;
            margin: 10vh auto;
            display: flex;
            justify-content: center;
            flex-direction: column;
            gap: 6vh;
        }

        .logo {
            font-size: 64px;
            text-align: center;
            font-weight: 900;
            font-family: 'Inter', Helvetica, sans-serif;
            margin: 0;
        }

        .logo-click {
            color: #8A54FF;
            display: inline-block;
            rotate: -6deg;
        }

        .logo-monger {
            color: #4ECE89;
            display: inline-block;
            rotate: 3deg;
            transform: translate(4px, 8px);
        }

        .header {
            display: flex;
            justify-content: center;
        }

        .header .message {}

        .timer {
            border: 3px solid #272727;
            background-color: #1B1B1B;
            border-radius: 50px;
            padding: 8px 35px;
            font-size: 1.3rem;
            font-weight: bold;
            color: white;
            letter-spacing: 2px;
        }

        .score-container {}

        .target-score {
            text-align: center;
            font-weight: bold;
            font-size: 1.3rem;
            color: white;
        }

        .score-strip {
            height: 40px;
            border-radius: 50px;
            overflow: hidden;
            position: relative;
            margin: 1vh 0;
        }

        .scores {
            position: relative;
            display: flex;
            justify-content: space-between;
            padding: 0 20px;
            height: 100%;
            align-items: center;
            font-size: 1rem;
            font-weight: bold;
            color: white;
        }

        .mid-line {
            position: absolute;
            width: 4px;
            background: #ffffff17;
            left: calc(50% - 2px);
            top: 0;
            height: 100%;
        }

        .score-bg {
            height: 100%;
            width: 100%;
            background: #2D2D2D;
            position: absolute;
            top: 0;
            left: 0;
        }

        .score-bg .self {
            position: absolute;
            top: 0;
            left: 0;
            background: #8A54FF;
            height: 100%;
            width: 40%;
        }

        .score-bg .opponent {
            position: absolute;
            top: 0;
            right: 0;
            background: #4ECE89;
            height: 100%;
            width: 40%;
        }

        .stats {
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            padding: 0 20px;
        }

        .click-pad {
            height: 25vh;
            background: #3A3A3A;
            border-radius: 20px;
            border: none;
            border-bottom: 4px solid #2C2C2C;
            min-height: 100px;
            cursor: pointer;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            user-select: none;
            font-size: 1.25rem;
            color: #737373;
            touch-action: manipulation;
        }

        .bonus-pad {
            background-color: #B99258;
            border: none;
            border-bottom: 4px solid #896B3E;
            border-radius: 18px;
            padding: 12px 30px;
            font-weight: bold;
            font-size: 1rem;
            position: absolute;
            top: 10%;
            left: 20%;
            color: white;
            touch-action: manipulation;
            user-select: none;
        }

        .bonus-pad:active {
            transform: scale(0.975);
        }

        .countdown {
            text-align: center;
        }

        .countdown p {
            font-size: 2rem;
            margin: 1rem 0;
            color: white;
            font-weight: bold;
        }

        .tap {
            font-size: 10px;
            letter-spacing: 10px;
            color: #737373;
        }

        .footer {
            text-align: center;
        }

        @media only screen 
        and (min-device-width: 375px) 
        and (max-device-width: 812px) 
        and (-webkit-min-device-pixel-ratio: 3) {
            .logo {
                font-size: 45px;
            }

            .wrapper {
                margin: 4vh auto;
                gap: 4vh;
            }

            .click-pad {
                max-height: 180px;
            }
        }
        </style>
        """

    async def __post_init__(self):
        self.pid = self._session.id + '/root'
        await self.multiplayer_service.join_game(self.pid)
        self.timer_task = None

    @Component.rpc
    async def handle_click(self, e):
        self.score += 1
        self.click_counter += 1
        await self.multiplayer_service.update_score(self.pid, 1)

    @Component.rpc
    async def handle_bonus_click(self, e):
        self.score += self.current_bonus
        await self.multiplayer_service.update_score(self.pid, self.current_bonus)
        self.current_bonus -= 1

    @Component.rpc
    async def new_game(self, e):
        self.score = 0
        self.opponent_score = 0
        self.click_counter = 0
        self.state = 'WAITING'
        self.timer = 10
        await self.multiplayer_service.join_game(self.pid)

    @multiplayer_service.on_event('countdown')
    async def update_countdown_ready(self, e: ServiceEvent):
        self.ready_countdown = e.data

    @multiplayer_service.on_event('start-countdown')
    async def start_countdown(self, e: ServiceEvent):
        self.state = "COUNTDOWN"
    
    @multiplayer_service.on_event('start-game')
    async def start_timer(self, e: ServiceEvent):
        print(self.pid, 'starting game')
        self.state = "PLAYING"
        self.timer_task = asyncio.create_task(self.update_timer())

    @multiplayer_service.on_event('start-bonus')
    async def start_bonus(self, e: ServiceEvent):
        self.bonus_x, self.bonus_y = e.data
        self.current_bonus = 5

    @multiplayer_service.on_event('stop-bonus')
    async def stop_bonus(self, e: ServiceEvent):
        self.current_bonus = 0

    @multiplayer_service.on_event('opponent-score-update')
    async def update_opponent_score(self, e: ServiceEvent):
        self.opponent_score = e.data

    @multiplayer_service.on_event('end-game')
    async def announce_result(self, e: ServiceEvent):
        self.state = "FINISHED"
        self.result = e.data

    async def update_timer(self):
        for _ in range(10):
            await asyncio.sleep(1)
            self.timer -= 1
        self.state = "FINISHED"
        self.result = self.score > self.opponent_score
    