"""
The base Component class
"""
class Component():
    """
    Initialize with a status of 'ok' by default
    """
    def __init__ (self, status="ok"):
        self._status = status

    """
    Run diagnostics for component.
    """
    def diagnose(self):
        print(self._status)

    """
    Update status of Component
    """
    def setStatus(self, status):
        self._status = status
        print("Set status to {status}.")


    