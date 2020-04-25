import os


def image_resize(image_path, output_path, width=2048, height=2048):
    try:
        from PySide2 import QtGui
        from PySide2 import QtCore
    except:   
        from PyQt4 import QtGui
        from PyQt4 import QtCore    
    
    q_image = QtGui.QImage(image_path)
    sq_scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding) 
    if sq_scaled.width() <= sq_scaled.height():
        x = 0
        y = (sq_scaled.height() - height) / 2
    elif sq_scaled.width() >= sq_scaled.height():
        x = (sq_scaled.width() - width) / 2
        y = 0
    copy = sq_scaled.copy(x, y, width, height) 
    if not os.path.isdir(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))        
    copy.save(output_path)
    output_path
    return output_path