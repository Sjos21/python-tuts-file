class Flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start()
class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")

class BoingEngine:
    def start(self):
        print("Starting Boing Engine")
a=AirbusEngine()
f=Flight(a)
f.startEngine()

b=BoingEngine()
f=Flight(b)
f.startEngine()