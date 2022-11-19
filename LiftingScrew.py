from Component import Component

class LiftingScrew(Component):
    MAX_HEIGHT = 5

    def __init__(self, height=0):
        super().__init__(type="Lifting Screw")
        self._height = height
        print("Initialized a LiftingScrew with starting heigh of {self._height}")

    """
    Raise the lifting screw by passing a value.
    """
    def increaseHeight(self, value):
        print("Raising lifting screw...")
        if self._height + value >= LiftingScrew.MAX_HEIGHT:
            self._height = LiftingScrew.MAX_HEIGHT
            print("Raised to max height.")
        else:
            self._height += value
            print("Raised to {self._height}.")
        
    """
    Lower the lifting screw by passing a value.
    """
    def decreaseHeight(self, value):
        print("Lowering lifting screw...")
        if self._height - value <= 0:
            self._height = 0
            print("Lowered to 0.")
        else:
            self._height -= value
            print("Lowered to {self._height}.")