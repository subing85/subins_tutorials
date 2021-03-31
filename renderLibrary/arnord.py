import mtoa.utils as utils
import mtoa.melUtils as melUtils
import mtoa.callbacks as callbacks
from collections import namedtuple
from itertools import groupby
import re
import arnold.ai_params
import maya.api.OpenMaya as om
import maya.mel as mel
import maya.cmds as cmds

BUILTIN_AOVS = (
                ('P',                   'vector'),
                ('Z',                   'float'),
                ('N',                   'vector'),
                ('opacity',             'rgb'),
                ('motionvector',        'rgb'),
                ('Pref',                'rgb'),
                ('raycount',            'float'),
                ('cputime',             'float'),
                ('ID',                  'uint'),
                ('RGBA',                'rgba'),
                ('direct',              'rgb'),
                ('indirect',            'rgb'),
                ('emission',            'rgb'),
                ('background',          'rgb'),
                ('diffuse',             'rgb'),
                ('specular',            'rgb'),
                ('transmission',        'rgb'),
                ('sss',                 'rgb'),
                ('volume',              'rgb'),
                ('albedo',              'rgb'),
                ('diffuse_direct',      'rgb'),
                ('diffuse_indirect',    'rgb'),
                ('diffuse_albedo',      'rgb'),
                ('specular_direct',     'rgb'),
                ('specular_indirect',   'rgb'),
                ('specular_albedo',     'rgb'),
                ('coat',                'rgb'),
                ('coat_direct',         'rgb'),
                ('coat_indirect',       'rgb'),
                ('coat_albedo',         'rgb'),
                ('sheen',                'rgb'),
                ('sheen_direct',         'rgb'),
                ('sheen_indirect',       'rgb'),
                ('sheen_albedo',         'rgb'),
                ('transmission_direct', 'rgb'),
                ('transmission_indirect','rgb'),
                ('transmission_albedo', 'rgb'),
                ('sss_direct',          'rgb'),
                ('sss_indirect',        'rgb'),
                ('sss_albedo',          'rgb'),
                ('volume_direct',       'rgb'),
                ('volume_indirect',     'rgb'),
                ('volume_albedo',       'rgb'),
                ('volume_opacity',      'rgb'),
                ('volume_Z',           'float'),
                ('shadow_matte',        'rgba'),
                ('AA_inv_density',      'float')

                )

# FIXME is there a way to avoid hardcoding this list ?
LIGHTING_AOVS = ['RGBA',         
                'direct',       
                'indirect',        
                'emission',        
                'diffuse',         
                'specular',        
                'transmission',    
                'sss',             
                'volume',          
                'diffuse_direct',  
                'diffuse_indirect',
                'diffuse_albedo',  
                'specular_direct',  
                'specular_indirect', 
                'specular_albedo',
                'coat',      
                'coat_direct',
                'coat_indirect',
                'coat_albedo',
                'transmission_direct', 
                'transmission_indirect',
                'transmission_albedo', 
                'sss_direct',
                'sss_indirect',
                'sss_albedo',
                'volume_direct', 
                'volume_indirect',
                'shadow_matte']

TYPES = (
    ("int",    arnold.ai_params.AI_TYPE_INT),
    ("uint",    arnold.ai_params.AI_TYPE_UINT),
    ("bool",   arnold.ai_params.AI_TYPE_BOOLEAN),
    ("float",  arnold.ai_params.AI_TYPE_FLOAT),
    ("rgb",    arnold.ai_params.AI_TYPE_RGB),
    ("rgba",   arnold.ai_params.AI_TYPE_RGBA),
    ("vector", arnold.ai_params.AI_TYPE_VECTOR),
    ("vector2", arnold.ai_params.AI_TYPE_VECTOR2),
    ("pointer",arnold.ai_params.AI_TYPE_POINTER))

defaultFiltersByName = {'Z' : 'closest', 'motion_vector' : 'closest', 'P' : 'closest', 'N' : 'closest', 'Pref' : 'closest', 'ID' : 'closest', 'AA_inv_density' : 'heatmap', 'volume_Z' : 'closest' }

GlobalAOVData = namedtuple('GlobalAOVData', ['name', 'attribute', 'type'])

SceneAOVData = namedtuple('SceneAOVData', ['name', 'type', 'index', 'node'])

# Return a list of nreq free indices that do not appear in
# the sorted list logIdxList
def listAvailableIndices(logIdxList, nreq):
    free = []
    last = -1
    for idx in logIdxList:
        if idx > last+1:
            rem = min(nreq-len(free), idx-(last+1))
            if rem <= 0:
                return free
            for i in xrange(0, rem):
                free.append(last+1+i)
        last = idx
    rem = nreq-len(free)
    for i in xrange(0, rem):
        free.append(last+1+i)
    return free

def getShadingGroupAOVMap(nodeAttr):
    nodeAttr = str(nodeAttr)
    '''
    return a mapping from aov name to element 'aovName' plug on aiCustomAOVs, and the next available index
    '''
    lastIndex = -1
    nextIndex = 0
    nameToAttr = {}

    idx_list = cmds.getAttr(nodeAttr, mi=True) or []

    for i in idx_list:
        _a = '{}[{}]'.format(nodeAttr, i)
        name = cmds.getAttr('{}.aovName'.format(_a))
        if name:
            nameToAttr[name] = _a
        nextIndex = i+1
    return nameToAttr, nextIndex

def removeAliases(aovs):
    for sg in cmds.ls(type='shadingEngine'):
        for aov in aovs:
            try:
                cmds.removeMultiInstance(sg + '.ai_aov_' + aov.name)
            except RuntimeError, err:
                pass #print err

def addAliases(aovs):
    for sg in cmds.ls(type='shadingEngine'):
        sgAttr = '{}.aiCustomAOVs'.format(sg)
        nameMapping, nextIndex = getShadingGroupAOVMap(sgAttr)
        for aov in aovs:
            try:
                plug = nameMapping[aov.name]
            except KeyError:
                plug = '{}[{}].aovName'.format(sgAttr, nextIndex)
                cmds.setAttr(plug, aov.name, type="string")

            # skip aliases on referenced nodes
            if cmds.referenceQuery(sg, isNodeReferenced=True):
                continue

            try:
                cmds.aliasAttr('ai_aov_' + aov.name, plug)
            except RuntimeError as err:
                cmds.aliasAttr(sg + '.ai_aov_' + aov.name, remove=True)
                cmds.aliasAttr('ai_aov_' + aov.name, plug)

def refreshAliases():
    aovList = getAOVs()
    removeAliases(aovList)
    addAliases(aovList)

def isValidAOVNode(name):
    maya_version = utils.getMayaVersion()
    if maya_version < 2017:
        return True

    hasRenderSetup = mel.eval('mayaHasRenderSetup()')

    if hasRenderSetup == 0:
        return True

    return not cmds.referenceQuery(name, isNodeReferenced=True)

class SceneAOV(object):
    def __init__(self, node, destAttr):
        self.destAttr = destAttr
        self._node = node
        self._index = None
        self._name = None
        self._type = None

    def __repr__(self):
        return '%s(%r, %d)' % (self.__class__.__name__, self.node, self.index)

    def __eq__(self, other):
        if isinstance(other, basestring):
            return self.name == other
        else:
            return self.name == other.name

    def __lt__(self, other):
        if isinstance(other, basestring):
            if other == "beauty":
                return False
            if self.name == "beauty":
                return True
            else:
                return self.name < other
        else:
            if other.name == "beauty":
                return False
            if self.name == "beauty":
                return True
            else:
                return self.name < other.name

    def __gt__(self, other):
        if isinstance(other, basestring):
            if self.name == "beauty":
                return False
            if other == "beauty":
                return True
            else:
                return self.name > other
        else:
            if self.name == "beauty":
                return False
            if other.name == "beauty":
                return True
            else:
                return self.name > other.name

    @property
    def index(self):
        if self._index is None:
            match = re.search(r'\[(\d)\]', self.destAttr)
            if match:
                self._index = int(match.groups()[0])
            else:
                self._index = 0
        return self._index

    @property
    def name(self):
        '''
        Note that this value is cached on first access and for the sake of speed it
        is not requeried.  To update the instance to reflect the current state of
        the aiAOV node that it wraps, call update()
        '''
        if self._name is None:
            self._name = cmds.getAttr('{}.name'.format(self._node))
        return self._name

    @property
    def type(self):
        '''
        Note that this value is cached on first access and for the sake of speed it
        is not requeried.  To update the instance to reflect the current state of
        the aiAOV node that it wraps, call update()
        '''
        if self._type is None:
            self._type = cmds.getAttr('{}.type'.format(self._node)) # FIXME : should this be returned as a string ?
        return self._type

    @property
    def node(self):
        return self._node

    def rename(self, newName, oldName=None):
        '''
        rename an AOV in the active list.

        provide oldName if the attribute has already been renamed and you just need
        to perform the proper bookkeeping
        '''
        if oldName is None:
            oldName = self.name
            cmds.setAttr('{}.name'.format(self.node), newName, type="string")

        for sg in cmds.ls(type='shadingEngine'):
            try:
                cmds.aliasAttr(sg + '.ai_aov_' + oldName, remove=True)
            except RuntimeError, err:
                pass #print err

            sgAttr = '{}.aiCustomAOVs'.format(sg)
            try:
                cmds.aliasAttr('ai_aov_' + newName, '{}[{}]'.format(sgAttr,self.index))
            except RuntimeError, err:
                pass #print err

    def update(self):
        '''
        update the cached name from the AOV node
        '''
        self._name = cmds.getAttr('{}.name'.format(self._node), type="string")

#------------------------------------------------------------
# scene queries
#------------------------------------------------------------

class AOVInterface(object):
    def __init__(self, node=None):
        self._node = node if node else 'defaultArnoldRenderOptions'
        self._aovAttr = '{}.aovs'.format(self._node)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._node)

    @property
    def node(self):
        if not cmds.objExists(self._node):
            raise TypeError("node doesn't exist")
        return self._node

    def nextAvailableAttr(self):
        nodeAndAttr = self._aovAttr.split('.', 1)
        numElements = melUtils.getAttrNumElements(*nodeAndAttr)
        return '{}[{}]'.format(self._aovAttr, numElements)

    def getAOVs(self, group=False, sort=True, enabled=None, include=None, exclude=None):
        '''
        return a list of SceneAOV classes for all AOVs in the scene
        if group is True, the SceneAOVs are grouped by name: (aovName, [SceneAOV1, SceneAOV2, ...])

        enabled: the enabled state of the AOV. ignored if None (default)
        include: a list of AOV names to include
        exclude: a list of AOV names to exclude
        '''
        _inputs = cmds.listConnections(self._aovAttr, source=True, destination=False, plugs=True, connections=True) or []
        _inputs = dict(zip(_inputs[::2], _inputs[1::2]))
        result = [SceneAOV(fromAttr.split('.')[0], toAttr) for toAttr, fromAttr in _inputs.items() if isValidAOVNode(fromAttr.split('.')[0])]
        if sort:
            result = sorted(result)
        if enabled is not None:
            result = [aov for aov in result if cmds.getAttr('{}.enabled'.format(aov.node)) == enabled]
        if group:
            result = [(aovName, list(aovs)) for aovName, aovs in groupby(result, lambda x: x.name)]
        if include:
            result = [a for a in result if a.name in include]
        if exclude:
            result = [a for a in result if a.name not in exclude]
        return result

    def getAOVNodes(self, names=False):
        '''
        sorted by aovName
        @param names: if True, returns pairs of (aovName, aovNode). if False, returns a list of aovNodes
        '''
        _inputs = cmds.listConnections(self._aovAttr, source=True, destination=False) or []
        if names:
            result = [(cmds.getAttr('{}.name'.format(x)), x) for x in _inputs if isValidAOVNode(x)]
            return sorted(result, key = lambda x: x[0])
        else:
            result = [x for x in _inputs if isValidAOVNode(x)]
            return sorted(result, key = lambda x: cmds.getAttr('{}.name'.format(x)))

    def getAOVNode(self, aovName):
        '''
        given the name of an AOV, return the corresponding aov node

        raises an error if there is more than one match.
        returns None if there are no matches.
        '''
        matches = self.getAOVs(include=[aovName])
        if len(matches) > 1:
            raise ValueError("More than one AOV matches name %r" % aovName)
        elif matches:
            return matches[0].node

    def addAOV(self, aovName, aovType=None, aovShader=None):
        '''
        add an AOV to the active list for this AOV node

        returns the created AOV node
        '''
        if aovType is None:
            aovType = getAOVTypeMap().get(aovName, 'rgba')
        if not isinstance(aovType, int):
            aovType = dict(TYPES)[aovType]
        aovNode = cmds.createNode('aiAOV', name='aiAOV_' + aovName, skipSelect=True)
        out = '{}.outputs[0]'.format(aovNode)

        cmds.connectAttr('defaultArnoldDriver.message', '{}.driver'.format(out))
        filter = defaultFiltersByName.get(aovName, None)
        if filter:
            node = cmds.createNode('aiAOVFilter', skipSelect=True)
            cmds.setAttr('{}.aiTranslator'.format(node), filter, type="string")
            filterAttr = '{}.message'.format(node)
            import mtoa.hooks as hooks
            hooks.setupFilter(filter, aovName)
        else:
            filterAttr = 'defaultArnoldFilter.message'
        cmds.connectAttr(filterAttr, '{}.filter'.format(out))

        cmds.setAttr('{}.name'.format(aovNode), aovName, type="string")
        cmds.setAttr('{}.type'.format(aovNode), aovType)
        nextPlug = self.nextAvailableAttr()
        cmds.connectAttr('{}.message'.format(aovNode), nextPlug)
        aov = SceneAOV(aovNode, nextPlug)
        addAliases([aov])

        if aovShader:
            # this is an AOV shader, we need to do some magic here
            outShader = None

            # first, check amongst active AOVs, to see  if one of them
            # is assigned to a shader of this type. If so, we can reuse it as output shader
            allActiveAOVs = getAOVs()
            for activeAOV in allActiveAOVs:
                conns = cmds.listConnections(activeAOV.node+".defaultValue", d=False, s=True, type=aovShader )
                if conns and len(conns) > 0 and conns[0]:
                    outShader = conns[0]
                    break

            if outShader == None:
                # second, see if shaders of this type already exist in the scene
                existingShaders = cmds.ls(type=aovShader)
                if existingShaders and len(existingShaders) > 0:
                    outShader = existingShaders[len(existingShaders) - 1]
                else:
                    # to finish, let's create a new shader in the scene if none was found
                    aiName = "_aov_"+aovShader
                    outShader = cmds.shadingNode(aovShader, name=aiName, asShader=True)

            # connect the output shader to 'defaultValue'
            cmds.connectAttr(("%s.outColor"%outShader), ("%s.defaultValue"%aovNode))
            cmds.select(outShader)

        return aov

    def removeAOV(self, aov):
        '''
        remove an AOV from the active list for this AOV node

        raises an error if there is more than one match
        returns True if the node was found and removed, False otherwise
        '''
        if isinstance(aov, basestring):
            matches = self.getAOVs(include=[aov])
            if not matches:
                return False
            assert len(matches) == 1
            aov = matches[0]

        self._removeAOVNode(aov.node)
        removeAliases([aov])

    def removeAOVs(self, aovNames):
        '''
        remove AOVs matching names in aovNames from the active list

        returns True if any nodes were removed
        '''
        matches = self.getAOVs(include=aovNames)
        if matches:
            for aov in matches:
                self._removeAOVNode(aov.node)
            removeAliases(matches)
            return True
        return False

    def _removeAOVNode(self, aovNode):
        '''
        Note this does not remove aliases. You must call removeAliases() manually
        '''
        inputs = []
        for nodeType in ['aiAOVDriver', 'aiAOVFilter']:
            inputs += cmds.listConnections(aovNode, source=True, destination=False, type=nodeType) or []
        utils.safeDelete(aovNode)
        for input in inputs:
            # callback may have deleted it
            if cmds.objExists(input) and not cmds.listConnections('{}.message'.format(input), source=False, destination=True):
                print "deleting", input

    def renameAOVs(self, oldName, newName):
        '''
        rename an AOV in the active list
        '''
        matches = self.getAOVs(include=[oldName])
        if matches:
            for aov in matches:
                cmds.setAttr('{}.name'.format(aov.node), newName, type="string")
                
            # we can only use one
            matches[0].rename(newName, oldName)
        else:
            raise NameError('Scene does not contain any AOVs with name %r' % oldName)

def getAOVs(group=False, sort=True, enabled=None, include=None, exclude=None):
    try:
        return AOVInterface().getAOVs(group, sort, enabled, include, exclude)
    except:
        return []

def getAOVNodes(names=False):
    try:
        return AOVInterface().getAOVNodes(names)
    except:
        return []

#------------------------------------------------------------
# global queries
#------------------------------------------------------------

def getRegisteredAOVs(builtin=False, nodeType=None):
    '''
    returns a list of all registered aov names.

    @param builtin: set to True to include built-in AOVs
    @param nodeType: a node name or list of node names to restrict result to AOVs for only those nodes
    '''
    if nodeType:
        if isinstance(nodeType, (list, tuple)):
            result = [x[0] for x in getNodeGlobalAOVData(nt) for nt in nodeType]
        else:
            result = [x[0] for x in getNodeGlobalAOVData(nodeType)]
    else:
        result = cmds.arnoldPlugins(listAOVs=True)
    if builtin:
        result = getBuiltinAOVs() + result
    return result

def getBuiltinAOVs():
    return [x[0] for x in BUILTIN_AOVS]

def getLightingAOVs():
    return LIGHTING_AOVS

def getNodeGlobalAOVData(nodeType):
    "returns a list of registered (name, attribute, data type) pairs for the given node type"
    # convert to a 2d array
    result = [GlobalAOVData(*x) for x in utils.groupn(cmds.arnoldPlugins(listAOVs=True, nodeType=nodeType), 3)]
    return sorted(result, key=lambda x: x.name)

def getNodeTypesWithAOVs():
    return sorted(cmds.arnoldPlugins(listAOVNodeTypes=True))

def getAOVShaders():
    return sorted(cmds.arnoldPlugins(listAOVShaders=True))

_aovTypeMap = None
def getAOVTypeMap():
    "return a dictionary of AOV name to AOV type"
    # TODO: update this cached result when new nodes are added
    global _aovTypeMap
    if _aovTypeMap is None:
        _aovTypeMap = {}
        for nodeType in getNodeTypesWithAOVs():
            for aovName, attr, type in getNodeGlobalAOVData(nodeType):
                _aovTypeMap[aovName] = type
        _aovTypeMap.update(dict(BUILTIN_AOVS))
    return _aovTypeMap

#- groups

def getAOVGroups():
    return ['<builtin>']

def getGroupAOVs(groupName):
    if groupName == '<builtin>':
        return getBuiltinAOVs()
    raise


#------------------------------------------------------------
# callbacks
#------------------------------------------------------------
_aovOptionsChangedCallbacks = callbacks.DeferredCallbackQueue()
# a public function for adding AOV callbacks
def addAOVChangedCallback(func, key=None):
    _aovOptionsChangedCallbacks.addCallback(func, key)

def removeAOVChangedCallback(key):
    _aovOptionsChangedCallbacks.removeCallback(key)

def createAliases(sg):
    # This will run on scene startup but the list of AOVs will be unknown
    sg = str(sg)
    if sg == '' or not cmds.objExists(sg):
        return
    if sg == "swatchShadingGroup":
        return
    
    if cmds.attributeQuery('attributeAliasList', node=sg, exists=True):
        alias_list = '{}.attributeAliasList'.format(sg)
        if cmds.objExists(alias_list) and not cmds.aliasAttr(sg, q=True) :
            print "Shading Group %s with bad Attribute Alias list detected. Fixing!" % sg
            cmds.deleteAttr(alias_list)

    aovList = getAOVNodes(True)
    sgPlug = "{}.aiCustomAOVs".format(sg)

    sgLogIdx = cmds.getAttr(sgPlug, mi=True) or []
    s = set([cmds.getAttr("{}[{}].aovName".format(sgPlug, i)) for i in sgLogIdx])
    free = listAvailableIndices(sgLogIdx, len(aovList))
    n = 0
    for aov in aovList:
        if aov[0] not in s:
            cmds.setAttr("{}[{}].aovName".format(sgPlug, free[n]), aov[0], typ="string")
            n += 1

    if cmds.referenceQuery(sg, isNodeReferenced=True):
        return

    sgAttr = '{}.aiCustomAOVs'.format(sg)
    attrValues = cmds.getAttr(sgAttr, mi=True) or []
    for i in attrValues:
        at = '{}[{}]'.format(sgAttr, i)
        name = cmds.getAttr('{}.aovName'.format(at))
        try:
            cmds.aliasAttr('ai_aov_' + name, at)
        except RuntimeError as err:
            cmds.aliasAttr(sg + '.ai_aov_' + name, remove=True)
            cmds.aliasAttr('ai_aov_' + name, at)


def installCallbacks():
    _sgAliasesCallbacks = callbacks.SceneLoadCallbackQueue()
    _sgAliasesCallbacks.addCallback(createAliases, passArgs=True)
    callbacks.addNodeAddedCallback(_sgAliasesCallbacks, 'shadingEngine',
                                   applyToExisting=True, apiArgs=False)

    if not cmds.about(batch=True):
        callbacks.addAttributeChangedCallback(_aovOptionsChangedCallbacks, 'aiOptions', 'aovList',
                                  context=om.MNodeMessage.kConnectionMade | om.MNodeMessage.kConnectionBroken,
                                  applyToExisting=True)
    #callbacks.addAttributeChangedCallback(_aovOptionsChangedCallbacks.entryCallback, 'aiAOV', None, applyToExisting=True)

