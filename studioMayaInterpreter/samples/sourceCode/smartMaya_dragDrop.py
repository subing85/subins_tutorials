'''
Smart Maya drag and Drop v0.1
Date : June 16, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import sys, os, shutil, datetime, binascii
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
from functools import partial
 
 
#Drop and drop
class dropArea (QtGui.QTreeWidget):   
    changed = QtCore.pyqtSignal(QtCore.QMimeData)
    
    def __init__(self, parent = None):
        super(dropArea, self).__init__(parent)       

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]

        self.iconDirectory  = os.path.join(os.path.dirname (__file__)) + '/icons'
 
        self.setSortingEnabled (True)
        self.setAlternatingRowColors (True)
        self.setAcceptDrops (True)
        self.setAutoFillBackground (True)
        self.clear ()       
        
    def dragEnterEvent (self, event):
        event.acceptProposedAction ()
 
    def dragMoveEvent (self, event):
        event.acceptProposedAction ()
 
 
    def dropEvent (self, event):
        mimeData = event.mimeData ()        
        if mimeData.hasUrls():
            for url in mimeData.urls() :
                filePath            = os.path.abspath (str (url.toLocalFile())).replace ('\\', '/')
                
                if self.objectName ()=='treeWidget_mayaFile'  :               
                    if filePath.endswith('.ma') or filePath.endswith('.mb') :                       
                        item        = QtGui.QTreeWidgetItem (self)                        
                        icon        = QtGui.QIcon ()

                        if filePath.endswith('.ma') :
                            icon.addPixmap (QtGui.QPixmap (self.iconDirectory + '/mayaAscii.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        if filePath.endswith('.mb') :
                            icon.addPixmap (QtGui.QPixmap(self.iconDirectory + '/mayaBinary.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                        item.setIcon(0, icon)
                        item.setText (0, os.path.basename (filePath))
                        item.setToolTip (0, filePath)        
                        item.setFlags (QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)
                       
                        
                elif self.objectName ()=='treeWidget_script' : 
                    if filePath.endswith('.mel') or filePath.endswith('.py') or filePath.endswith('.pyc') :                
                        item        = QtGui.QTreeWidgetItem (self)                        
                        icon        = QtGui.QIcon ()

                        if filePath.endswith('.mel') :
                            icon.addPixmap (QtGui.QPixmap (self.iconDirectory + '/mel.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)                            
                        if filePath.endswith('.py') :
                            icon.addPixmap (QtGui.QPixmap (self.iconDirectory + '/python.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        if filePath.endswith('.pyc') :
                            icon.addPixmap (QtGui.QPixmap(self.iconDirectory + '/pythonCompile.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                        item.setIcon(0, icon)
                        item.setText (0, os.path.basename (filePath))
                        item.setToolTip (0, filePath)        
                        item.setFlags (QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)
                          
                else :
                    print 'Its not correct file, please check the file extension'                   
        event.acceptProposedAction() 
               
    def dragLeaveEvent(self, event):
        #self.clear()
        event.accept()
