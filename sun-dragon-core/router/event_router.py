from src.events.event_bus import EventBus

class EventRouter:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.routes = {}

    def register(self, event, handler):
        self.routes[event] = handler
        self.bus.on(event, self.dispatch)

    def dispatch(self, data):
        # event name comes implicitly via binding
        for event, handler in self.routes.items():
            handler(data)
