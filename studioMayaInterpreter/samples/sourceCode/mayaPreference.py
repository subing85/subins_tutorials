'''
Smart Preference v0.1
Date : June 16, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import sys, os, datetime, imp
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject
from functools import partial

#uiDirectory             = os.path.join (os.path.dirname (__file__)) + '/ui'
#uiDirectory             = 'F:/My Work/dumps/My script/pythonApplication/smartTool/smartMaya/ui'
#form_class, base_class  = uic.loadUiType (uiDirectory + '/' + 'smartMayaPreference_ui.ui')

#sys.path.append ('F:/My Work/dumps/My script/pythonApplication/smartTool/Applications/smartMaya/ui')
from smartMayaPreference_ui import Ui_MainWindow_preference

class MAYAPREFERENCE (QtGui.QMainWindow):
    def __init__(self, mWindow, parent=None):
    #def __init__(self, parent=None):        
        super (MAYAPREFERENCE, self).__init__(parent)
        self.ui        = Ui_MainWindow_preference ()
        self.ui.setupUi(self)

        self.appDirectory   = os.path.abspath (os.path.join (os.path.dirname (__file__))).replace ('\\', '/')
        self.iconDirectory  = os.path.join(os.path.dirname (__file__)) + '/icons'
        self.docDirectory   = os.path.abspath (os.getenv('USERPROFILE') + '/Documents').replace ('\\', '/')

        #self.mayaVersion   = 'C:/Program Files/Autodesk/Maya2012'
        self.mayaVersion    = 'C:/Program Files/Autodesk/Maya2012'
        self.autodeskPath   =  'C:/Program Files/Autodesk'
        self.setupPath      =  self.docDirectory + '/SmartTool/SmartMaya/smartMayaSetup.py'
        self.modePath       =  self.docDirectory + '/SmartTool/SmartMaya/smartMayaMode.py'
        
        self.mainWindow     = mWindow

        #Pass Signals
        qRadioButtonList    = [eachRadioButton for eachRadioButton in self.ui.groupBox_versions.findChildren (QtGui.QRadioButton)]
        for eachRadioButton in qRadioButtonList :        
            eachRadioButton.clicked.connect (partial (self.setMayaVersion, eachRadioButton))
            self.radioButton = eachRadioButton

        self.ui.radioButton_edit.clicked.connect (partial (self.mayaMode, 'edit'))
        self.ui.radioButton_quarry.clicked.connect (partial (self.mayaMode, 'quarry'))            

        self.ui.button_directory.clicked.connect (self.setDirectory)  
        self.ui.button_apply.clicked.connect (self.applyPreference)  
        self.ui.button_cancel.clicked.connect (self.cancelPreference)        

        #Call function
        self.iconConfigure ()
        self.uiConfigure ()
        self.readCurrentMaya ()
        self.readMayaMode ()
        
        
    def uiConfigure (self) :
        self.setWindowTitle ('Preference')        
        self.ui.lineEdit_directory.setText (self.mayaVersion)
        self.mainWindow.hide ()
        self.ui.radioButton_edit.setChecked (2)
        self.ui.tabWidget_preference.setCurrentIndex (0)
        self.ui.radioButton_none.hide ()
        self.ui.radioButton_version.setChecked (2)
         
    def iconConfigure (self) :
        icon        = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap (self.appDirectory + '/icons/preference.png'))
        self.setWindowIcon (icon)
        
        qRadioButtonList    = [eachRadioButton for eachRadioButton in self.findChildren (QtGui.QRadioButton)]        
        for iconLoop in range (0, len (qRadioButtonList), 1) :            
            icon            = QtGui.QIcon()
            iconName        = str (qRadioButtonList[iconLoop].objectName ()).split ('_')[1]            
            icon.addPixmap(QtGui.QPixmap (self.iconDirectory + '/' + iconName + '.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            qRadioButtonList[iconLoop].setIcon (icon)

    def setDirectory (self) :
        getPath         = QtGui.QFileDialog.getExistingDirectory (self, 'Browse Maya directory', self.mayaVersion)        
        self.ui.lineEdit_directory.setText (os.path.abspath (str (getPath)).replace ('\\', '/'))        
        qRadioButtonList    = [eachRadioButton for eachRadioButton in self.ui.groupBox_versions.findChildren (QtGui.QRadioButton)]        
        for iconLoop in range (0, len (qRadioButtonList), 1) :            
            iconName        = str (qRadioButtonList[iconLoop].objectName ()).split ('_')[1]
            if os.path.basename (str (getPath)).lower ()==iconName.lower () :
                qRadioButtonList[iconLoop].setChecked (2)
                break
        print os.path.abspath (str (getPath)).replace ('\\', '/')


    def applyPreference (self) :
        #Store datas
        currentMaya     = str(self.radioButton.objectName()).split ('_')[1]
        mayaPath        = {currentMaya : 'C:/Program Files/Autodesk/' + currentMaya[0].upper() + currentMaya[1:]}
        self.ui.lineEdit_directory.setText (mayaPath.values()[0])      
        self.createSetup (mayaPath)
        mayaPath        = str (self.ui.lineEdit_directory.text ())
        self.mainWindow.setToolTip (mayaPath)
        
        self.storeMayaMode ()
        
        self.close ()
        self.mainWindow.show ()
        print '\nCurrent Maya Version is reset to \n\t', mayaPath
        

    def cancelPreference (self) :
        self.close ()
        self.mainWindow.show ()
            
        if not os.path.isfile (self.setupPath) :
            currentMaya     = str(self.radioButton.objectName()).split ('_')[1]
            mayaPath        = {currentMaya : 'C:/Program Files/Autodesk/' + currentMaya[0].upper() + currentMaya[1:]}           
            self.createSetup (mayaPath)
        
        if not os.path.isfile (self.modePath) :
            self.storeMayaMode ()
            

    def setMayaVersion (self, radioButton) :
        self.radioButton    = radioButton
        currentMaya         = str(radioButton.objectName()).split ('_')[1]       
        mayaPath            = {currentMaya : 'C:/Program Files/Autodesk/' + currentMaya[0].upper() + currentMaya[1:]}
        self.ui.lineEdit_directory.setText (mayaPath.values()[0])        
        

    def createSetup (self, data) :
        if not os.path.isdir (self.docDirectory + '/SmartTool/SmartMaya') :
            os.makedirs (self.docDirectory + '/SmartTool/SmartMaya')            

        if os.path.isfile (self.setupPath) :
            try :
                os.remove (self.setupPath)
            except Exception as result :
                print result      
            
        currentTime = datetime.datetime.now()
        dtaeAndTime = currentTime.strftime("%A, %B %d, %Y %H:%M:%S %p")            
        title       = '# -*- coding: utf-8 -*-\n# Form implementation generated from reading Smart Maya \n#\n# Created: ' + dtaeAndTime + '\n#      by: Store code generator 4.5.4\n#\n# WARNING! All changes made in this file will be lost!\n'
        storeInfo   = open (self.setupPath, 'w')
        storeInfo.write(title + '\ndef SMARTMAYA_type () :\n\tmayaVersion\t= ' + str(data) + '\n\treturn mayaVersion')
        storeInfo.close ()
        

    def searchMaya (self) :        
        mayaList            = os.listdir (self.autodeskPath)
        currentMayaList     = {}      
        for eachMaya in mayaList :
            if os.path.isfile (self.autodeskPath + '/' + eachMaya + '/bin/maya.exe') :
                currentMayaList.setdefault (eachMaya.lower(), self.autodeskPath + '/' + eachMaya)                
        return currentMayaList
    

    def readCurrentMaya (self) :
        currentMayaList     = self.searchMaya ()        
        
        qRadioButtonList    = [eachRadioButton for eachRadioButton in self.ui.groupBox_versions.findChildren (QtGui.QRadioButton)]        
        if os.path.isfile (self.setupPath) :
            database        = os.path.basename (self.setupPath).split('.')[0]        
            sys.path.append (os.path.dirname (self.setupPath))
            import smartMayaSetup as smSetup
            reload (smSetup)
            mayaPath        = smSetup.SMARTMAYA_type ()            

            for radLoop in range (0, len (qRadioButtonList), 1) :
                if str(qRadioButtonList[radLoop].objectName()).endswith (mayaPath.keys()[0]) :
                    qRadioButtonList[radLoop].setChecked (2)
                    break

        else :            
            if currentMayaList :
                mayaPath    = {currentMayaList.keys()[-1] : currentMayaList.values()[-1]}
                for radLoop in range (0, len (qRadioButtonList), 1) :
                    if str(qRadioButtonList[radLoop].objectName()).split('_')[1] in currentMayaList.keys() :
                        self.setMayaVersion (qRadioButtonList[radLoop])
                        qRadioButtonList[radLoop].setChecked (2)

        print '\nCurrnet maya s exists in your computer'
        for eachMaya in currentMayaList :
            print '\t', eachMaya, '\t', currentMayaList[eachMaya]

        for radLoop in range (0, len (qRadioButtonList), 1) :
            if str(qRadioButtonList[radLoop].objectName()).split('_')[1] not in currentMayaList.keys() :
                qRadioButtonList[radLoop].setEnabled (False)                
        print '\nCurrent Maya Version\n\t', mayaPath.keys()[0], '\n\t', mayaPath.values()[0]
        

    def mayaMode (self, mode) :
        if mode=='edit' :
            self.ui.radioButton_overwrite.setEnabled (1)
            self.ui.radioButton_version.setEnabled (1)
            self.ui.radioButton_version.setChecked (2)        
        if mode=='quarry' :        
            self.ui.radioButton_overwrite.setEnabled (0)
            self.ui.radioButton_version.setEnabled (0)            
            self.ui.radioButton_none.setChecked (2)


    def storeMayaMode (self) :
        mode        = 0
        version     = 0
        if self.ui.radioButton_edit.isChecked() :
            mode    = 1
            if self.ui.radioButton_overwrite.isChecked() :
                version     = 1
            if self.ui.radioButton_version.isChecked() :
                version     = 2 

        #mode       =1= edit
        #mode       =0= quarry
        #version    =0= none
        #version    =1= overwrite
        #version    =2= version
        if os.path.isfile (self.modePath) :
            try :
                os.remove (self.modePath)
            except Exception as result :
                print result    
        
        currentTime = datetime.datetime.now()
        dtaeAndTime = currentTime.strftime("%A, %B %d, %Y %H:%M:%S %p")            
        title       = '# -*- coding: utf-8 -*-\n# Form implementation generated from reading Smart Maya \n#\n# Created: ' + dtaeAndTime + '\n#      by: Store code generator 4.5.4\n#\n# WARNING! All changes made in this file will be lost!\n'
        storeInfo   = open (self.modePath, 'w')
        storeInfo.write(title + '\ndef SMARTMAYA_mode () :\n\tmayaMode\t= [' + str(mode) + ', '+ str(version) + ']\n\treturn mayaMode')
        storeInfo.close ()
        

    def readMayaMode (self) :
        mode        ='quarry'
        if os.path.isfile (self.modePath) :
            import smartMayaMode as smMode
            reload (smMode)
            mayaPath        = smMode.SMARTMAYA_mode ()
            
            self.ui.radioButton_quarry.setChecked (2)
            self.ui.radioButton_none.setChecked (2)
           
            if mayaPath[0]==1 :
                mode        ='edit'
                self.ui.radioButton_edit.setChecked (2)
                self.ui.radioButton_overwrite.setChecked (2)
                if mayaPath[1]==2 :
                   self.ui.radioButton_version.setChecked (2)

        self.mayaMode (mode)
