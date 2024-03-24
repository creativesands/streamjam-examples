import json
import typing as tp
from streamjam import Component, ComponentEvent

from .todo_item import TodoItem
from .todo_input import TodoInput


count = 0


class Root(Component):
    new_todo: str = ""
    todos: tp.List = [
        # {"id": "todo-1", "done": True, "text": "Example"} 
    ]
    
    class UI: 
        """@
        <script>
        console.log('Root has mounted')
        </script>

        <div class="wrapper">
            <h1>
                <span><span class="bold">StreamJam</span> Stuff To Do</span>
            </h1>
            <div class="container">
                <div class="input">
                    <TodoInput id="new-todo-input" text={new_todo}/>
                </div>
                <div class="todos">
                    {#each todos as todo (todo.id)}
                        <TodoItem id={todo.id} done={todo.done} text={todo.text} />
                    {/each}
                </div>
            </div>
        </div>

        <style>
        :global(:root) {
            background: #f8f7f4;
            color: black;
        }

        .wrapper {
            max-width: 600px;
            margin: 10rem auto 2rem;
        }

        h1 {
            font-weight: lighter;
            text-transform: uppercase;
            color: black;
            letter-spacing: 3px;
            font-size: 25px;
        }

        h1 span {
            padding-bottom: 8px;
            border-bottom: 1px solid rgb(52, 52, 52);
        }

        .container {
            margin-top: 3rem;
            display: flex;
            flex-direction: column;
            border: 1px solid rgb(52, 52, 52); 
        }

        .bold {
            font-weight: bold;
        }
        </style>
        """

    async def __post_init__(self):
        try:
            self.todos = json.loads(open('./todos.json').read())
            global count
            count = max([int(t['id'].split('-')[-1]) for t in self.todos])
            print('Loading data', self.__state__, id(self))
        except:
            print('No data to load or error on load')
            self.todos = []
    
    @Component.on_event('remove-todo')
    async def handle_remove(self, e: ComponentEvent):
        remove_id =  e.data
        self.todos = [todo for todo in self.todos if todo['id'] != remove_id]

    @Component.on_event('new-todo')
    async def add_new_todo(self, e: ComponentEvent):
        global count
        count += 1
        self.todos.append({
            "id": f'todo-{count}',
            "done": False,
            "text": e.data
        })
        self.todos = self.todos 

    @Component.on_event('toggle-todo')
    async def toggle_todo(self, e: ComponentEvent):
        for todo in self.todos:
            if todo['id'] == e.data['id']:
                todo['done'] = e.data['done'] 
        self.todos = self.todos

    async def on_disconnect(self):
        print('Client disconnected. Dumping data.', self.__state__, id(self))
        with open('./todos.json', 'w') as file:
            json.dump(self.todos, file)
