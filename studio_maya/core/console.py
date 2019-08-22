import sys
import PySide.QtCore as QtCore


class Connect(QtCore.QObject):
    _stdout = None
    _stderr = None
    message_written = QtCore.Signal(str)

    def flush(self):
        pass

    def fileno(self):
        return -1

    def write(self, message):
        if not self.signalsBlocked():
            self.message_written.emit(message)

    @staticmethod
    def stdout():
        if not Connect._stdout:
            Connect._stdout = Connect()
            sys.stdout = Connect._stdout
        return Connect._stdout

    @staticmethod
    def stderr():
        if not Connect._stderr:
            sys.stderr = Connect._stderr
        return Connect._stderr
