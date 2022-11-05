from Component import Component

class ControlUnit(Component):
    def __init__(self, status):
        super().__init__(status)

    def requestDiagnostics():
        print("Requesting diagnostics of components...")
