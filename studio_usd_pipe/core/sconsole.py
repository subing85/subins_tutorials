import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from studio_usd_pipe.core import swidgets


class Console (QtCore.QObject):  
    _stdout = None
    _stderr = None
    message_written = QtCore.Signal(str)
    
    def __init__(self, widget=None): 
        super(Console, self).__init__()    
        self.widget = widget
   
    def write(self, message):
        if self.signalsBlocked() :
            return
        self.set_text_color(message)              
        self.message_written.emit(message)
           
    @staticmethod
    def stdout(widget):
        if not Console._stdout :
            Console._stdout = Console(widget)           
            sys.stdout = Console._stdout
        return Console._stdout
   
    @staticmethod
    def stderr():
        if not Console._stderr :
            sys.stderr = Console._stderr
        return Console._stderr  
    
    def set_text_color(self, message):
        # header color, info color, warning color, error color
        clolor_bundle = swidgets.get_color_code()
        if '#header' in message:
            clolor_code = clolor_bundle[0]
        elif '#info' in message:
            clolor_code = clolor_bundle[1]          
        elif '#warning' in message:
            clolor_code = clolor_bundle[2]  
        elif '#error' in message:
            clolor_code = clolor_bundle[3]
        elif '#failed' in message:
            clolor_code = clolor_bundle[3]            
        else:
            clolor_code = clolor_bundle[1]
        self.widget.setTextColor(clolor_code)                        
    
