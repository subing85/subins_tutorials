def get_qwidget():
    import shiboken2
    from maya import OpenMayaUI
    from PySide2 import QtWidgets
    qwidget = OpenMayaUI.MQtUtil.mainWindow()
    main_window = shiboken2.wrapInstance(long(qwidget), QtWidgets.QMainWindow)
    return main_window


def get_main_window():
    from maya import cmds
    maya_windows = [each_win for each_win in cmds.lsUI(
        wnd=True) if cmds.window(each_win, q=True, mw=True)]
    return maya_windows[0]


def remove_exists_window(object_name):
    from maya import OpenMayaUI
    from maya import cmds
    wind = OpenMayaUI.MQtUtil()
    if wind.findWindow(object_name):
        cmds.deleteUI(object_name)
