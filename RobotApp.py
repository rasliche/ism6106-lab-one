from ControlUnit import ControlUnit
from RobotUnit import RobotUnit

# Demonstration of the capabilities of the robot
# Prints output to the terminal

if __name__ == '__main__':
    print("RUNNING PROGRAM")
    robot = RobotUnit()
    robot.report()
    robot.routeToDestination(1)
    robot.identifyShelf()
    robot.carryShelf()
    robot.routeToDestination(-1)
    robot.dropShelf()
    robot.charge()
    print("PROGRAM FINISHED")