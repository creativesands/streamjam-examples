from streamjam import Component


class TodoInput(Component):
    text: str = ""

    class UI:
        """@
        <input 
            type="text" 
            bind:value={text} 
            placeholder="What do you want to do?"
            on:keydown="{(e) => { e.code === 'Enter' && new_todo(text) }}"
        />

        <style>
        input {
            padding: 20px;
            font-size: 18px;
            color: black;
            width: 100%;
            background-color: transparent;
            border: none;
            box-sizing: border-box;
            border-bottom: 1px solid rgb(52, 52, 52);
            transition: 0.3s ease;
        }

        input:active,
        input:focus {
            background-color: white;
            outline: none;
        }
        </style>
        """

    @Component.rpc
    async def new_todo(self, text):
        self.dispatch('new-todo', text)
        self.text = ""