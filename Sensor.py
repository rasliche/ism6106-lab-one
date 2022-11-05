from Component import Component

class Sensor(Component):
    def __init__(self, status):
        super().__init__(status)

    def detect():
        print("Detecting...")

class TouchSensor(Sensor):
    def __init__(self, status):
        super().__init__(status)

class InfraredSensor(Sensor):
    def __init__(self, status):
        super().__init__(status)

class CameraSensor(Sensor):
    def __init__(self, status):
        super().__init__(status)
