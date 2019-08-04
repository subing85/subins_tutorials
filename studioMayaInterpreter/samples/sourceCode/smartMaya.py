'''
Smart Maya v0.1
Date : June 16, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import sys, os
import datetime, imp
import _sre
import sip, re, atexit

import mayaVersion as mVersion
reload (mVersion)
mVersion.version ()

try :
    import maya.standalone
    maya.standalone.initialize(name='python')
    print 'standalone\t', maya.standalone
except Exception, result :
    print result

#import maya.cmds as cmds
#import maya.mel as mel

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject
from functools import partial

#uiDirectory             = os.path.join (os.path.dirname (__file__)) + '/ui'
#uiDirectory             = 'F:/My Work/dumps/My script/pythonApplication/smartTool/smartMaya/ui'
#form_class, base_class  = uic.loadUiType (uiDirectory + '/' + 'smartMaya_ui.ui')
#sys.path.append ('F:/My Work/dumps/My script/pythonApplication/smartTool/Applications/smartMaya/ui')

from smartMaya_ui import Ui_MainWindow_smartMaya

#print base_class
prefLoad    	= 1

#class SMARTMAYA (form_class, base_class):
class SMARTMAYA (QtGui.QMainWindow) :
    
    def __init__(self, parent=None):
    #def __init__(self, parent=None):        
        super (SMARTMAYA, self).__init__(parent)
        self.ui        = Ui_MainWindow_smartMaya()
        self.ui.setupUi(self)

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]

        #Global variables
        self.appDirectory   = os.path.abspath (os.path.join (os.path.dirname (__file__))).replace ('\\', '/')
        self.iconDirectory  = os.path.join(os.path.dirname (__file__)) + '/icons'
        self.docDirectory   = os.path.abspath (os.getenv('USERPROFILE') + '/Documents').replace ('\\', '/')

        self.tempDirectory  = os.path.abspath (os.getenv('TEMP')).replace ('\\', '/')

        self.saveStatus     = ''
        self.iconPrefix     = {'.mel':'mel', '.py':'python', '.mb':'mayaBinary', '.ma':'mayaAscii'}
        self.mayaVersion    = ''

        #Load Function
        self.readCurrentMaya ()
        self.uiConfigure ()        
        self.loadToolBar ()
        self.iconConfigure ()
        self.loadQTreeWidget ()
        
        #self.rightClick ()

        #Pass Signals    
        self.ui.action_new.triggered.connect (self.newSM)        
        self.ui.action_open.triggered.connect (self.openSM)        
        self.ui.action_save.triggered.connect (self.saveSM)        
        self.ui.action_saveAs.triggered.connect (self.saveAsSM)        
        self.ui.action_quit.triggered.connect (self.close)        
        self.ui.action_importMayaFile.triggered.connect (self.importMayaFile)        
        self.ui.action_importMelPython.triggered.connect (self.importMelPython)
        
        self.ui.action_preference.triggered.connect (self.loadPreference)        
        self.ui.action_startToExecute.triggered.connect (self.startToExecute)       
        self.ui.action_aboutApplication.triggered.connect (self.aboutApplication)
        
    def uiConfigure (self) :
        self.setWindowTitle ('Smart Maya v0.1')        
        self.setToolTip (self.mayaVersion)
        self.ui.progressBar.hide ()

    def readCurrentMaya (self) :
        path        =  self.docDirectory + '/SmartTool/SmartMaya/smartMayaSetup.py'
        global prefLoad

        if os.path.isfile (path) :
            database       = os.path.basename (path).split('.')[0]        
            sys.path.append (os.path.dirname (path))
            import smartMayaSetup as smSetup
            imp.reload (smSetup)

            mayaType    	= smSetup.SMARTMAYA_type()            
            self.mayaVersion    = mayaType.values()[0]
            self.browsePath     = self.mayaVersion
            print '\nCurrent Maya Version\n\t',  self.mayaVersion

        else :
            self.loadPreference ()
            prefLoad     = 0

        #print prefLoad

    def iconConfigure (self) :
        icon        = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap (self.appDirectory + '/icons/smartMaya.png'))
        self.setWindowIcon (icon)
        
        qActionList     = [eachQAction for eachQAction in self.findChildren (QtGui.QAction)]
        for eachAction in qActionList :
            icon            = QtGui.QIcon()            
            iconName        =  str (eachAction.objectName ()).split ('action_')
            if len(iconName)==2 :
                icon.addPixmap(QtGui.QPixmap (self.iconDirectory + '/' + iconName[1] + '.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                eachAction.setIcon (icon)  

    def loadToolBar (self) :
        self.toolBar = QtGui.QToolBar()
        self.toolBar.addAction(self.ui.action_new)
        self.toolBar.addAction(self.ui.action_open)
        self.toolBar.addAction(self.ui.action_save)
        #self.toolBar.addAction(self.ui.action_saveAs)        
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()        
        self.toolBar.addAction(self.ui.action_importMayaFile)
        self.toolBar.addAction(self.ui.action_importMelPython)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()        
        self.toolBar.addAction(self.ui.action_preference)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        
        self.toolBar.addAction(self.ui.action_startToExecute)       
        self.ui.horizontalLayout_toolBar.addWidget (self.toolBar)


    def loadQTreeWidget (self) :
        from smartMaya_dragDrop import dropArea
        
        self.treeWidget_mayaFile    = dropArea ()
        self.treeWidget_mayaFile.setObjectName ('treeWidget_mayaFile')
        self.treeWidget_mayaFile.headerItem().setText(0, 'Maya Files')        
        self.ui.splitter.addWidget (self.treeWidget_mayaFile)      
        self.treeWidget_mayaFile.setSelectionMode (QtGui.QAbstractItemView.ExtendedSelection)
       
        self.treeWidget_script    = dropArea ()
        self.treeWidget_script.setObjectName ('treeWidget_script')
        self.treeWidget_script.headerItem().setText(0, 'Scripts')
        self.treeWidget_script.setSelectionMode (QtGui.QAbstractItemView.SingleSelection)
        
        self.ui.splitter.addWidget (self.treeWidget_script)
        

    def rightClick (self) :
        #set button context menu policy
        self.treeWidget_mayaFile.setContextMenuPolicy (QtCore.Qt.CustomContextMenu)
        self.treeWidget_mayaFile.customContextMenuRequested.connect (self.contextMenu)
     
        # create context menu
        self.popMenu = QtGui.QMenu (self)
        self.popMenu.addAction(QtGui.QIcon(self.appDirectory + '/icons/openDirectory.png'), 'Open Directory', (self.openDirectory))
        self.popMenu.addAction(QtGui.QIcon(self.appDirectory + '/icons/openScene.png'), 'Open Scene', (self.openScene))        
        self.popMenu.addAction(QtGui.QIcon(self.appDirectory + '/icons/createReference.png'), 'Create Reference', (self.createReference))        

    def contextMenu(self, point):
        self.popMenu.exec_(self.listWidget_assetAppend.mapToGlobal(point))

    def aboutApplication (self) :
        os.startfile (self.appDirectory + '/docs/index.html')
        #os.system (self.tempDirectory + '/smartMaya_init.bat')        

    def newSM (self) :
        self.treeWidget_mayaFile.clear ()
        self.treeWidget_script.clear ()
        self.setWindowTitle ('Smart Maya v0.1')        
        self.saveStatus     = ''        
        
    def openSM (self) :
        self.result ('\nmodule_open')
        self.newSM ()
        openFile            = QtGui.QFileDialog.getOpenFileName (self, 'Open Form', self.browsePath, 'Maya Taxi (*.sm)')
        if openFile :
            readData        = open (str (openFile), 'r')
            data            = readData.read ()
            if 'smKey\t= ' in data :
                dataDict    = data.split ('smKey\t= ')[1]
                fileList    = ast.literal_eval (dataDict)                

                for eachWidget in fileList :
                    currentWidget       = self.treeWidget_mayaFile                    
                    if eachWidget=='treeWidget_script' :
                        currentWidget       = self.treeWidget_script

                    self.result ('\n'.join (fileList[eachWidget]).expandtabs(4))                    
                    self.importFiles (currentWidget, fileList[eachWidget])
                
                self.result ('\tFile open\n// Result: ' + str(openFile).expandtabs(4))            
        else :
            self.result ('\tFile open\n// Result: empty //'.expandtabs(4))

    
    def saveSM (self) :
        if self.saveStatus :               
            self.saveTo (self.saveStatus, [self.treeWidget_mayaFile, self.treeWidget_script])           
        else :
            self.saveAsSM ()         
            
    def saveAsSM (self) :
        saveAsName          = QtGui.QFileDialog.getSaveFileName (self, 'Save Form As', self.browsePath, 'Smart Maya (*.sm)')
        fileName            = str(saveAsName) + '.sm'            
        if '.' in saveAsName :
            fileName        = str(saveAsName).split ('.')[0] + '.sm'
                               
        self.saveTo (fileName, [self.treeWidget_mayaFile, self.treeWidget_script])           
        self.saveStatus     = fileName        
        
    def saveTo (self, directory, widgets) :
        self.result ('\nmodule_save') 
        data                    = {}
        for eachWidget in widgets :             
            widget              = eachWidget.invisibleRootItem()
            itemCount           = widget.childCount ()
            
            for itLoop in range (0, itemCount, 1) :
                childItem       = widget.child(itLoop)                
                fileDirectory   = str (childItem.toolTip(0))
                data.setdefault (str (eachWidget.objectName()), []).append (fileDirectory)    

        currentTime = datetime.datetime.now()
        title       = '# -*- coding :- Smart Maya -*-\n# Form implementation generated from reading \"Smart Maya\"\n'
        date        = '# Created: ' + currentTime.strftime("%A, %B %d, %Y %H:%M:%S %p") + '\n#\tby Subin Gopi (subing85@gmail.com)\n'
        warning     = '# WARNING! All changes made in this file will be lost!\n\n'
        key         = 'smKey = '
        infoList    = title + date + warning + 'smKey\t= ' + str(data)
        
        writeData   = open (directory, 'w')
        for eachInfo in infoList :
            writeData.write (eachInfo)                
        writeData.close ()
        self.result ('\tFile save\n\t\t// Result: ' + directory + ' //'.expandtabs(4))                  
        self.setWindowTitle ('Smart Maya v0.1\t' + directory.expandtabs(4))

                
    def importMayaFile (self) :
        openFiles           = QtGui.QFileDialog.getOpenFileNames (self, 'Import Maya Files', self.browsePath, 'Maya file (*.ma *.mb)')
        if openFiles :        
            self.importFiles (self.treeWidget_mayaFile, openFiles)


    def importMelPython (self) :       
        openFiles           = QtGui.QFileDialog.getOpenFileNames (self, 'Import Script Files', self.browsePath, 'Maya file (*.mel *.py)')
        if openFiles :
            self.importFiles (self.treeWidget_script, openFiles)

    def importFiles (self, widget, fileList) :
        self.result ('\nmodule_import') 
        for eachFile in fileList :
            item        = QtGui.QTreeWidgetItem (widget)                
            item.setText (0, os.path.basename (str(eachFile)))
            item.setToolTip (0, os.path.abspath (str(eachFile)).replace ('\\', '/'))
            item.setFlags (QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)

            extentions              = os.path.splitext (str(eachFile))[1]
            currentIconDirectory    = self.iconDirectory + '/unknown.png'

            if os.path.isfile (self.iconDirectory + '/' + self.iconPrefix[extentions] + '.png') :
                currentIconDirectory    = self.iconDirectory + '/' + self.iconPrefix[extentions] + '.png'

            icon        = QtGui.QIcon ()
            icon.addPixmap (QtGui.QPixmap (currentIconDirectory), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon (0, icon)

            self.result ('\t' + str(eachFile).expandtabs(4))

        self.browsePath     = os.path.dirname (str(fileList[-1]))
        #self.result ('\t' + os.path.dirname (str(fileList[-1])).expandtabs(4))
        

    def loadPreference (self) :         
        #self.setEnabled (0)
        import mayaPreference as mayaP
        #reload (mayaP)
        self.mp     = mayaP.MAYAPREFERENCE (self)
        self.mp.show  ()


    def startToExecute (self) :
        mayaPath        = str (self.toolTip ())
        
        mayaList        = self.treeWidget_mayaFile.selectedItems ()
        scriptList      = self.treeWidget_script.selectedItems ()
        currentMayaPath = str(self.toolTip())        
        
        self.result ('mod_startToExecute\n\tReading maya file')

        if mayaList :
            if scriptList :
                scriptFile      = str (scriptList[-1].toolTip (0))
                loop            = 0
                self.ui.progressBar.setMaximum (len(mayaList))
                
                for eachMaya in mayaList :         
                    mayaFile    = str (eachMaya.toolTip (0))

                    #Create Batach File
                    if os.path.isfile (self.tempDirectory + '/smartMaya_init.bat') :
                        try :
                            os.remove(self.tempDirectory + '/smartMaya_inits.bat')
                        except Exception as result :
                            print result

                    write_bat   = open (self.tempDirectory + '/smartMaya_init.bat', 'w')                        
                    batLine     = '\"' + currentMayaPath + '/bin/mayapy.exe\" ' + '\"' + self.tempDirectory + '/smFunction_init.py' + '\"'               
                    write_bat.write (batLine)
                    write_bat.close ()

                    #Create python function file
                    if os.path.isfile (self.tempDirectory + '/smFunction_init.py') :
                        try :
                            os.remove(self.tempDirectory + '/smFunction_init.py')
                        except Exception as result :
                            print result

                    importLines     = ['import sys', 'sys.path.append (''\'' + currentMayaPath + '/devkit/other/pymel/extras/completion/py' + '\''')',
                                       'import maya.standalone', 'maya.standalone.initialize()', 'import maya.cmds as cmds', 'import maya.mel as mel']
                    fileOpen        = 'cmds.file (\'' + mayaFile + '\', f=1, iv=1, o=1)'
                    scriptPath      = ''
                    
                    if scriptFile.endswith ('.mel') :
                        scriptPath  = 'mel.eval (\'source \"%s\";\')' % scriptFile
                        #mel.eval ('source \"F:/My Work/dumps/My script/pythonApplication/smartTool/Applications/smartMaya/scripts/geometryCheck.mel\";')
                    
                    if scriptFile.endswith ('.py') or scriptFile.endswith ('.pyc') :
                        scriptPath      = 'sys.path.insert (0, \'' + os.path.dirname (scriptFile) + '\')\nimport ' + os.path.basename (scriptFile).split('.')[0]
               
                    writrFunction_init      = open (self.tempDirectory + '/smFunction_init.py', 'w')                   
                    for eachImportLine in importLines :                      
                        writrFunction_init.write (eachImportLine + '\n')

                    fileSplit       = os.path.splitext (mayaFile)
                    sMayaFile       = '%s%s%s' % (fileSplit[0], '_smartMaya', fileSplit[1])
                    version         = 'cmds.file (rename=\'%s\')'% sMayaFile + '\ncmds.file (f=1, save=1)'

                    writrFunction_init.write (fileOpen + '\n' + scriptPath + '\n' + version)
                    writrFunction_init.close ()
                    
                    os.system (self.tempDirectory + '/smartMaya_init.bat')
                 
                    if os.path.isfile (self.tempDirectory + '/smartMaya_init.bat') :
                        try :
                            os.remove(self.tempDirectory + '/smartMaya_init.bat')
                        except Exception as result :
                            print result
                            
                    if os.path.isfile (self.tempDirectory + '/smFunction_init.py') :
                        try :
                            os.remove(self.tempDirectory + '/smFunction_init.py')
                        except Exception as result :
                            print result

              
                    '''
                    #Old settinf        
                    cmds.file (f=1, new=1)
                    self.result ('\t\t' + mayaFile)
                    
                    self.ui.progressBar.setFormat ('Reading maya file\t- ' + mayaFile.expandtabs(4))                
                    self.ui.progressBar.setValue (loop)
                    
                    cmds.file (mayaFile, iv=1, o=True)

                    if scriptFile.endswith ('.mel') :
                        mel.eval ('source "%s";' % scriptFile)

                    if scriptFile.endswith ('.py') or scriptFile.endswith ('.pyc') :
                        sys.path.insert (0, os.path.dirname (scriptFile))
                        modules     = map(__import__, [os.path.basename (scriptFile).split('.')[0]])
                        #reload(modules[0])
                        #modules[0].function ()

                    self.ui.progressBar.setFormat ('Updating maya file\t- please wait'.expandtabs(4))                
                    #self.ui.progressBar.setValue (loop)
                    
                    cmds.file (rename=sMayaFile)
                    #cmds.file (f=1, save=1, type=self.gv.mayaType[1])            
                    cmds.file (f=1, save=1)
                    
                    self.ui.progressBar.setFormat ('Updated version is\t' + sMayaFile.expandtabs(4))                
                    #self.ui.progressBar.setValue (loop)
                    '''                    
                     
                    self.result ('\tUpdated version is\n\t\t' + sMayaFile)
                    os.startfile (os.path.dirname (sMayaFile))
                    loop += 1
                    
                self.ui.progressBar.setValue (100)
            else :
                self.result ('\tPlease select the script file')
        else :
            self.result ('\tPlease select the maya file')
            
            
    def result (self, message) :
        print message.expandtabs(4)
        self.ui.textEdit_result.append (message.expandtabs(4))


if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    windowA = SMARTMAYA ()
    if prefLoad==1 : 
        windowA.show ()
    sys.exit (app.exec_())
