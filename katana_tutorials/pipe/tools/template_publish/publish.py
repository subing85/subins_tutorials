import os
import shutil

from core import scene
from core import nodegraph


def start_publish(directory, typed):    
    if os.path.isdir(directory):
        try:
            shutil.rmtree(directory)
        except Exception as error:
            print '#error %s' % (str(error))
    if not os.path.isdir(directory):
        os.makedirs(directory)        
    xml_scene = os.path.join(directory, '%s.xml' % typed)   
    scene_nodes = nodegraph.get_scene_katana_nodes()
    scene.nodes_to_xml_file(scene_nodes, xml_scene, force=True)    
    return True
     
