from maya import OpenMaya

from renderLibrary.utils import mayaNode


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



def get():
    pass


def getRenderMembers(layer, typed=None):
    '''
    :example
        from renderLibrary.utils import studioMaya
        studioMaya.getRenderMembers('batman', typed=OpenMaya.MFn.kMesh)
    '''    
    selectLayer(layer)
    mcommand_result = OpenMaya.MCommandResult()
    command = 'editRenderLayerMembers -q %s;' % layer
    OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
    members = []
    mcommand_result.getResult(members)    
    if not typed:
        return members    
    _members = []
    for member in members:
        mn = mayaNode.Connect(node=member)
        dagpath = mn.getDagPath()        
        if not dagpath.hasFn(typed):
            continue
        _members.append(dagpath.fullPathName())
    return _members


def getOverrides(layer, typed=None):
    '''
    :example
        from renderLibrary.utils import studioMaya
        studioMaya.getOverrides('batman', typed=OpenMaya.MFn.kMesh)
    '''
    selectLayer(layer)    
    mcommand_result = OpenMaya.MCommandResult()
    command = 'editRenderLayerAdjustment -q -layer %s;' % layer
    OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
    plugs = []
    mcommand_result.getResult(plugs)    
    if not typed:
        return plugs
    _plugs = []
    for plug in plugs:
        mn = mayaNode.Connect(node=plug)
        mplug = mn.getMPlug() 
        dagpath = OpenMaya.MDagPath()
        dagpath.getAPathTo(mplug.node(), dagpath)    
        if not dagpath.hasFn(typed):
            continue        
        _plugs.append(plug)
    return _plugs        
             
