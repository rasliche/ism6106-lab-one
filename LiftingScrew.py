from Component import Component

class LiftingScrew(Component):
    def __init__(self, status, height):
        super().__init__(status)
        self._height = height
        
    def raise(self):
        print("Raising lifting screw...")

    def lower(self):
        print("Lowering lifting screw...")