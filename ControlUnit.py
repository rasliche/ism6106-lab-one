from Component import Component

"""
ControlUnit class to coordinate the operation of subsystems.
Movement, diagnostics, communication with hivemind goes through
this class.
"""
class ControlUnit(Component):
    def __init__(self, status):
        super().__init__(status)

    """
    Ask all composition components to run diagnostics and
    report back the status.
    """
    def requestDiagnostics():
        print("Requesting diagnostics of components...")
