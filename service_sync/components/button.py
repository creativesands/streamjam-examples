from streamjam import Component, ComponentEvent


class Button(Component):
    title: str = ''

    class UI:
        """@
        <button on:click={handle_click}>{title}</button>
        """

    @Component.rpc
    async def handle_click(self, e: ComponentEvent):
        self.dispatch('Button.click') 
