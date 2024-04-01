<script>
    /*---------- BEGIN: STREAMJAM ----------*/

    import { getContext, setContext, onDestroy as __onDestroy } from "svelte"

    

    export let id = "root"

    /* Props */
    export let score = 0
    export let click_counter = 0
    export let timer = 10
    export let ready_countdown = 0
    export let current_bonus = 0
    export let ready = false
    export let game_over = false
    export let result = false
    export let opponent_joined = false
    export let opponent_score = 0
    export let opponent_click_counter = 0
    export let bonus_x = 0.0
    export let bonus_y = 0.0

    const __client = getContext("streamjam")
    const __parentId = getContext("__parentId")
    const __hasServer = true
    const __should_create_component = __hasServer && (!__client.isRestored || !(id in __client.state))
    const __self = __client.newComponent(id, __parentId, __should_create_component, 'Root', {score, click_counter, timer, ready_countdown, current_bonus, ready, game_over, result, opponent_joined, opponent_score, opponent_click_counter, bonus_x, bonus_y})
    id && setContext("__parentId", id)

    /* Shadow Stores Init */
    let _score
    let _click_counter
    let _timer
    let _ready_countdown
    let _current_bonus
    let _ready
    let _game_over
    let _result
    let _opponent_joined
    let _opponent_score
    let _opponent_click_counter
    let _bonus_x
    let _bonus_y

    if (__client.state &&  id in __client.state) {
        _score = __self.newStore('score', __client.state[id]['score'])
        _click_counter = __self.newStore('click_counter', __client.state[id]['click_counter'])
        _timer = __self.newStore('timer', __client.state[id]['timer'])
        _ready_countdown = __self.newStore('ready_countdown', __client.state[id]['ready_countdown'])
        _current_bonus = __self.newStore('current_bonus', __client.state[id]['current_bonus'])
        _ready = __self.newStore('ready', __client.state[id]['ready'])
        _game_over = __self.newStore('game_over', __client.state[id]['game_over'])
        _result = __self.newStore('result', __client.state[id]['result'])
        _opponent_joined = __self.newStore('opponent_joined', __client.state[id]['opponent_joined'])
        _opponent_score = __self.newStore('opponent_score', __client.state[id]['opponent_score'])
        _opponent_click_counter = __self.newStore('opponent_click_counter', __client.state[id]['opponent_click_counter'])
        _bonus_x = __self.newStore('bonus_x', __client.state[id]['bonus_x'])
        _bonus_y = __self.newStore('bonus_y', __client.state[id]['bonus_y'])
    } else {
        _score = __self.newStore('score', score)
        _click_counter = __self.newStore('click_counter', click_counter)
        _timer = __self.newStore('timer', timer)
        _ready_countdown = __self.newStore('ready_countdown', ready_countdown)
        _current_bonus = __self.newStore('current_bonus', current_bonus)
        _ready = __self.newStore('ready', ready)
        _game_over = __self.newStore('game_over', game_over)
        _result = __self.newStore('result', result)
        _opponent_joined = __self.newStore('opponent_joined', opponent_joined)
        _opponent_score = __self.newStore('opponent_score', opponent_score)
        _opponent_click_counter = __self.newStore('opponent_click_counter', opponent_click_counter)
        _bonus_x = __self.newStore('bonus_x', bonus_x)
        _bonus_y = __self.newStore('bonus_y', bonus_y)
    }

    /* Shadow Stores Reactive Get */
    $: score = $_score
    $: click_counter = $_click_counter
    $: timer = $_timer
    $: ready_countdown = $_ready_countdown
    $: current_bonus = $_current_bonus
    $: ready = $_ready
    $: game_over = $_game_over
    $: result = $_result
    $: opponent_joined = $_opponent_joined
    $: opponent_score = $_opponent_score
    $: opponent_click_counter = $_opponent_click_counter
    $: bonus_x = $_bonus_x
    $: bonus_y = $_bonus_y

    /* Shadow Stores Reactive Set */
    $: if ($_score !== score) _score.set(score)
    $: if ($_click_counter !== click_counter) _click_counter.set(click_counter)
    $: if ($_timer !== timer) _timer.set(timer)
    $: if ($_ready_countdown !== ready_countdown) _ready_countdown.set(ready_countdown)
    $: if ($_current_bonus !== current_bonus) _current_bonus.set(current_bonus)
    $: if ($_ready !== ready) _ready.set(ready)
    $: if ($_game_over !== game_over) _game_over.set(game_over)
    $: if ($_result !== result) _result.set(result)
    $: if ($_opponent_joined !== opponent_joined) _opponent_joined.set(opponent_joined)
    $: if ($_opponent_score !== opponent_score) _opponent_score.set(opponent_score)
    $: if ($_opponent_click_counter !== opponent_click_counter) _opponent_click_counter.set(opponent_click_counter)
    $: if ($_bonus_x !== bonus_x) _bonus_x.set(bonus_x)
    $: if ($_bonus_y !== bonus_y) _bonus_y.set(bonus_y)

    /* Proxy RPCs */
    const multiplayer_service = __self.proxyRPC('multiplayer_service')
    const handle_click = __self.proxyRPC('handle_click')
    const handle_bonus_click = __self.proxyRPC('handle_bonus_click')

    /* Destroy Component */
    __onDestroy(() => {
        __client.destroyComponent(__self)
    })

    /*---------- END: STREAMJAM ----------*/

    
</script>

        <div class="wrapper">
            <h1 class="logo"><span class="logo-click">Click</span><span class="logo-monger">Monger</span></h1>

            <div class="header">
                {#if !ready && ready_countdown == 0}
                    <div class="message">Waiting for an opponent to join...</div>
                {:else if !ready && ready_countdown > 0}
                    <div class="message">Prepare for your Click Battle!</div>
                {:else}
                    <div class="timer">00:{String(timer).padStart(2, '0')}</div>
                {/if}
            </div>

            <div class="score-container">
                <div class="target-score">200</div>
                <div class="score-strip">
                    <div class="score-bg">
                        <div class="self" style="width: {Math.min(score/4, 50)}%"></div>
                        <div class="opponent" style="width: {Math.min(opponent_score/4, 50)}%"></div>
                    </div>
                    <div class="mid-line"></div>
                    <div class="scores">
                        <div>{score}</div>
                        <div>{opponent_score}</div>
                    </div>
                </div>
                <div class="stats">
                    <div>{click_counter/10} clicks/s</div>
                    <div>{opponent_click_counter/10} clicks/s</div>
                </div>
            </div>

            <button class="click-pad" disabled={!ready} on:click={handle_click}>
                {#if ready_countdown >= 1}
                    <div class="countdown">
                        <p>{ready_countdown}</p>
                    </div>
                {:else if game_over}
                    <span>You {result ? 'Won! 😎' : 'Lost! 🙄'}</span>
                {:else}
                    <div class="tap">TAP</div>
                {/if}
                {#if current_bonus > 0}
                    <button 
                        class="bonus-pad" 
                        style="left: {bonus_x}%; top: {bonus_y}%"
                        on:click|stopPropagation={handle_bonus_click}
                    >
                        +{current_bonus}
                    </button>
                {/if}
            </button>

            <div class="footer">
                <p class="rules">Keep clicking on the target. Click on the timed targets for bonus points.</p>
            </div>
        </div>

        <style>
        .wrapper {
            width: 75%;
            min-width: 350px;
            max-width: 800px;
            margin: 10vh auto;
            display: flex;
            justify-content: center;
            flex-direction: column;
            gap: 6vh;
        }

        .logo {
            font-size: 64px;
            text-align: center;
            font-weight: 900;
            font-family: 'Inter', Helvetica, sans-serif;
            margin: 0;
        }

        .logo-click {
            color: #8A54FF;
            display: inline-block;
            rotate: -6deg;
        }

        .logo-monger {
            color: #4ECE89;
            display: inline-block;
            rotate: 3deg;
            transform: translate(4px, 8px);
        }

        .header {
            display: flex;
            justify-content: center;
        }

        .header .message {}

        .timer {
            border: 3px solid #272727;
            background-color: #1B1B1B;
            border-radius: 50px;
            padding: 8px 35px;
            font-size: 1.3rem;
            font-weight: bold;
            color: white;
            letter-spacing: 2px;
        }

        .score-container {}

        .target-score {
            text-align: center;
            font-weight: bold;
            font-size: 1.3rem;
            color: white;
        }

        .score-strip {
            height: 40px;
            border-radius: 50px;
            overflow: hidden;
            position: relative;
            margin: 1vh 0;
        }

        .scores {
            position: relative;
            display: flex;
            justify-content: space-between;
            padding: 0 20px;
            height: 100%;
            align-items: center;
            font-size: 1rem;
            font-weight: bold;
            color: white;
        }

        .mid-line {
            position: absolute;
            width: 4px;
            background: #ffffff17;
            left: calc(50% - 2px);
            top: 0;
            height: 100%;
        }

        .score-bg {
            height: 100%;
            width: 100%;
            background: #2D2D2D;
            position: absolute;
            top: 0;
            left: 0;
        }

        .score-bg .self {
            position: absolute;
            top: 0;
            left: 0;
            background: #8A54FF;
            height: 100%;
            width: 40%;
        }

        .score-bg .opponent {
            position: absolute;
            top: 0;
            right: 0;
            background: #4ECE89;
            height: 100%;
            width: 40%;
        }

        .stats {
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            padding: 0 20px;
        }

        .click-pad {
            height: 25vh;
            background: #3A3A3A;
            border-radius: 20px;
            border: none;
            border-bottom: 4px solid #2C2C2C;
            min-height: 100px;
            cursor: pointer;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            user-select: none;
            font-size: 1.25rem;
            color: #737373;
            touch-action: manipulation;
        }

        .bonus-pad {
            background-color: #B99258;
            border: none;
            border-bottom: 4px solid #896B3E;
            border-radius: 18px;
            padding: 12px 30px;
            font-weight: bold;
            font-size: 1rem;
            position: absolute;
            top: 10%;
            left: 20%;
            color: white;
            touch-action: manipulation;
            user-select: none;
        }

        .bonus-pad:active {
            transform: scale(0.975);
        }

        .countdown {
            text-align: center;
        }

        .countdown p {
            font-size: 2rem;
            margin: 1rem 0;
            color: white;
            font-weight: bold;
        }

        .tap {
            font-size: 10px;
            letter-spacing: 10px;
            color: #737373;
        }

        .footer {
            text-align: center;
        }

        @media only screen 
        and (min-device-width: 375px) 
        and (max-device-width: 812px) 
        and (-webkit-min-device-pixel-ratio: 3) {
            .logo {
                font-size: 45px;
            }

            .wrapper {
                margin: 4vh auto;
                gap: 4vh;
            }

            .click-pad {
                max-height: 180px;
            }
        }
        </style>
        