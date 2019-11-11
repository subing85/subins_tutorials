'''
studioImage.py 0.0.1 
Date: January 16, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import tempfile

from PySide import QtGui
from PySide import QtCore

from studioPipe import resources


class ImageCalibration(object):

    def __init__(self, imgae_file=None, dirname=None, file_name=None, format='png'):
        self.image_file = imgae_file
        self.dirname = dirname
        self.file_name = file_name
        self.format = format
                
        self.unknown_icon = os.path.join(
            resources.getIconPath(), 'unknown.png')

    def create(self, width=2048, height=2048):
        try:
            m_image = self.vieport_snapshot()
            output_path = self.write_maya_image(m_image)
        except:
            output_path = self.unknown_icon
        q_image = QtGui.QImage(output_path)
        return q_image, output_path

    def vieport_snapshot(self):
        from maya import OpenMaya
        from maya import OpenMayaUI
        m3d_view = OpenMayaUI.M3dView.active3dView()
        if not m3d_view.isVisible():
            OpenMaya.MGlobal.displayWarning('Active 3d View not visible!...')
            return
        m3d_view.refresh(True, True, True)
        m_image = OpenMaya.MImage()
        m3d_view.readColorBuffer(m_image, True)
        return m_image

    def write_maya_image(self, m_image):
        if not m_image:
            m_image = OpenMaya.MImage()
            m_image.readFromFile(self.unknown_icon)
        m_image.writeToFileWithDepth(self.image_file, self.format, False)
        self.keep_aspect_ratio(output_path=self.image_file)
        output_path = self.image_resize(output_path=self.image_file)
        return output_path

    def write_image(self, q_image):
        if not q_image:
            q_image = QtGui.QImage(self.unknown_icon)
        result = q_image.save(self.image_file, self.format.upper())
        return result

    def image_resize(self, output_path=None, width=2048, height=2048):
        if not output_path:
            output_path = self.image_file
        q_image = QtGui.QImage(self.image_file)
        scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        scaled.save(output_path)
        return output_path
    
    def set_studio_size(self, source_image=None, output_path=None, width=2048, height=2048):
        if source_image:
            self.image_file = source_image
        result, q_image = self.keep_aspect_ratio(output_path=None, width=width, height=height)
        if not output_path:
            output_path = os.path.join(
                tempfile.gettempdir(), 'studio_image_snapshot.%s' % self.format)
        q_image.save(output_path)
        a = QtGui.QImage()
        a.setText('aaaa', '33333333333')
        
        return q_image, output_path
    
    def keep_aspect_ratio(self, output_path=None, width=2048, height=2048):
        q_image = QtGui.QImage(self.image_file)
        sq_scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding) 
        if sq_scaled.width() <= sq_scaled.height():
            x = 0
            y = (sq_scaled.height()-height)/2
        elif sq_scaled.width() >= sq_scaled.height():
            x = (sq_scaled.width()-width)/2
            y = 0
        copy = sq_scaled.copy(x, y, width, height)
        if output_path:
            copy.save(output_path)
        return True, copy
    
    def set_qimage(self, path):
        q_image = QtGui.QImage(path)
        return q_image
       

# end ####################################################################
