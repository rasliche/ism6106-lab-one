from Component import Component

class Battery(Component):
    def __init__(self, chargeRemaining=100) -> None:
        super().__init__(type="Battery")
        self._chargeRemaining=chargeRemaining
