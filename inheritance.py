class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Staring the Car")

    def stop(self):
        print("Stopping the Car")

class ThreeSeries(BMW):
    def __init__(self,cruseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruseControlEnabled
    def display(self):
        print(self.cruiseControlEnabled)
    def start(self):
        super().start()
        print("Button start")

class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled

threeSeries=ThreeSeries(True,"BMW","328I","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()