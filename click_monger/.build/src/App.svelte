<script>
    import { setContext } from "svelte"
    import { StreamJamClient, DevTools } from "streamjam"
    import Root from "./components/Root.svelte"

    const client_id = window.location.pathname.substring(1)

    if (!client_id) {
        window.location.href += 'default-client'
    }

    const client = new StreamJamClient(`ws://192.168.1.78:7755/${client_id}`)
    let client_connection = client.connect()

    setContext('streamjam', client)
    setContext('__parentId', 'root')
</script>

{#await client_connection}
    Connecting...
{:then _}
    <Root/>
{/await}

<DevTools/>
