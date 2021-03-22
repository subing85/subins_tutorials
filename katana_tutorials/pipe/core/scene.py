import os
import re  # regular expression
import shutil

from Katana import PyXmlIO
from Katana import KatanaFile
from Katana import NodegraphAPI

from core import nodegraph


def get_current_scene():    
    '''
    :description get the current scene path
    :param None
    :example
        from core import scene
        scene.get_current_scene()
    '''    
    # NodegraphAPI.GetProjectFile()
    # NodegraphAPI.GetProjectAssetID()   
    return NodegraphAPI.GetSourceFile()


def get_scene_directory():
    '''
    :description get the current scene directory
    :param None
    :example
        from core import scene
        scene.get_scene_directory()    
    '''     
    return NodegraphAPI.GetProjectDir()


def get_scene_name():
    '''
    :description get the current scene name
    :param None
    :example
        from core import scene
        scene.get_scene_name()        
    '''       
    return NodegraphAPI.GetKatanaSceneName()


def new_katana_scene():
    '''
    :description to create new katana scene
    :param None
    :example
        from core import scene
        scene.new_katana_scene()               
    '''
    KatanaFile.New()
    return True


def open_katana_scene(katana_scene):  
    '''
    :description to open the specific katana scene
    :param katana_scene <str>   
    :example
        from core import scene
        scene.open_katana_scene()        
    '''      
    if not os.path.isfile(katana_scene):
        print '#warnings: not found katana scene'
        return        
    KatanaFile.Load(katana_scene, isCrashFile=False)
    print '#info: open katana scene', katana_scene
    return True


def save_katana_scene(katana_scene, force=False):
    '''
    :description to save the current scene, force true is to overwrite the scene, if scene exists
    :param katana_scene <str>
    :param force <bool> 
    :example
        from core import scene
        scene.save_katana_scene()      
    '''
    if os.path.isfile(katana_scene) and not force:        
        print '#warnings: already found katana scene'
        return
    if not os.path.isdir(os.path.dirname(katana_scene)):
        os.makedirs(os.path.dirname(katana_scene))        
    KatanaFile.Save(katana_scene, extraOptionsDict=None)
    print '#info: save katana scene', katana_scene
    return True


def incremental_saving():
    '''
    :description incremental saving, need to save manual at the first time
    :param None
    :example
        from core import scene
        scene.incremental_saving()      
    '''    
    current_directory = get_scene_directory()
    if not current_directory:
        print '#warnings: please save first version and try'
        return
    scene_name = get_scene_name()
    next_version = '%s_%s' % (scene_name, 1)
    digits = re.findall('\d+', scene_name, flags=0)
    if digits:
        increment = int(digits[-1][-1]) + 1
        next_digit = '%s%s' % (digits[-1][0:-1], increment)
        prefix = scene_name.rsplit(digits[-1], 1)
        next_version = prefix[0] + next_digit + prefix[1]
    next_katana_scene = os.path.join(
        current_directory, '%s.katana' % next_version)
    save_katana_scene(next_katana_scene, force=True)    
    print next_katana_scene
    return True
    
    
def export_katana_nodes(knodes, katana_scene, force=False):
    '''
    :description to export the katana nodes from the current scene ,
        force true is to overwrite the scene, if scene exists
    :param knodes <list>
    :param katana_scene <str>
    :param force <bool>
    :example
        from core import scene
        knodes = NodegraphAPI.GetAllSelectedNodes()
        katana_scene = '/venture/shows/katana_tutorials/tmp/export_03.katana'
        scene.export_katana_nodes(knodes, katana_scene)      
    '''      
    knodes = nodegraph.get_katana_nodes(knodes)
    if not knodes:        
        print '#warnings: not found valid katana nodes'
        return
    if os.path.isfile(katana_scene) and not force:        
        print '#warnings: already found katana scene'
        return
    if not os.path.isdir(os.path.dirname(katana_scene)):
        os.makedirs(os.path.dirname(katana_scene))
    KatanaFile.Export(katana_scene, knodes, extraOptionsDict=None)
    print '#info: export nodes'
    for knode in knodes:
        print '\t', knode.getName()
    return True


def import_katana_scene(katana_scene):
    '''
    :description to import the katana scene
    :param katana_scene <str>
    :example
        from core import scene
        katana_scene = '/venture/shows/katana_tutorials/tmp/export_03.katana'
        scene.import_katana_scene(katana_scene)      
    '''       
    if not os.path.isfile(katana_scene):
        print '#warnings: not found katana scene'
        return
    knodes = KatanaFile.Import(katana_scene, floatNodes=False)
    print '#info: import nodes'
    for knode in knodes:
        print '\t', knode.getName()
    return True        


def nodes_to_xml_element(knodes):
    '''
    :description to convert katana nodes(NodegraphAPI nodes) to xml element
    :param knodes <list>
    :example
        from core import scene
        knodes = NodegraphAPI.GetAllSelectedNodes()
        scene.nodes_to_xml_element(knodes)   
    '''       
    xml_element = NodegraphAPI.BuildNodesXmlIO(knodes)
    return xml_element


def nodes_to_xml_file(knodes, xml_scene, force=False):
    '''
    :description to convert katana nodes to xml file
    :param knodes <list>
    :param xml_scene <str>
    :param force <bool>
    :example
        from core import scene
        knodes = NodegraphAPI.GetAllSelectedNodes()
        xml_scene = '/venture/shows/katana_tutorials/tmp/test_01.xml'
        scene.nodes_to_xml_file(knodes, xml_scene)   
    '''       
    knodes = nodegraph.get_katana_nodes(knodes)
    if not knodes:        
        print '#warnings: not found valid katana nodes'
        return
    if os.path.isfile(xml_scene) and not force:        
        print '#warnings: already found katana scene xml'
        return
    if not os.path.isdir(os.path.dirname(xml_scene)):
        os.makedirs(os.path.dirname(xml_scene))   
    xml_element = nodes_to_xml_element(knodes)    
    xml_element_to_xml_file(xml_element, xml_scene)
    print '#info: write xml scene'
    print '\t', xml_scene
    return xml_element


def xml_element_to_xml_file(xml_element, xml_scene):
    '''
    :description to create xml file from xml element
    :param xml_element <PyXmlIO.Element>
    :param xml_scene <str>
    :example
        from core import scene
        xml_scene = '/venture/shows/katana_tutorials/tmp/test_01.xml'
        scene.xml_element_to_xml_file(xml_element, xml_scene)   
    '''       
    xml_element.write(xml_scene)
    return True


def xml_file_to_nodes(xml_scene, parent=None):
    '''
    :description to create katana nodes from xml file
    :param xml_scene <str>
    :param parent <Nodegraph Node Object>
    :example
        from core import scene
        xml_scene = '/venture/shows/katana_tutorials/tmp/test_01.xml'
        scene.xml_file_to_nodes(xml_scene)   
    '''      
    xml_element = xml_fie_to_xml_element(xml_scene)
    if not xml_element:
        print '#warnings: not valid xml element'        
        return None
    knodes = xml_element_to_nodes(xml_element, parent=parent)
    print '#info: import nodes from xml file'
    for knode in knodes:
        print '\t', knode.getName()
    return knodes


def xml_fie_to_xml_element(xml_scene):
    '''
    :description to convert xml file to xml element
    :param xml_scene <str>
    :example
        from core import scene
        xml_scene = '/venture/shows/katana_tutorials/tmp/test_01.xml'
        scene.xml_fie_to_xml_element(xml_scene)   
    '''     
    if not os.path.isfile(xml_scene):
        print '#warnings: not found xml scene'
        return    
    xml_element, upgraded = NodegraphAPI.LoadElementsFromFile(xml_scene, versionUp=True)
    return xml_element


def xml_file_to_pyxml_element(xml_scene):
    '''
    :description to convert xml file to xml element using PyXmlIO class
    :param xml_scene <str>
    :example
        from core import scene
        xml_scene = '/venture/shows/katana_tutorials/tmp/test_01.xml'
        scene.xml_file_to_pyxml_element(xml_scene)   
    '''       
    if not os.path.isfile(xml_scene):
        print '#warnings: not found xml scene'
        return
    parser = PyXmlIO.Parser()
    xml_element = parser.parse(xml_scene)
    return  xml_element 


def xml_element_to_nodes(xml_element, parent=None):
    '''
    :description to create katana nodes from xml element
    :param xml_element <PyXmlIO.Element>
    :param parent <Nodegraph Node Object>
    :example
        from core import scene
        scene.xml_element_to_nodes(xml_element)   
    '''       
    if not parent:
        parent = NodegraphAPI.GetRootNode()
    knodes = KatanaFile.Paste(xml_element, parent)
    return knodes


def xml_string_to_xml_element(xml_string):
    '''
    :description to convert xml string to xml element
    :param xml_string <str>
    :example
        from core import scene
        scene.xml_string_to_xml_element(xml_element)   
    '''  
    xml_element, upgraded = NodegraphAPI.LoadElementsFromString(xml_string, versionUp=True)
    return xml_element


def xml_string_to_pyxml_element(xml_string):
    '''
    :description to convert xml string to xml element using PyXmlIO class
    :param xml_string <str>
    :example
        from core import scene
        scene.xml_string_to_pyxml_element(xml_element)   
    '''     
    parser = PyXmlIO.Parser()
    xml_element = parser.parseString(xml_string)
    return xml_element


def xml_element_to_katana_scene(katana_scene, xml_element, force=False):
    '''
    :description to create katana scene from xml element,
        force true is to overwrite the scene, if scene exists
    :param katana_scene <str>
    :param xml_element <PyXmlIO.Element>    
    :param force <bool>
    :example
        from core import scene
        katana_scene = '/venture/shows/katana_tutorials/tmp/export_03.katana'
        scene.xml_element_to_katana_scene(katana_scene, xml_element)      
    '''   
    if os.path.isfile(katana_scene) and not force:        
        print '#warnings: already found katana scene'
        return
    if not os.path.isdir(os.path.dirname(katana_scene)):
        os.makedirs(os.path.dirname(katana_scene))              
    NodegraphAPI.WriteKatanaFile(katana_scene, xml_element, compress=True, archive=True, opaqueParams=None)
    return True


def xml_file_to_katana_scene(katana_scene, xml_scene, force=False):
    '''
    :description to create katana scene from xml file,
        force true is to overwrite the scene, if scene exists
    :param katana_scene <str>
    :param xml_scene <str>    
    :param force <bool>
    :example
        from core import scene
        katana_scene = '/venture/shows/katana_tutorials/tmp/export_03.katana'
        xml_scene = '/venture/shows/katana_tutorials/tmp/export_03.xml'
        scene.xml_file_to_katana_scene(katana_scene, xml_scene)      
    '''     
    if os.path.isfile(katana_scene) and not force:        
        print '#warnings: already found katana scene'
        return
    if not os.path.isdir(os.path.dirname(katana_scene)):
        os.makedirs(os.path.dirname(katana_scene))        
    xml_element = xml_fie_to_xml_element(xml_scene) 
    result = xml_element_to_katana_scene(katana_scene, xml_element, force=force)
    return result


def xml_string_to_katana_scene(katana_scene, xml_string, force=False):
    '''
    :description to create katana scene from xml string,
        force true is to overwrite the scene, if scene exists
    :param katana_scene <str>
    :param xml_string <str>    
    :param force <bool>
    :example
        from core import scene
        katana_scene = '/venture/shows/katana_tutorials/tmp/export_03.katana'
        scene.xml_string_to_katana_scene(katana_scene, xml_string)      
    '''     
    if os.path.isfile(katana_scene) and not force:        
        print '#warnings: already found katana scene'
        return
    if not os.path.isdir(os.path.dirname(katana_scene)):
        os.makedirs(os.path.dirname(katana_scene))         
    xml_element = xml_string_to_xml_element(xml_string)       
    result = xml_element_to_katana_scene(katana_scene, xml_element, force=force)
    return result


def convert_to_live_group(kgroup, publish_path): 
    '''
    :description to convert group to live group (external node graph file)
        force true is to overwrite the scene, if scene exists
    :param kgroup <Group GroupNode>
    :param publish_path <str>    
    :example
        from core import scene
        publish_path = '/venture/shows/katana_tutorials/tmp/live_group_v1.livegroup'
        scene.convert_to_live_group(kgroup, publish_path)      
    '''         
    if isinstance(kgroup, str) or isinstance(kgroup, unicode):
        kgroup = NodegraphAPI.GetNode(kgroup)        
    if kgroup.getType != 'Group':
        print '#warning: not valid group node'
        return    
    klive_group = NodegraphAPI.ConvertGroupToLiveGroup(kgroup)
    publish_path = klive_group.publishAssetAndFinishEditingContents(
        filenameOrAssetID=publish_path)
    return klive_group, publish_path


def make_editable_live_group(klive_group):
    '''
    :description make live group node editable, allowing changes to its contents
    :param klive_group <LiveGroup LiveGroupNode>
    :example
        from core import scene
        scene.make_editable_live_group(klive_group)  
    '''
    if isinstance(klive_group, str) or isinstance(klive_group, unicode):
        klive_group = NodegraphAPI.GetNode(klive_group)        
    if klive_group.getType != 'LiveGroup':
        print '#warning: not valid live group node'
        return
    valid = klive_group.makeEditable(includingAllParents=False)
    return valid


def convert_live_group_to_group(klive_group):
    '''
    :description converts live group node to a group node
    :param klive_group <LiveGroup LiveGroupNode>
    :example
        from core import scene
        scene.convert_live_group_to_group(klive_group)  
    '''      
    if isinstance(klive_group, str) or isinstance(klive_group, unicode):
        klive_group = NodegraphAPI.GetNode(klive_group)        
    if klive_group.getType != 'LiveGroup':
        print '#warning: not valid live group node'
        return                  
    kgroup = klive_group.convertToGroup()
    return kgroup


def look_file_bake(klook_bake_node, look_file_path, bake_type=0, force=False):
    if isinstance(klook_bake_node, str) or isinstance(klook_bake_node, unicode):
        klook_bake_node = NodegraphAPI.GetNode(klook_bake_node)      
    if os.path.isfile(look_file_path) and not force:        
        print '#warnings: already found klf file'
        return
    if os.path.isfile(look_file_path):
        os.remove(look_file_path)
    if os.path.isdir(look_file_path):
        shutil.rmtree(look_file_path)
    if not os.path.isdir(os.path.dirname(look_file_path)):
        os.makedirs(os.path.dirname(look_file_path))
    if bake_type == 0:   
        # write all the passes in a lookfile to a compound file (currently a ZIP).
        klook_bake_node.WriteToCompoundFile(
            None, look_file_path, includeGlobalAttributes=True, includeLodInfo=True)
    if bake_type == 1:  
        # look file bake instance, normal bake
        klook_bake_node.WriteToLookFile(None, look_file_path)
    if bake_type == 2:     
        # bake all look file passes, this is a high level bake [baking attributes from the root location]
        klook_bake_node.WriteToAsset(None, look_file_path)

    if bake_type == 3:     
        # lower level bake, bake one or all look file passes into a directory   
        klook_bake_node.WriteToDirectory(
            None, look_file_path, includeGlobalAttributes=True, includeLodInfo=True)
    return True


def clear_global_variables():
    roo_node = NodegraphAPI.GetRootNode()
    variable_parameter = roo_node.getParameter('variables')
    for child in variable_parameter.getChildren():
        variable_parameter.deleteChild(child)    


def create_global_variable(label, values, force=False):
    '''
    :description create global variables on root node
    :param label <str>
    :param values <list>
    :param force <bool>    
    :example
        from core import scene
        label = 'camera'
        values = ['alembic1', 'default1', 'default2', 'default3']
        scene.create_global_variable(label, values, force=True)
    '''     
    roo_node = NodegraphAPI.GetRootNode()
    variable_parameter = roo_node.getParameter('variables')
    exists_variables = []
    for child in variable_parameter.getChildren():
        exists_variables.append(child.getName())
    if label in exists_variables and not force:
        print '#warnings: already exists the global variable', label
        return
    if label in exists_variables:       
        exists_variable = variable_parameter.getChild(label)
        variable_parameter.deleteChild(exists_variable)
    child_group = variable_parameter.createChildGroup(label)
    child_group.createChildNumber('enable', 1)
    children = child_group.createChildStringArray('options', len(values), 1)
    for index, child in enumerate(children.getChildren()):
        child_group.createChildString('value', values[index])
        child.setValue(values[index], 1)
    return True


def create_custom_global_variable(label, values, force=False):
    '''
    :description create custom global variables on root node
    :param label <str>
    :param values <list>
    :param force <bool>    
    :example
        from core import scene
        label = 'camera'
        values = ['alembic1', 'default1', 'default2', 'default3']
        scene.create_custom_global_variable(label, values, force=True)
    '''    
    roo_node = NodegraphAPI.GetRootNode()
    variable_parameter = roo_node.getParameter('variables')    
    exists_variables = []
    for child in variable_parameter.getChildren():
        exists_variables.append(child.getName())
    if label in exists_variables and not force:
        print '#warnings: already exists the global variable', label
        return
    if label in exists_variables:       
        exists_variable = variable_parameter.getChild(label)
        variable_parameter.deleteChild(exists_variable)            
    variable = variable_parameter.createChildString(label, label)
    hint = {
        'widget': 'popup',
        'options': values
        }
    variable.setHintString(str(hint))
    variable.setValue(values[0], 1.0)

