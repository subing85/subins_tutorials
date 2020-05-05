import shiboken2

from maya import cmds
from maya import OpenMaya
from maya import OpenMayaUI
from PySide2 import QtWidgets
    

def get_qwidget():
    qwidget = OpenMayaUI.MQtUtil.mainWindow()
    main_window = shiboken2.wrapInstance(long(qwidget), QtWidgets.QWidget)
    return main_window


def get_main_window():
    from maya import cmds
    maya_windows = [each_win for each_win in cmds.lsUI(
        wnd=True) if cmds.window(each_win, q=True, mw=True)]
    return maya_windows[0]


def remove_exists_window(object_name):
    wind = OpenMayaUI.MQtUtil()
    if not wind.findWindow(object_name):
        return
    mel_command = 'deleteUI \"%s\"' % object_name 
    OpenMaya.MGlobal.executeCommand(mel_command, False, True) 


