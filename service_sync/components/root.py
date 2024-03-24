from streamjam import Component, ServiceClient, ComponentEvent, ServiceEvent

from .button import Button
from .services import CounterService


class Root(Component):
    count: int = 0
    text: str = ''
    
    counter_service = ServiceClient(CounterService, 'CounterService') 
    
    class UI: 
        """@
        <div class="row">
            <Button id='counter-button-dec' title="- 1" />
            <p>{count}</p>
            <Button id='counter-button-inc' title="+ 1" />
        </div>
        <input type="text" bind:value={text} placeholder="Sync text here">

        <style>
        .row {
            display: flex;
            gap: 10px;
        }

        input {
            display: block;
            width: 80%;
            max-width: 800px;
            padding: 5px;
            margin-top: 1em;
        }
        </style>
        """ 

    async def __post_init__(self):
        self.count = await self.counter_service.get_count()
        self.text = await self.counter_service.get_text()

    @Component.rpc
    async def inc(self, e: ComponentEvent):
        await self.counter_service.inc() 

    @Component.on_update('text')
    async def set_text(self, text):
        await self.counter_service.set_text(text)
        return text

    @Component.on_event('Button.click')
    async def update_count_value(self, e: ComponentEvent):
        if e.source.id == 'counter-button-inc':
            await self.counter_service.inc()
        elif e.source.id == 'counter-button-dec':
            await self.counter_service.dec()

    @counter_service.on_event('counter-update')
    async def update_count(self, e: ServiceEvent):
        self.count = e.data['count'] 

    @counter_service.on_event('text-update')
    async def update_text(self, e: ServiceEvent): 
        self.text = e.data['text']
