from Component import Component

class Sensor(Component):
    def __init__(self, status):
        super().__init__(status)

    """
    Detect obstacles or reference barcodes,
    depending on type of sensor.
    """
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
