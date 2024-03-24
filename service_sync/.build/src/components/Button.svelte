<script>
    /*---------- BEGIN: STREAMJAM ----------*/

    import { getContext, setContext, onDestroy as __onDestroy } from "svelte"

    

    export let id = null

    /* Props */
    export let title = ""

    const __client = getContext("streamjam")
    const __parentId = getContext("__parentId")
    const __hasServer = true
    const __should_create_component = __hasServer && (!__client.isRestored || !(id in __client.state))
    const __self = __client.newComponent(id, __parentId, __should_create_component, 'Button', {title})
    id && setContext("__parentId", id)

    /* Shadow Stores Init */
    let _title

    if (__client.state &&  id in __client.state) {
        _title = __self.newStore('title', __client.state[id]['title'])
    } else {
        _title = __self.newStore('title', title)
    }

    /* Shadow Stores Reactive Get */
    $: title = $_title

    /* Shadow Stores Reactive Set */
    $: if ($_title !== title) _title.set(title)

    /* Proxy RPCs */
    const handle_click = __self.proxyRPC('handle_click')

    /* Destroy Component */
    __onDestroy(() => {
        __client.destroyComponent(__self)
    })

    /*---------- END: STREAMJAM ----------*/

    
</script>

        <button on:click={handle_click}>{title}</button>
        