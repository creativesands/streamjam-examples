<script>
    /*---------- BEGIN: STREAMJAM ----------*/

    import { getContext, setContext, onDestroy as __onDestroy } from "svelte"

    import TodoInput from './TodoInput.svelte'
    import TodoItem from './TodoItem.svelte'

    export let id = "root"

    /* Props */
    export let new_todo = ""
    export let todos = []

    const __client = getContext("streamjam")
    const __parentId = getContext("__parentId")
    const __hasServer = true
    const __should_create_component = __hasServer && (!__client.isRestored || !(id in __client.state))
    const __self = __client.newComponent(id, __parentId, __should_create_component, 'Root', {new_todo, todos})
    id && setContext("__parentId", id)

    /* Shadow Stores Init */
    let _new_todo
    let _todos

    if (__client.state &&  id in __client.state) {
        _new_todo = __self.newStore('new_todo', __client.state[id]['new_todo'])
        _todos = __self.newStore('todos', __client.state[id]['todos'])
    } else {
        _new_todo = __self.newStore('new_todo', new_todo)
        _todos = __self.newStore('todos', todos)
    }

    /* Shadow Stores Reactive Get */
    $: new_todo = $_new_todo
    $: todos = $_todos

    /* Shadow Stores Reactive Set */
    $: if ($_new_todo !== new_todo) _new_todo.set(new_todo)
    $: if ($_todos !== todos) _todos.set(todos)

    /* Proxy RPCs */
    

    /* Destroy Component */
    __onDestroy(() => {
        __client.destroyComponent(__self)
    })

    /*---------- END: STREAMJAM ----------*/

    
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
        