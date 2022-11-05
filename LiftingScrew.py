from Component import Component

class LiftingScrew(Component):
    MAX_HEIGHT = 5

    def __init__(self, status, height=0):
        super().__init__(status)
        self._height = height

    def increaseHeight(self, value):
        if self._height + value >= LiftingScrew.MAX_HEIGHT:
            self._height = LiftingScrew.MAX_HEIGHT
        else:
            self._height += value
        print("Raising lifting screw...")

    def decreaseHeight(self, value):
        if self._height - value <= 0:
            self._height = 0
        else:
            self._height -= value
        print("Lowering lifting screw...")