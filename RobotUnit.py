from ControlUnit import ControlUnit
from Battery import Battery
from Wheel import Wheel
from Sensor import CameraSensor
from LiftingScrew import LiftingScrew

"""
The RobotUnit class represents a functioning
real world unit. It includes all the associated
parts and keeps account. Commands are sent to the robot
which can pass them on as necessary.
"""

class RobotUnit():
    def __init__(self) -> None:
        self._components = [ControlUnit(), Battery(), Wheel(side="Port", velocity=1), Wheel(side="Starboard", velocity=0.8), CameraSensor(), LiftingScrew()]

    def report(self):
        print("_" * 24)
        print("Beginning Report:")
        print("_" * 24)
        for c in self._components:
            print("---")
            print(c._type)
            print(c.diagnose())
        print("-" * 24)
        print("Report Finalized.")
        print("_" * 24)

    def routeToDestination(self, velocity):
        self._components[0].processCommand("Mission: Retrieve Shelf Unit")
        self._components[0].route()
        self._components[2]._velocity = velocity
        self._components[2].diagnose()
        self._components[0].processCommand("Mission: Deliver Shelf Unit to Picker")
        self._components[0].route()
        self._components[3]._velocity = velocity
        self._components[3].diagnose()

    def identifyShelf(self):
        self._components[4].captureBarcode()

    def carryShelf(self):
        self._components[5].increaseHeight(5)

    def dropShelf(self):
        self._components[5].decreaseHeight(6)

    def heading(self):
        return 0

    def charge(self):
        print("Proceeding to charging station to standby")