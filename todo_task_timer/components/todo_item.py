import asyncio
from streamjam import Component


class TodoItem(Component): 
    done: bool = False
    text: str = ''
    time: int = 0
    is_running: bool = False

    class UI:
        """@
        <div class="container">
            <div class="group">
                <input type="checkbox" bind:checked={done}/> 
                <span class="text" class:completed={done}>{text}</span>
            </div>
            <div class="small group">
                <div class="time">
                    {Math.floor(time / 3600)}h {Math.floor(time % 3600 / 60)}m {time % 60}s
                </div>
                {#if is_running}
                    <button on:click={stop_timer} class="btn active">Stop</button>
                {:else}
                    <button on:click={start_timer} class="btn">Start</button>
                {/if}
                <button on:click={remove_item} class="btn remove">—</button>
            </div>
        </div>

        <style>
        .container {
            display: flex;
            align-items: center;
            padding: 7px;
            justify-content: space-between;
            border-bottom: 1px solid rgb(52, 52, 52);
        }

        .container:last-child {
            border-bottom: none;
        }

        .group {
            display: flex;
            gap: 10px;
        }

        .small.group {
            gap: 5px;
        }

        .btn {
            padding: 5px 10px;
            font-size: 10px;
            background-color: black;
            border: none;
            border-radius: 20px;
        }

        .btn.active {
            background-color: #7527E9;
        }

        .remove:hover {
            background-color: #fe6c62;
        }

        .completed {
            text-decoration: line-through;
            opacity: 0.5;
        }

        .time {
            font-family: monospace;
            font-size: 14px;
        }
        </style>
        """


    async def __post_init__(self):
        self.timer_task = None

    @Component.rpc
    async def remove_item(self, e):
        self.dispatch('remove-todo', self.id)

    async def run_timer(self):
        while True:
            if self.is_running:
                await asyncio.sleep(1)
                self.time += 1
            else:
                break

    @Component.rpc
    async def start_timer(self, e):
        self.is_running = True
        self.timer_task = asyncio.create_task(self.run_timer())

    @Component.rpc
    async def stop_timer(self, e):
        self.is_running = False

    @Component.on_update('done')
    async def update_done(self, done):
        self.dispatch('toggle-todo', {'id': self.id, 'done': done}) 
        return done
    
    async def on_destroy(self):
        if self.timer_task:
            did_cancel = self.timer_task.cancel()
            print(self, f'{did_cancel=}. Destructing.')
