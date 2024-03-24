<script>
    /*---------- BEGIN: STREAMJAM ----------*/

    import { getContext, setContext, onDestroy as __onDestroy } from "svelte"

    

    export let id = null

    /* Props */
    export let text = ""

    const __client = getContext("streamjam")
    const __parentId = getContext("__parentId")
    const __hasServer = true
    const __should_create_component = __hasServer && (!__client.isRestored || !(id in __client.state))
    const __self = __client.newComponent(id, __parentId, __should_create_component, 'TodoInput', {text})
    id && setContext("__parentId", id)

    /* Shadow Stores Init */
    let _text

    if (__client.state &&  id in __client.state) {
        _text = __self.newStore('text', __client.state[id]['text'])
    } else {
        _text = __self.newStore('text', text)
    }

    /* Shadow Stores Reactive Get */
    $: text = $_text

    /* Shadow Stores Reactive Set */
    $: if ($_text !== text) _text.set(text)

    /* Proxy RPCs */
    const new_todo = __self.proxyRPC('new_todo')

    /* Destroy Component */
    __onDestroy(() => {
        __client.destroyComponent(__self)
    })

    /*---------- END: STREAMJAM ----------*/

    
</script>

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
        