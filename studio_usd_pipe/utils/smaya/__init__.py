def get_qwidget():
    import shiboken2
    from maya import OpenMayaUI
    from PySide2 import QtWidgets
    qwidget = OpenMayaUI.MQtUtil.mainWindow()
    main_window = shiboken2.wrapInstance(long(qwidget), QtWidgets.QMainWindow)
    return main_window


def remove_exists_window(object_name):
    from maya import OpenMaya
    from maya import OpenMayaUI
    wind = OpenMayaUI.MQtUtil()
    if wind.findWindow(object_name):
        mel_command = 'deleteUI \"%s\"' % object_name 
        OpenMaya.MGlobal.executeCommand(mel_command, False, True) 
