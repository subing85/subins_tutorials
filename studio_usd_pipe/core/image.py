import os
from PySide2 import QtGui
from PySide2 import QtCore

def image_resize(image_path, output_path, time_stamp=None, width=2048, height=2048):
    q_image = QtGui.QImage(image_path)
    sq_scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding) 
    if sq_scaled.width() <= sq_scaled.height():
        x = 0
        y = (sq_scaled.height() - height) / 2
    elif sq_scaled.width() >= sq_scaled.height():
        x = (sq_scaled.width() - width) / 2
        y = 0
    copy = sq_scaled.copy(x, y, width, height) 
    copy.save(output_path)
    if time_stamp:
        os.utime(output_path, (time_stamp, time_stamp))
    return output_path