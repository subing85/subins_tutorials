import os
import math
from maya import OpenMaya

from renderLibrary.api import mayaNode


def getRenderSteup():
    
    '''
    :description
        get the current render steup whether Legacy or New Render Setup
        1 =  (new) Render Setup is active
        0 = Legacy Render Layers is active  
    :example
    from renderLibrary.utils import studioMaya
    studioMaya.getRenderSteup()
            
    '''
    mcommand_result = OpenMaya.MCommandResult()
    command = 'optionVar -q \"renderSetupEnable\";'
    OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
    mscript_util = OpenMaya.MScriptUtil()
    index_ptr = mscript_util.asIntPtr()
    mcommand_result.getResult(index_ptr)    
    _value = mscript_util.getInt(index_ptr)
    
    setups = {
        0: 'Legacy Render Layers',
        1: 'Render Setup'
        }
    OpenMaya.MGlobal.displayInfo('current render: %s' % setups.get(_value))
    return _value 


def getRenderEngine():
    mcommand_result = OpenMaya.MCommandResult()
    command = 'getAttr \"defaultRenderGlobals.currentRenderer\"',
    OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
    render_engine = mcommand_result.stringResult() 
    OpenMaya.MGlobal.displayInfo('current render engine: %s' % render_engine)
    return render_engine


def selectLayer(layer):
    mcommand_result = OpenMaya.MCommandResult()
    command = 'editRenderLayerGlobals -currentRenderLayer %s;' % layer
    OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)


def getSelectedNodes():
    selected = OpenMaya.MSelectionList()
    OpenMaya.MGlobal.getActiveSelectionList(selected)
    nodes = []
    selected.getSelectionStrings(nodes)
    return nodes


def getRootNode(node):
    mn = mayaNode.Connect()
    root_node = mn.getRootNode(node)
    return root_node

    
def getGeometries(layer, root_node):
    selectLayer(layer)
    mn = mayaNode.Connect()    
    mesh_hierarchy = mn.getMeshHierarchy(root_node)
    
    _geometries = {}
    
    for index in range (mesh_hierarchy.length()):
        node = mesh_hierarchy[index].fullPathName()
        _node = mesh_hierarchy[index].partialPathName()
        
        _geometries[node] = {}
        
        mesh_hierarchy[index].extendToShape()
        shape = mesh_hierarchy[index].partialPathName()
        
        _geometries[node]['shape'] = shape
        
        shading_engines = mn.getShadingEngines(mesh_hierarchy[index])
        
        shading = {}
             
        for x in range(shading_engines.length()):
            
            shader = mn.getShader(shading_engines[x])
            materials = mn.getMaterialNodes(shader)            
            members = mn.getAssignComponents(shading_engines[x])
            members = set(sum(members.values(), []))
            
            _members = []
            for member in members:                
                if not member.startswith(_node):
                    continue
                _members.append(member)
           
            sg_mfnnode = OpenMaya.MFnDependencyNode(shading_engines[x])
            sh_mfn_node = OpenMaya.MFnDependencyNode(shader)
            
            _materials = []            
            for m in range(materials.length()):
                ma_mfnnode = OpenMaya.MFnDependencyNode(materials[m])
                _materials.append(ma_mfnnode.name())
            
            contents = {
                'shading_engines': sg_mfnnode.name(),
                'shader': sh_mfn_node.name(),
                'materials': _materials,
                'members': _members
                }
            
            shading.setdefault(x, contents)

        _geometries[node]['shading'] = shading

    return _geometries


def getShaders(layer, root_node):
    selectLayer(layer)
    mn = mayaNode.Connect()    
    mesh_hierarchy = mn.getMeshHierarchy(root_node)
    
    _shaders, _nodes = {}, []
    
    for index in range (mesh_hierarchy.length()):
        node = mesh_hierarchy[index].fullPathName()
        _node = mesh_hierarchy[index].partialPathName()
        mesh_hierarchy[index].extendToShape()
        shape = mesh_hierarchy[index].partialPathName()

        shading_engines = mn.getShadingEngines(mesh_hierarchy[index])
             
        for x in range(shading_engines.length()):

            sg_mfnnode = OpenMaya.MFnDependencyNode(shading_engines[x])
            if sg_mfnnode.name() in _shaders:
                _shaders[sg_mfnnode.name()].setdefault('nodes', []).append(node)
                _shaders[sg_mfnnode.name()].setdefault('shapes', []).append(shape)
                continue
  
            shader = mn.getShader(shading_engines[x])
            materials = mn.getMaterialNodes(shader)            
            members = mn.getAssignComponents(shading_engines[x])
            members = set(sum(members.values(), []))
            
            _members = []
            for member in members:                
                if not member.startswith(_node):
                    continue
                _members.append(member)
           
            sh_mfn_node = OpenMaya.MFnDependencyNode(shader)
            
            _materials = []            
            for m in range(materials.length()):
                ma_mfnnode = OpenMaya.MFnDependencyNode(materials[m])
                _materials.append(ma_mfnnode.name())
            
            contents = {
                'shader': sh_mfn_node.name(),
                'materials': _materials,
                'members': _members,
                'nodes': [node],
                'shapes': [shape]
                }
            _shaders.setdefault(sg_mfnnode.name(), contents)
            _nodes.append(sg_mfnnode.name())
            _nodes.append(sh_mfn_node.name())
            _nodes.extend(_materials)

    return _shaders, _nodes


def getLights(layer):
    selectLayer(layer)
    
    mn = mayaNode.Connect()    
    members = mn.getRenderMembers(layer)
    node_types = getNodeTypes('light')
    
    _lights = {}
    
    for member in members:

        dagpath = mn.getDagPath(member)
        
        if dagpath.childCount():
            dagpath.extendToShape()  
                  
        node_type = getNodeType(dagpath.fullPathName())
        
        if node_type not in node_types:
            continue
        
        shape = dagpath.fullPathName()
        
        dagnode = OpenMaya.MFnDagNode(dagpath)
        mobject = dagnode.parent(0)
        _dagpath = OpenMaya.MDagPath()
        _dagpath.getAPathTo(mobject, _dagpath)
    
        contents = {
            'shape': shape
        }
        _lights.setdefault(_dagpath.fullPathName(), contents)
                
                
    return  _lights       
    
  
def getOverrides(layer, includes):
    '''
    :example
        from renderLibrary.utils import studioMaya
        studioMaya.getOverrides('batman')
    '''
    selectLayer(layer)
    
    if isinstance(includes, dict):       
        nodes = []
        for k, v in includes.items():
            nodes.append(k)
            if not v.get('shape'):
                continue
            nodes.append(v['shape'])
    else:
        nodes = includes
        
    mn = mayaNode.Connect()
    _overrides = {}
    for node in nodes:        
        overrides = mn.getOverrides(node, layer)
        if not overrides:
            continue
        _overrides.setdefault(node, overrides)
    
    return _overrides


def getRenderMembers(layer, includes):
    '''
    :example
        from renderLibrary.utils import studioMaya
        studioMaya.getRenderMembers('batman', typed=OpenMaya.MFn.kMesh)
    '''  
    
    selectLayer(layer)
    
    if isinstance(includes, dict):       
        nodes = []
        for k, v in includes.items():
            nodes.append(k)
            if not v.get('shape'):
                continue
            nodes.append(v['shape'])
    else:
        nodes = includes
    
    mn = mayaNode.Connect()    
    members = mn.getRenderMembers(layer)
    _members = []
    for member in members:
        if member not in nodes:
            continue
        _members.append(member)
    return _members


def getNodesTransform(nodes):
    _transform = {}
    for node in nodes:
        _values = getTransformValues(node)
        _transform.setdefault(node, _values)
    return _transform
        

def getTransformValues(node):
    mn = mayaNode.Connect()
    dagpath = mn.getDagPath(node)
    # get world sapce translate value
    transform_matrix = OpenMaya.MTransformationMatrix(dagpath.inclusiveMatrix())
    mvector = transform_matrix.getTranslation(OpenMaya.MSpace.kWorld)       
    
    # get world sapce rotate pivot value
    mfn_transform = OpenMaya.MFnTransform(dagpath)
    _transform_matrix = mfn_transform.transformation()
    mpoints = _transform_matrix.rotatePivot(OpenMaya.MSpace.kWorld)
    
    translate = [
        mvector.x + mpoints.x,
        mvector.y + mpoints.y,
        mvector.z + mpoints.z
        ]
    
    # get rotation value
    m_euler = transform_matrix.eulerRotation()
    angles = [m_euler.x, m_euler.y, m_euler.z]
    rotate = [math.degrees(angle) for angle in angles] 
    
    # get scale value
    scale_util = OpenMaya.MScriptUtil()
    scale_util.createFromList([0, 0, 0], 3)
    double = scale_util.asDoublePtr()
    transform_matrix.getScale(double, OpenMaya.MSpace.kWorld)
    scale = [OpenMaya.MScriptUtil.getDoubleArrayItem(double, x) for x in range(3)]       
       
    _transform = {
        'translate': translate,
        'rotate': rotate,
        'scale': scale
        }
    
    return _transform


def getNodesAttributes(nodes):
    
    if isinstance(nodes, dict):       
        _nodes = []
        for k, v in nodes.items():
            _nodes.append(k)
            if not v.get('shape'):
                continue
            _nodes.append(v['shape'])
    else:
        nodes = nodes
 
    node_attributes = {}
    
    for node in _nodes:
        attributes = getAttributeValue(node)
        node_attributes.setdefault(node, attributes)
    return node_attributes


def getAttributeValue(node):    
    mn = mayaNode.Connect()
    attributes = mn.getAttributes(node)
    return attributes


def addStudioAttribute(node, values):
    mn = mayaNode.Connect()
        
    mn.addStringATtributes(node, 'studioSceneDescription', 'ssd', value=str(values))


def exportSelection(nodes, path, **kwargs):
    format = kwargs.get('format') or 'mayaAscii'    
    preserved = kwargs.get('preserved') or False
    
    if os.path.isfile(path):
        try:
            os.chmod(path, 0777)
            os.remove(path)
        except Exception as error:
            print '#remove error', error
    
    mselection_list = OpenMaya.MSelectionList()
    for node in nodes:
        mselection_list.add(node)  
    OpenMaya.MGlobal.setActiveSelectionList(mselection_list)
    OpenMaya.MFileIO.exportSelected(path, format, preserved) 
    OpenMaya.MGlobal.clearSelectionList()
    
    
def getNodeTypes(typed):
    mcommand_result = OpenMaya.MCommandResult()
    command = 'listNodeTypes \"%s\";' % typed
    OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
    nodes = []
    mcommand_result.getResult(nodes)
    return nodes


def getNodeType(node):
    mcommand_result = OpenMaya.MCommandResult()
    mel_command = 'nodeType \"%s\"' % node
    OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, False)
    node_type = mcommand_result.stringResult()
    return node_type
             
