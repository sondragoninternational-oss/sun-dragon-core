from src.orchestrator.engine import Engine
from src.services.pipeline import Pipeline

if __name__ == '__main__':
    e = Engine()
    p = Pipeline()
    print(e.run())
    print(p.execute())
test
