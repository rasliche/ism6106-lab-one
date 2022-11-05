"""
The base Component Class
"""
class Component():
    def __init__ (self, status):
        self._status = status

    def diagnose(self):
        print(self._status)

    def setStatus(self, status):
        self._status = status
        print("Set status to {status}.")


    