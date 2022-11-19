from ControlUnit import ControlUnit
from Battery import Battery
from Wheel import Wheel
from Sensor import *

"""
The RobotUnit class represents a functioning
real world unit. It includes all the associated
parts and keeps account. Commands are sent to the robot
which can pass them on as necessary.
"""

class RobotUnit():
    def __init__(self) -> None:
        self._components = [ControlUnit(), Battery(), Wheel(side="Port", velocity=1), Wheel(side="Starboard", velocity=0.8), CameraSensor()]

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

    def routeToDestination(self):
        self._components[0].route()

    
        

    def heading():
        return 0