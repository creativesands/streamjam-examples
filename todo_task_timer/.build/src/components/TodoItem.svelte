<script>
    /*---------- BEGIN: STREAMJAM ----------*/

    import { getContext, setContext, onDestroy as __onDestroy } from "svelte"

    

    export let id = null

    /* Props */
    export let done = false
    export let text = ""
    export let time = 0
    export let is_running = false

    const __client = getContext("streamjam")
    const __parentId = getContext("__parentId")
    const __hasServer = true
    const __should_create_component = __hasServer && (!__client.isRestored || !(id in __client.state))
    const __self = __client.newComponent(id, __parentId, __should_create_component, 'TodoItem', {done, text, time, is_running})
    id && setContext("__parentId", id)

    /* Shadow Stores Init */
    let _done
    let _text
    let _time
    let _is_running

    if (__client.state &&  id in __client.state) {
        _done = __self.newStore('done', __client.state[id]['done'])
        _text = __self.newStore('text', __client.state[id]['text'])
        _time = __self.newStore('time', __client.state[id]['time'])
        _is_running = __self.newStore('is_running', __client.state[id]['is_running'])
    } else {
        _done = __self.newStore('done', done)
        _text = __self.newStore('text', text)
        _time = __self.newStore('time', time)
        _is_running = __self.newStore('is_running', is_running)
    }

    /* Shadow Stores Reactive Get */
    $: done = $_done
    $: text = $_text
    $: time = $_time
    $: is_running = $_is_running

    /* Shadow Stores Reactive Set */
    $: if ($_done !== done) _done.set(done)
    $: if ($_text !== text) _text.set(text)
    $: if ($_time !== time) _time.set(time)
    $: if ($_is_running !== is_running) _is_running.set(is_running)

    /* Proxy RPCs */
    const remove_item = __self.proxyRPC('remove_item')
    const start_timer = __self.proxyRPC('start_timer')
    const stop_timer = __self.proxyRPC('stop_timer')

    /* Destroy Component */
    __onDestroy(() => {
        __client.destroyComponent(__self)
    })

    /*---------- END: STREAMJAM ----------*/

    
</script>

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
        