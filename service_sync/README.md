# Example: Service Sync

## Feature Covered

- (/components/services.py)
    - A SocketService is a special service that can handle incoming socket connections. The `on_connect` method will receive a websocket object. This method must return a unique identifier for each connection. In this example the path is used as an identifier.
    - A simple CounterService to hold shared state between different connections.
    - Dispatching events. The dispatch method can also target a connection (using the ID specified by the SockerService) using the `recipients` parameter. Dispatch also supports dispatching to `rooms` which is a collection of connections.
- (/main.py) Registering and configuring services.
- (/components/root.py) 
    - Service event handlers
    - Identifying a Component Event's source 


---

## Issues that will be addressed in the future

- If a component needs to import another python file, it must also be placed within the `components` directory. Not doing so will result in a `streamjam build` error.