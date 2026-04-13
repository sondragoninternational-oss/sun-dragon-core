from src.events.event_bus import EventBus

bus = EventBus()

class Pipeline:
    def execute(self):
        bus.emit('pipeline.start')
        return 'PIPELINE RUNNING'
