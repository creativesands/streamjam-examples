<script>
    /*---------- BEGIN: STREAMJAM ----------*/

    import { getContext, setContext, onDestroy as __onDestroy } from "svelte"

    import Button from './Button.svelte'

    export let id = "root"

    /* Props */
    export let count = 0
    export let text = ""

    const __client = getContext("streamjam")
    const __parentId = getContext("__parentId")
    const __hasServer = true
    const __should_create_component = __hasServer && (!__client.isRestored || !(id in __client.state))
    const __self = __client.newComponent(id, __parentId, __should_create_component, 'Root', {count, text})
    id && setContext("__parentId", id)

    /* Shadow Stores Init */
    let _count
    let _text

    if (__client.state &&  id in __client.state) {
        _count = __self.newStore('count', __client.state[id]['count'])
        _text = __self.newStore('text', __client.state[id]['text'])
    } else {
        _count = __self.newStore('count', count)
        _text = __self.newStore('text', text)
    }

    /* Shadow Stores Reactive Get */
    $: count = $_count
    $: text = $_text

    /* Shadow Stores Reactive Set */
    $: if ($_count !== count) _count.set(count)
    $: if ($_text !== text) _text.set(text)

    /* Proxy RPCs */
    const counter_service = __self.proxyRPC('counter_service')
    const inc = __self.proxyRPC('inc')

    /* Destroy Component */
    __onDestroy(() => {
        __client.destroyComponent(__self)
    })

    /*---------- END: STREAMJAM ----------*/

    
</script>

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
        