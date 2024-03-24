import asyncio
from streamjam import StreamJam

app = StreamJam(
    name="todo_task_timer"
)


if __name__ == '__main__':
    asyncio.run(app.serve())
