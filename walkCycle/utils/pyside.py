import sys
import os
import warnings
import pysideuic

from PySide import QtCore
from PySide import  QtGui
from shiboken import wrapInstance
import xml.etree.ElementTree as xml
from cStringIO import StringIO

def loadUi(uiFile=None):    
    if not uiFile :
        warnings.warn('argument(uiFile)is none')
        return None 
    if not os.path.isfile(uiFile) :
        warnings.warn('No such directory {}'.format(uiFile))
        return False

    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text    
    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}                
        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame                
        form_class = frame['Ui_%s'%form_class]
        base_class = eval('QtGui.%s'%widget_class)    
    return form_class, base_class
