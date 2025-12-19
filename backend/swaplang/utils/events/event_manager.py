from asyncio import CancelledError, Queue
from typing import AsyncGenerator

from swaplang.utils.events.models import MessageEvent


class _EventManager:
    def __init__(self):
        self.listeners: set[Queue[MessageEvent]] = set()

    def subscribe(self):
        listener: Queue[MessageEvent] = Queue()
        self.listeners.add(listener)
        return listener

    def unsubscribe(self, listener: Queue[MessageEvent]):
        self.listeners.discard(listener)

    def emit(self, message_event: MessageEvent):
        for listener in self.listeners:
            listener.put_nowait(message_event)

    async def stream(self) -> AsyncGenerator[str, None]:
        listener_queue = self.subscribe()
        try:
            while True:
                event = await listener_queue.get()
                print("Yielding event:", event.model_dump())
                yield str(event.model_dump())
        except CancelledError:
            print("Stream cancelled, unsubscribing listener.")
            self.unsubscribe(listener_queue)
            raise


event = _EventManager()
