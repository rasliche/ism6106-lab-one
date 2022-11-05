from Component import Component

class LiftingScrew(Component):
    MAX_HEIGHT = 5

    def __init__(self, status, height=0):
        super().__init__(status)
        self._height = height

    def increaseHeight(self, value):
        print("Raising lifting screw...")
        if self._height + value >= LiftingScrew.MAX_HEIGHT:
            self._height = LiftingScrew.MAX_HEIGHT
            print("Raised to max height.")
        else:
            self._height += value
        

    def decreaseHeight(self, value):
        print("Lowering lifting screw...")
        if self._height - value <= 0:
            self._height = 0
        else:
            self._height -= value