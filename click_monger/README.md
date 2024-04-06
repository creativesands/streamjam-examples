# Click Monger (Multiplayer PvP Game)

## Setup:

> NOTE: As of Apr 6 2024, StreamJam apps are not exposed to network by default. Follow the steps below to make StreamJam apps accessible to other devices in the network.

1. Update main.py to specify host as '0.0.0.0' when initializing StreamJam app.

```python
app = StreamJam(
    ...,
    host='0.0.0.0'
)
```

2. Update `/.build/src/App.svelte` to modify the WS address with your local IP:

```js
const client = new StreamJamClient(`ws://192.168.1.XXX:7755/${client_id}`)
```


3. Update `/.build/package.json` to add `--host` to dev script:

```json
 "scripts": {
    "dev": "vite --host",
    "build": "vite build",
    "preview": "vite preview"
  }
```

4. Each player is differentiated by the URL. (http://{ ip }:5173/{ id }) For example:
    - Player 1: `http://192.168.1.XXX:5173/1`
    - Player 2: `http://192.168.1.XXX:5173/2`

    Matchmaking strategy: new players (with different IDs) are paired for a match.

5. Match will commence as soon as two players join.

6. Click your way to victory!

---

## Files to look at:

- `/components/root.py`
- `/components/services.py`
