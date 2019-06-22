'''
studioImage.py 0.0.1 
Date: January 16, 2019
Last modified: June 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import tempfile

from PySide2 import QtGui
from PySide2 import QtCore

from maya import OpenMaya
from maya import OpenMayaUI

from shaderLibrary_maya2017 import resources


class ImageCalibration(object):

    def __init__(self, path=None, name=None, format='png'):
        self.name = name
        self.format = format
        if not path:
            self.image_file = os.path.join(
                tempfile.gettempdir(), 'studio_image_snapshot.%s' % self.format)
        elif path and name:
            self.image_file = os.path.join(path, '%s.%s' % (name, format))
        self.unknown_icon = os.path.join(
            resources.getIconPath(), 'unknown.png')

    def create(self, width=2048, height=2048):
        m_image = self.vieportSnapShot()
        output_path = self.writeImage(m_image, width=width, height=height)
        return m_image, output_path

    def vieportSnapShot(self):
        m3d_view = OpenMayaUI.M3dView.active3dView()
        if not m3d_view.isVisible():
            OpenMaya.MGlobal.displayWarning('Active 3d View not visible!...')
            return
        m3d_view.refresh(True, True, True)
        m_image = OpenMaya.MImage()
        m3d_view.readColorBuffer(m_image, True)
        return m_image

    def writeImage(self, m_image, width=2048, height=2048):
        if not m_image:
            m_image = OpenMaya.MImage()
            m_image.readFromFile(self.unknown_icon)
        m_image.writeToFileWithDepth(self.image_file, self.format, False)
        self.keepAspectRatio(out_file=self.image_file)
        output_path = self.imageResize(output_path=self.image_file)
        return output_path

    def keepAspectRatio(self, out_file=None):
        q_image = QtGui.QImage(self.image_file)
        q_size = q_image.size()
        min_value = min([q_size.width(), q_size.height()])
        max_value = max([q_size.width(), q_size.height()])
        width, height = min_value, min_value
        length_x = (max_value / 2) - (min_value / 2)
        length_y = 0
        if q_size.width() < q_size.height():
            length_x = 0
            length_y = (max_value / 2) - (min_value / 2)
        copy = q_image.copy(length_x, length_y, width, height)
        copy.save(out_file)
        return True

    def imageResize(self, output_path=None, width=2048, height=2048):
        if not output_path:
            output_path = self.image_file
        q_image = QtGui.QImage(self.image_file)
        scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        scaled.save(output_path)
        return output_path

# end ####################################################################
