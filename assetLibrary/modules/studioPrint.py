import warnings

try:
    from maya import OpenMaya
except Exception as error:
    warnings.warn(error, Warning)
    

class Print(object):
    
    def __init__(self, type, widget):        
        self.type = type
        self.widget = widget
        
    def display_error(self, message):
        if self.type=='__main__':
            self.widget.setTextBackgroundColor('gray')
            self.widget.setTextColor('red')
            
            self.widget.setText('#Error {}'.format(message))
            print '#Error ', message
        else:
            OpenMaya.MGlobal.displayError(str(message))
    
    def display_info(self, message):
        if self.type=='__main__':
            self.widget.setTextBackgroundColor('gray')            
            self.widget.setTextColor('black')
            self.widget.setText('#Error {}'.format(message))
        else:
            OpenMaya.MGlobal.displayInfo(str(message))
    
    def display_warning(self, message):
        if self.type=='__main__':
            self.widget.setTextBackgroundColor('gray')            
            self.widget.setTextColor('yellow')
            self.widget.setText('#Error {}'.format(message))            
            print '\n#Warning ', message
        else:
            OpenMaya.MGlobal.displayWarning(str(message))

    