from src.events.event_bus import EventBus

bus = EventBus()

class Engine:
    def run(self):
        bus.emit('system.start')
        return 'CORE RUNNING WITH EVENTS'
