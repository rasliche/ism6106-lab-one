from Component import Component

class Sensor(Component):
    def __init__(self, status):
        super().__init__(status)

    def detect():
        print("Detecting...")
