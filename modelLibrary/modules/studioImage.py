import os
import tempfile

from PySide import QtGui
from PySide import QtCore

from maya import OpenMaya
from maya import OpenMayaUI


class ImageCalibration(object):
    
    def __init__(self, path=None, format='png'):        
        self.image_file = path        
        self.format = format                
        if not path:
            self.image_file = os.path.join(tempfile.gettempdir(),
                                    'studio_image_snapshot.%s' % self.format)        
    
    def create(self, width=2048, height=2048):
        m_image = self.vieportSnapShot()
        output_path = self.writeImage(m_image, width=width, height=height)
        return output_path      
    
    def vieportSnapShot(self):      
        m3d_view = OpenMayaUI.M3dView.active3dView()
        m3d_view.refresh(False, True, True)
        m_image = OpenMaya.MImage()
        m3d_view.readColorBuffer(m_image, True)        
        return m_image
        
    def writeImage(self, m_image, width=2048, height=2048):               
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
        
        length_x = (max_value/2) - (min_value/2)
        length_y = 0
        
        if q_size.width()<q_size.height():
            length_x = 0
            length_y = (max_value/2) - (min_value/2)
        
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
    
    
    
    