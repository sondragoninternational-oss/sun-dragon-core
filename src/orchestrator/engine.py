from src.events.event_bus import EventBus

bus = EventBus()

class Engine:
    def run(self):
        bus.emit('system.start', {"status": "boot"})
        return "CORE RUNNING WITH ARCHITECTURE LAYER"
