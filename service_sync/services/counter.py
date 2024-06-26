from streamjam import Service


class CounterService(Service):
    def __init__(self, n):
        self.count = 0
        self.text = ''

    async def get_count(self):
        return self.count
    
    async def set_count(self, value):
        self.count = value 

    async def inc(self):
        self.count += 1
        self.dispatch('counter-update', {'count': self.count})

    async def dec(self):
        self.count -= 1
        self.dispatch('counter-update', {'count': self.count})

    async def get_text(self):
        return self.text
    
    async def set_text(self, text):
        self.text = text
        self.dispatch('text-update', {'text': self.text})

