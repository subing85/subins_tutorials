import os
import resources

from core import scene
from core import versions

from PyQt4 import QtGui

from Katana import NodegraphAPI


def create_node():    
    template_path = resources.get_template_path()    
    latest_version = versions.get_latest_version(template_path, 'lookdev')
    if not latest_version:
        message = 'not found any publish versions'
        QtGui.QMessageBox.warning(
            None, 'Warning', message, QtGui.QMessageBox.Ok)
        return            
    xml_scene = os.path.join(
        template_path, 'lookdev', latest_version, 'lookdev.xml')     
    if not os.path.isfile(xml_scene):
        message = 'not found xml in the latest publish \n<%s>\n<%s>' % (
            latest_version, xml_scene)
        QtGui.QMessageBox.warning(
            None, 'Warning', message, QtGui.QMessageBox.Ok)
        return     
    scene.new_katana_scene()    
    root_node = NodegraphAPI.GetRootNode()
    knodes = scene.xml_file_to_nodes(xml_scene, parent=root_node)
    print '# info: lookdev template nodes'
    for knode in knodes:
        print '\t', knode.getName()
    message = [
        'template type: '.rjust(15) + 'lookdev',
        'version: '.rjust(15) + latest_version,
        'path: '.rjust(15) + xml_scene
        ]
    QtGui.QMessageBox.information(
            None, 'success', '\n'.join(message), QtGui.QMessageBox.Ok)
    print '\n'.join(message)
    
    
