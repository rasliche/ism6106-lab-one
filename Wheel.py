from Component import Component

class Wheel(Component):
    def __init__(self, side, velocity):
        super().__init__(type="Wheel")
        self._side = side
        self._velocity = velocity

    def diagnose(self) -> str:
        super().diagnose()
        print(self._side)
        if self._velocity > 0:
            direction = "forwards"
        else:
            direction = "backwards"
        print(f"Moving {self._velocity} m/s {direction}.")