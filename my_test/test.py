
add_new_attribute

from maya import OpenMaya

mselection = OpenMaya.MSelectionList()
mselection.add('pSphere1')
mobject = OpenMaya.MObject()
mselection.getDependNode(0, mobject)        

type_attr = OpenMaya.MFnTypedAttribute()
aSampleTxt = OpenMaya.MObject()
aSampleTxt = type_attr.create('crowd_tag', 'crdt', OpenMaya.MFnData.kString)
type_attr.setKeyable( True )
type_attr.setWritable( True )
type_attr.setReadable( True )
type_attr.setStorable( True )

m_node_fn = OpenMaya.MFnDependencyNode()  
m_node_fn.setObject( mobject )
m_node_fn.addAttribute(aSampleTxt)


##############################################

compound = OpenMaya.MFnCompoundAttribute()
node.target = compound.create("target", "t")

xv = OpenMaya.MFnUnitAttribute()
node.inTargetX = xv.create("targetTranslateX", "ttx", OpenMaya.MFnUnitAttribute.kDistance)
xv.setStorable(1)
xv.setWritable(1)
compound.addChild(node.inTargetX)

yv = OpenMaya.MFnUnitAttribute()
node.inTargetY = xv.create("targetTranslateY", "tty", OpenMaya.MFnUnitAttribute.kDistance)
yv.setConnectable(1)
yv.setStorable(1)
yv.setWritable(1)
compound.addChild(node.inTargetY)

zv = OpenMaya.MFnUnitAttribute()
node.inTargetZ =  xv.create("targetTranslateZ", "ttz", OpenMaya.MFnUnitAttribute.kDistance)
zv.setConnectable(1)
zv.setStorable(1)
zv.setWritable(1)
compound.addChild(node.inTargetZ)

# add to the node
node.addAttribute(node.target)


###########################################################
eAttr = OpenMaya.MFnEnumAttribute()     
testNode.optionMenu= eAttr.create('options', 'options', 0)

eAttr.addField('option1', 0)
eAttr.addField('option2', 1)
eAttr.addField('option3', 2)
eAttr.addField('option4', 3)
eAttr.addField('option5', 4)

eAttr.setKeyable(1)
eAttr.setStorable(1)

testNode.addAttribute(testNode.optionMenu)

eAttr = OpenMaya.MFnEnumAttribute()
 
testNode.optionMenu= eAttr.create('options', 'options', 0)
eAttr.addField('option1', 0)
eAttr.addField('option2', 1)
eAttr.addField('option3', 2)
eAttr.addField('option4', 3)
eAttr.addField('option5', 4)
eAttr.setKeyable(1)
eAttr.setStorable(1)
testNode.addAttribute(testNode.optionMenu)


optionMenu_value = dataBlock.inputValue(testNode.optionMenu)
    
if optionMenu_value.asInt() == 0:
    runThisCode()
if optionMenu_value.asInt() == 1:
    runThisCode()
if optionMenu_value.asInt() == 2:
    runThisCode()
    
    
####################################################################
import maya.OpenMaya as OpenMaya        # general Maya API module

def addExtraAttrToNode( m_node_name ):
    """
    add custom extra attributes to the node using Maya API
    classes in runtime mode 'on fly'
    INPUT:  m_node_name - node name, like 'lambert1' 
    RETURN: True -  if attributes added properly, False - otherwise
    USAGE:  addExtraAttrToNode('lambert1')    
    """
    # create selection list
    #
    m_selectionList = OpenMaya.MSelectionList() 
    # create MObject
    #
    m_node = OpenMaya.MObject()
    # create a function set to work with MObject
    #                 
    m_node_fn = OpenMaya.MFnDependencyNode()    
    try:
        # add node with name 'lambert2'
        # if node don't exist return exception 
        m_selectionList.add( m_node_name )            
    except:
        return False
    # get first element in the selection list and connect with MObject 
    #
    m_selectionList.getDependNode( 0, m_node )  
    # connect MObject with function set
    # 
    m_node_fn.setObject( m_node )
    #            
    # float attribute
    # 
    fAttr = OpenMaya.MFnNumericAttribute()
    aSampleFloat  = OpenMaya.MObject()
    aSampleFloat = fAttr.create( "sampleFloat", "sf", 
                                 OpenMaya.MFnNumericData.kFloat, 0.0 )
    fAttr.setKeyable( True )
    fAttr.setStorable( True )
    fAttr.setDefault( 1.0 )
    #            
    # string attribute
    # 
    fAttr = OpenMaya.MFnTypedAttribute()
    aSampleTxt = OpenMaya.MObject()
    aSampleTxt = fAttr.create( "sampleTXT", "st", 
                               OpenMaya.MFnData.kString )
    fAttr.setKeyable( True )
    fAttr.setWritable( True )
    fAttr.setReadable( True )
    fAttr.setStorable( True )
    #            
    # boolean attribute
    # 
    fAttr = OpenMaya.MFnNumericAttribute()
    aSampleBool = OpenMaya.MObject()
    aSampleBool = fAttr.create( "sampleBOOL", "sb", 
                                OpenMaya.MFnNumericData.kBoolean, True )
    fAttr.setKeyable( True )
    fAttr.setStorable( True )
    fAttr.setReadable( True )
    fAttr.setWritable( True )
    #            
    # multi compound attribute
    # 
    fAttr = OpenMaya.MFnCompoundAttribute()
    aCompound = OpenMaya.MObject()
    aCompound = fAttr.create( "sampleCompound", "sc" )
    fAttr.addChild( aSampleBool )  # child 0
    fAttr.addChild( aSampleTxt )   # child 1
    fAttr.addChild( aSampleFloat ) # child 2
    fAttr.setArray( True ) # create 'multi' attr
    fAttr.setKeyable( True )
    fAttr.setWritable( True )
    fAttr.setReadable( True )
    fAttr.setStorable( True )
    try:
        # try to add attributes using function set
        m_node_fn.addAttribute( aCompound )
    except:
        return False
    return True

def printExtraAttrData( m_node_name ):
    """
    print's data stored in extra attributes 
    INPUT:  m_node_name - node name, like 'lambert1' 
    RETURN: True -  if well done, False - otherwise
    USAGE:  printExtraAttrData('lambert1')         
    """
    m_selectionList = OpenMaya.MSelectionList() # create selection list
    m_node = OpenMaya.MObject()                 # create MObject
    m_node_fn = OpenMaya.MFnDependencyNode()    # create a function set
    try:
        # add node with name 'lambert2'
        m_selectionList.add( m_node_name )            
    except:
        return False
    # get first element in the selection list and connect with MObject 
    m_selectionList.getDependNode( 0, m_node )  
    # connect MObject with function set 
    m_node_fn.setObject( m_node )
    # find attribute by name using function set class 
    #
    m_attr = m_node_fn.attribute('sampleCompound')
    # create MPlug object fo work with attribute
    # A plug is a point on a dependency node where a 
    # particular attribute can be connected
    m_attr_plug = OpenMaya.MPlug( m_node, m_attr )
    # create int array fo storing indexes of available items
    #
    m_ind = OpenMaya.MIntArray()
    m_attr_plug.getExistingArrayAttributeIndices(m_ind)
    try:
        for i in m_ind:
            print("IND %s BOOL %s STR %s FLOAT %s" 
                %( i,
                   m_attr_plug.elementByLogicalIndex(i).child(0).asBool(),
                   m_attr_plug.elementByLogicalIndex(i).child(1).asString(),
                   m_attr_plug.elementByLogicalIndex(i).child(2).asFloat() ) )
    except:
        return False
    return True 
    
def setExtraAttrValues( m_node_name, m_index, m_tuple ):
    """
    write data to the node 
    INPUT:  m_node_name - node name, like 'lambert1'
            m_index     - index of item where you wont to write
            m_tuple     - tuple, like: ( True , 'Test', 4.2 ) 
                          m_tuple[0] - True
                          m_tuple[1] - 'Test'
                          m_tuple[2] - 4.2                                                  
    RETURN: True -  if well done, False - otherwise
    USAGE:  setExtraAttrValues( 'lambert1', 1, ( False , 'Test', 4.2 )  )       
    """ 
    m_selectionList = OpenMaya.MSelectionList() 
    m_node = OpenMaya.MObject()                 
    m_node_fn = OpenMaya.MFnDependencyNode()    
    try:
        m_selectionList.add( m_node_name )            
        m_selectionList.getDependNode( 0, m_node )  
        m_node_fn.setObject( m_node )
        m_attr = m_node_fn.attribute('sampleCompound')
        m_attr_plug = OpenMaya.MPlug( m_node, m_attr )
        # convert m_index to integer
        #
        m_index = int(m_index)
        # write data stored in tuple to the node
        #
        m_attr_plug.elementByLogicalIndex(m_index).child(0).setBool( m_tuple[0] )
        m_attr_plug.elementByLogicalIndex(m_index).child(1).setString( m_tuple[1] )
        m_attr_plug.elementByLogicalIndex(m_index).child(2).setFloat( m_tuple[2] )         
    except:
        return False
    return True 


####################################################
# ==================== AttributeAccess.py ====================
import maya.cmds as cmds
import maya.mel as mel
import sys
import maya.OpenMaya as OM        # Version 1
import math

import inspect
import types

# ---------- Common Stuff ----------

# "something" can be any Python object.
def Exists(something):
    return something is not None

def printElements(ob):
    print '----- Elements: -----'
    i = 0
    for x in ob:
        print ' [' + str(i) + ']:  ' + repr(x)
        i += 1
    print '---------------------'

def printDictElements(ob):
    print ''
    print '-----------------------'
    for x in ob: print repr(x) + ':  ' + repr(ob[x])
    print '-----------------------'


# ---------- inspect Attributes ----------

# NOTE: ob is an instance, NOT a type object.
def TypeName(ob):
    return ob.__class__ .__name__

# Excludes 'internal' names (start with '__').
def Public(name):
    return not name.startswith('__')

# member is element of inspect.getmembers:
#   a two-element tuple.
def MemberWithType(member):
    return ( member[0], TypeName(member[1]), member[1] )
#print MemberWithType( (1.1, 2) )

def Members(ob):
    return inspect.getmembers(ob)

# True for Maya Python's 'this' member.
# member [1] is attribute value.
def SwigThis(member):
    return (member[0] == 'this') and (TypeName(member[1]) == 'SwigPyObject')

# HACK: "not SwigThis": omit Maya Python's 'this' member.
def PublicMembers(ob):
    members = filter(lambda member: Public(member[0]) and not SwigThis(member), Members(ob))
    return map(MemberWithType, members)

# Excludes 'internal' names (start with '__').
def Dir(ob):
    return filter(Public, dir(ob))


def _Type_And_Features(ob, names):
    return '{0}.({1})'.format(TypeName(ob), ', '.join(names))

def MemberName(member):
    return member[0]

# member with typename inserted as [1]. So descriptor is [2].
# member type-name is [1].
def CallableMember(member):
    #return (member[2].__class__  is types.MethodType)
    return inspect.isroutine(member[2])

def MemberNames(members):
    return map(MemberName, members)

def Features(ob):
    return _Type_And_Features(ob, MemberNames(PublicMembers(ob)) )   
    #return _Type_And_Features(ob, Dir(ob))

def Callable(ob):
    return _Type_And_Features(ob, MemberNames(filter(lambda a: CallableMember(a), PublicMembers(ob))))
    #return _Type_And_Features(ob, filter(lambda a: callable(a), Dir(ob)))

def IsClassVar(self, attrName):
    return hasattr(self.__class__, attrName)

# REQUIRE attrName already known to be supported by self.
# But just in case, return False if exception, so will be skipped.
def IsNotSameAsClassVar(self, attrName):
    try:
        if not IsClassVar(self, attrName):
            return True
        # If it has different value than class' attribute, it is on the instance.
        return getattr(self, attrName) is not getattr(self.__class__, attrName)
    except:
        return False

# ---------- _MayaValues ----------

# NOTE: 'ob' is an instance, not the class (type) itself.
def _ClassVars(ob):
    attributes = filter(lambda a: not CallableMember(a), PublicMembers(ob))
    # Keep class variables.
    # "not IsProperty": HACK: Skip Maya/Swig 'property' class variables.
    classVars = filter(lambda desc: IsClassVar(ob, desc[0]) and not IsProperty(getattr(ob.__class__, desc[0])), attributes)
    return MemberNames(classVars)

# NOTE: 'ob' is an instance, not the class (type) itself.
def ClassVars(ob):
    return _Header_And_Values(TypeName(ob) + ' Class_Variables',
        map(lambda attr: attr + ': ' + Repr(getattr(ob, attr)), _ClassVars(ob)),
        0
        )


# If it is invocable without parameters, return (attrName, typename, result of invocation).
# if Not reportExceptions, return None for Exception.
def CallAttribute_AsTriple(self, attrName, reportExceptions=False):
    try:
        expressionString = 'self.{0}()'.format(attrName)
        result = eval(expressionString)
        typename = TypeName(result)
    except Exception as e:
        if reportExceptions:
            result = e
            typename = '*** Exception'
        else:
            return None
    return (attrName, typename, result)

# member is tuple (attrName, typeName, value)
# If it is invocable without parameters, return (attrName, typename, result of invocation).
# if Not reportExceptions, return None for Exception.
def CallMember_AsTriple(self, member, reportExceptions=False):
    return CallAttribute_AsTriple(self, member[0], reportExceptions)

# If it is invocable without parameters, return string: pretty-printed result of invocation.
# if Not reportExceptions, return None for Exception.
def CallAttribute(self, attrName, reportExceptions=False):
    try:
        #printElements(locals())
        expressionString = 'self.{0}()'.format(attrName)
        #print Eval(expressionString, locals())
        result = eval(expressionString)
        resultString = Repr(result)
        typename = TypeName(result)
    except Exception as e:
        if reportExceptions:
            #result = '*** Exception  ' + str(e)
            result = e
            resultString = str(e)
            typename = '*** Exception'
        else:
            return None
    return ' .{0} {{{1}}}= {2}'.format(attrName, typename, resultString)

# member is tuple (attrName, typeName, value)
# If it is invocable without parameters, return string: pretty-printed result of invocation.
# if Not reportExceptions, return None for Exception.
def CallMemberRepr(self, member, reportExceptions=False):
    return CallAttribute(self, member[0], reportExceptions)

def FirstLine(string):
    lines = string.split('\n')
    if len(lines) > 1:
        return lines[0] + '...'
    return string

def ArgLessRoutines_AsTriples(ob):
    members = PublicMembers(ob)
    members_WithNones = map(lambda member: CallMember_AsTriple(ob, member), members)
    # member is tuple (attrName, typeName, value)
    members = filter(Exists, members_WithNones)
    return members

def ArgLessRoutines(ob):
    members = PublicMembers(ob)
    members_WithNones = map(lambda member: CallMember_AsTriple(ob, member), members)
    # member is tuple (attrName, typeName, value)
    members = filter(Exists, members_WithNones)
    resultStrings = map(lambda string: FirstLine(string), resultStrings)
    return _Header_And_Values(TypeName(ob) + ' ArgLessRoutines', resultStrings)

def _MayaCallables_Common(mayaType):
    try:
        typeName = mayaType.__name__
        if typeName == 'MDagPath':
            return ['fullPathName']
        if typeName == 'MTypeId':
            return ['id']
        if typeName == 'MFnMesh':
            return ['numPolygons', 'numVertices', 'numEdges', 'numFaceVertices']
        if typeName == 'MDagPath':
            return ['fullPathName']
    except Exception as e:
        print e
    return []

def _MayaCallables_Version1(mayaType):
    return _MayaCallables_Common(mayaType)

def _MayaCallables_Version2(mayaType):
    return _MayaCallables_Common(mayaType)

# Names of callable attributes to include in Repr of 'ob'.
# For instances of types in 'maya.OpenMaya'.
def MayaCallables(ob):
    try:
        typ = ob.__class__
        if typ == type:
            return []
        if typ.__module__ == 'maya.OpenMaya':
            return _MayaCallables_Version1(typ)
        if typ.__module__ == 'OpenMaya':
            return _MayaCallables_Version2(typ)
    except Exception as e:
        print e
    return []

# Return (name, typename, value) per maya callable.
def _MayaValues(ob):
    callables = MayaCallables(ob)
    members_WithNones = map(lambda attrName: CallAttribute_AsTriple(ob, attrName), callables)
    members = filter(Exists, members_WithNones)
    return members

# TODO: If all results fit on single line, remove "{typename}" so is more readable.
#def MayaValues(ob):
#    resultStrings = _MayaValues(ob)
#    return _Header_And_Values(TypeName(ob) + ' MayaValues', resultStrings)

# ---------- Attributes ----------
def _AttributeNames(ob):
    attributes = filter(lambda a: not CallableMember(a), PublicMembers(ob))
    # Omit class variables.
    attributes = filter(lambda desc: IsNotSameAsClassVar(ob, desc[0]), attributes)
    return MemberNames(attributes)

def AttributeNames(ob):
    return _Type_And_Features(ob, _AttributeNames(ob))
    #return _Type_And_Features(ob, filter(lambda a: not callable(a), Dir(ob)))

def _Header_And_Values(headerString, valueStrings, maxWidth=100):
    if sum(map(len, valueStrings)) > maxWidth:
        # pretty print, with one value per line.
        return '{0}(\n  {1}\n)'.format(headerString, '\n  '.join(valueStrings))
    return '{0}({1})'.format(headerString, ', '.join(valueStrings))

def _Type_And_Values(ob, valueStrings, maxWidth=100):
    return _Header_And_Values(TypeName(ob), valueStrings, maxWidth)

def AttributeValues(ob):
    return _Type_And_Values(ob, map(lambda attr: str(getattr(ob, attr)), _AttributeNames(ob)))

def Attributes(ob, depth=0):
    # Limit recursion.
    # If deep, don't include MayaValues.
    if depth >= 2:
        return _Type_And_Values(ob, map(lambda attr: attr + ': ' + str(getattr(ob, attr)), _AttributeNames(ob)))
    attributes = map(lambda attr: attr + ': ' + Repr(getattr(ob, attr), depth + 1), _AttributeNames(ob))
    if depth == 0:
        mayaValues = _MayaValues(ob)
        if len(mayaValues) > 0:
            for mayaValue in mayaValues:
                attribute = mayaValue[0] + ': ' + Repr(mayaValue[2])
                attributes.append(attribute)
    return _Type_And_Values(ob, attributes)

def IsProperty(ob):
    return (TypeName(ob) == 'property')

# ---------- Repr ----------
def Repr(ob, depth=0):
    r = repr(ob)
    # Helps avoid undesired recursion.
    if ob.__class__ == type:
        return r
    if (r.__class__ == types.StringType) and (len(r) > 0) and (r.find('<') <> 0):
        # Has a good repr.
        return r
    # Doesn't have a good repr; inspect it instead.
    return '#' + Attributes(ob, depth)

def Eval(expressionString, _locals=locals(), _globals=globals()):
    return str(expressionString) + "= " + str(Repr(eval(expressionString, _globals, _locals)))


# ---------- Testing ----------

# ---------- class Vector ----------
class Vector(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = x, y, z
    # Provide useful info for 'repr(self)', 'str(self)', and 'print self'.
    def __repr__(self):
        return 'Vector({0}, {1}, {2})'.format(self.x, self.y, self.z)
    # math operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    # ==
    def __eq__(self, other):
        return (self.__class__ == other.__class__) and \
            (self.x == other.x) and \
            (self.y == other.y) and \
            (self.z == other.z)
    # a simple method
    def ApproximateLength(self):
        return self.x + self.y + self.z
    # list/sequence/iterator support.
    def tolist(self):
        return [self.x, self.y, self.z]
    def __len__(self):
        return 3
        # No need for "next(self)", because we create a list, use its iterator.
    def __iter__(self):
        return iter(self.tolist())
# class variable
Vector.Zero = Vector()

# ---------- inspecting Vector ----------
def Testing_Vector_Attributes():
    #vec = (1, 2, 3)
    #vec = [1, 2, 3]
    #vec = Vector(1.0, 2.0, 3.0)
    vec = OM.MFloatVector(1, 2, 3)
    print vec
    #for x in vec: print x
    print dir(vec)
    print TypeName(vec)
    print Dir(vec)
    print Features(vec)
    print Callable(vec)
    print '-----------------------'
    printElements(PublicMembers(vec))
    print '-----------------------'
    print AttributeNames(vec)
    #print vec.x
    #print eval('vec.x')
    #print getattr(vec, 'x')
    print AttributeValues(vec)
    print Attributes(vec)
    vec = OM.MFloatVector(1, 2, 3)
    #print repr(vec)
    #print Repr('Hi')
    print Repr( (1,2,3) )
    print Repr(vec)
    print ClassVars( Vector(1.0, 2.0, 3.0) )
    print ClassVars( OM.MFloatVector(1, 2, 3) )
    print Eval('OM.MMatrix()')
    print Eval('OM.MMatrix().matrix')

if __name__ == "__main__":
    Testing_Vector_Attributes()
    
    
#########################################
#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Jul 10 15:40:53 2018
#========================================
import os, re, json
import maya.cmds as mc
import maya.OpenMaya as OpenMaya
from . import shaderUtil
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def get_all_shading_nodes():
    '''
    get scene all shadingEngine nodes.
    '''
    iterator = OpenMaya.MItDependencyNodes(OpenMaya.MFn.kShadingEngine)
    while not iterator.isDone():
        yield iterator.item()
        iterator.next()





def get_sel_shading_nodes():
    '''
    get shadingEngine nodes by selected geometrys.
    '''
    #- get selected geometry
    mc.select(hi=True)
    geo_selection = OpenMaya.MSelectionList()
    OpenMaya.MGlobal.getActiveSelectionList(geo_selection)

    #-
    geo_iterator = OpenMaya.MItSelectionList(geo_selection)
    geo_mobject  = OpenMaya.MObject()
    while not geo_iterator.isDone():
        geo_iterator.getDependNode(geo_mobject)

        sg_iterator = OpenMaya.MItDependencyGraph(geo_mobject, OpenMaya.MFn.kShadingEngine, OpenMaya.MItDependencyGraph.kDownstream)
        while not sg_iterator.isDone():
            yield sg_iterator.currentItem()
            sg_iterator.next()

        geo_iterator.next()





def export_shading_nodes(sg_nodes, sg_file_path):
    '''
    '''
    selection = OpenMaya.MSelectionList()
    for sg in sg_nodes:
        if not OpenMaya.MFnDependencyNode(sg).isDefaultNode():
            selection.add(sg)

    if selection.isEmpty():
        return False

    OpenMaya.MGlobal.setActiveSelectionList(selection)
    OpenMaya.MFileIO.exportSelected(sg_file_path, None, True)

    return True





def export_all_shading_nodes(sg_file_path):
    '''
    '''
    return export_shading_nodes(get_all_shading_nodes(), sg_file_path)





def export_sel_shading_nodes(sg_file_path):
    '''
    '''
    return export_shading_nodes(get_sel_shading_nodes(), sg_file_path)





def get_shading_members(sg_node):
    '''
    '''
    sg_api_mfn = OpenMaya.MFnSet(sg_node)
    geo_selection = OpenMaya.MSelectionList()
    if not sg_api_mfn.isDefaultNode():
        sg_api_mfn.getMembers(geo_selection, False)

    return geo_selection





def get_select_strings(selection, cut_shape=True):
    '''
    '''
    iterator = OpenMaya.MItSelectionList(selection)

    members = list()
    strings = list()
    dagpath = OpenMaya.MDagPath()
    while not iterator.isDone():
        iterator.getStrings(strings)
        iterator.getDagPath(dagpath)

        if cut_shape:
            geo = dagpath.fullPathName().rsplit('|', 1)[0]
        else:
            geo = dagpath.fullPathName().rsplit('.', 1)[0]

        for x in strings:
            if x.count('.') == 0:
                members.append(geo)
            else:
                members.append('{0}.{1}'.format(geo, x.split('.')[-1]))

        iterator.next()

    return members





def export_shading_data(sg_nodes, data_file_path):
    '''
    '''
    data = dict()
    for sg in sg_nodes:
        sg_name    = OpenMaya.MFnDependencyNode(sg).name()
        sg_members = get_select_strings(get_shading_members(sg))
        if sg_members:
            sg_members.sort()
            data[sg_name] = sg_members

    with open(data_file_path, 'w') as f:
        json.dump(data, f, indent=4)

    return True





def export_all_shading_data(data_file_path):
    '''
    '''
    sg_nodes = get_all_shading_nodes()
    return export_shading_data(sg_nodes, data_file_path)





def export_sel_shading_data(data_file_path):
    '''
    '''
    sg_nodes = get_sel_shading_nodes()
    return export_shading_data(sg_nodes, data_file_path)





def import_shading_data(data_file_path):
    '''
    '''
    if not os.path.isfile(data_file_path):
        return dict()

    with open(data_file_path, 'r') as f:
        data = json.load(f)
        return data





def refrence_shader(shader_file_path):
    '''
    '''
    if not os.path.isfile(shader_file_path):
        return

    if shader_file_path in mc.file(q=True, r=True):
        namespace = mc.file(shader_file_path, q=True, ns=True)

    else:
        selection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(selection)

        basename = os.path.splitext(os.path.basename(shader_file_path))[0]
        OpenMaya.MFileIO.reference(shader_file_path, False, False, basename)
        namespace = mc.file(shader_file_path, q=True, ns=True)

        OpenMaya.MGlobal.setActiveSelectionList(selection)

    return namespace





def set_shading_members(data_file_path, shader_ns=None, geo_ns=None, by_sel=False):
    '''
    '''
    data = import_shading_data(data_file_path)

    if by_sel:
        sel_list = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(sel_list)

    shaderUtil.startProgress(len(data))
    for sg, geo_data in data.iteritems():
        #- shader sg
        if shader_ns:
            sg = '{0}:{1}'.format(shader_ns, sg) #- shader_SG -> material:shader_SG

        if not mc.objExists(sg):
            continue

        #- geometry
        shaderUtil.moveProgress('Set shading members for - {0}'.format(sg))

        geo_selection = OpenMaya.MSelectionList()
        for geo in geo_data:
            if geo_ns:
                geo = geo.replace('|', '|{0}:'.format(geo_ns))

            for i in range(5):
                try:
                    geo_selection.add('{0}*{1}'.format('*:'*i, geo))
                    break
                except:
                    pass

        if by_sel:
            geo_selection.intersect(sel_list)

        if not geo_selection.isEmpty():
            mc.sets(get_select_strings(geo_selection, cut_shape=False), e=True, forceElement=sg)
        else:
            print 'No memebers for - {0}'.format(sg)


    shaderUtil.endProgress()

    return True




def set_arnold_attribute(attr_file_path, geo_ns=None, by_sel=False):
    '''
    '''
    if not os.path.isfile(attr_file_path):
        return

    #- set arnold attribute data
    attr_data = dict()
    with open(attr_file_path, 'r') as f:
        attr_data = json.load(f)

    for geo, attrbutes in attr_data.iteritems():
        if geo_ns:
            geo = geo.replace('|', '|{0}:'.format(geo_ns))
        if not mc.objExists(geo):
            continue

        for attr, value in attrbutes.iteritems():
            shapes = mc.listRelatives(geo, s=True, path=True)
            if shapes:
                if re.match('mtoa_', attr) and not mc.attributeQuery(attr, n=shapes[0], ex=True):
                    mc.addAttr(shapes[0], ln=attr[:-1], at="double3")
                    mc.addAttr(shapes[0], ln=attr[:-1]+'X', at="double", p=attr[:-1])
                    mc.addAttr(shapes[0], ln=attr[:-1]+'Y', at="double", p=attr[:-1])
                    mc.addAttr(shapes[0], ln=attr[:-1]+'Z', at="double", p=attr[:-1])

            if isinstance(value, basestring):
                try:
                    mc.setAttr('{0}.{1}'.format(geo, attr), value, typ='string')
                except:
                    pass
            else:
                try:
                    mc.setAttr('{0}.{1}'.format(geo, attr), value)
                except:
                    pass
                
                
#########################################################

import maya.cmds as cmds
import maya.mel as mm

animated = []
static = []        
      
# Find animated Plugs
OpenMayaAnim.MAnimUtil.findAnimatedPlugs ( dagPath, plugs )

# Get animated attributes into a list
for i in range (0, plugs.length()):
      animated.append( plugs[i].partialName(False, False, False, False, False, True) )

# list keyable Attributes
fullPath = dagPath.fullPathName()
keyable = cmds.listAttr( fullPath, k=True )

# get the keyable not animated attributes
for i in range (0, len (keyable)):
      match = False
      for j in range (0, len (animated)):
          if  animated[j] == keyable[i]: 
              match = True
      if match == False:
          static.append( keyable[i] )

# try to use MEL to get the same, but not this way...
unkeyed = mm.stringArrayRemove( animated, keyable )

############################################


static const char kDefaultString[] = "Default String";

MStatus myCommand::AddAttribute( MObject & node )
{
  MStatus                               status;

  MDGModifier                           dgModifier;
  MFnTypedAttribute                     tAttr;

  aStringWithDefault = tAttr.create( "string", "str", MFnData::kString, MObject::kNullObj );
  fnTypedAttr.setStorable(true);
  fnTypedAttr.setKeyable(false);

  status = dgModifier.addAttribute( node, aStringWithDefault );
  status = dgModifier.doIt();

  // The default for the string attribute does not "stick" after a
  // save and reload; explicitly set it via its MPlug.
  MPlug plug( node, aStringWithDefault );
  plug.setValue( kDefaultString );

  return status;
}

######################################################


import maya.OpenMaya as OpenMaya        # general Maya API module

def addExtraAttrToNode( m_node_name ):
    """
    add custom extra attributes to the node using Maya API
    classes in runtime mode 'on fly'
    INPUT:  m_node_name - node name, like 'lambert1' 
    RETURN: True -  if attributes added properly, False - otherwise
    USAGE:  addExtraAttrToNode('lambert1')    
    """
    # create selection list
    #
    m_selectionList = OpenMaya.MSelectionList() 
    # create MObject
    #
    m_node = OpenMaya.MObject()
    # create a function set to work with MObject
    #                 
    m_node_fn = OpenMaya.MFnDependencyNode()    
    try:
        # add node with name 'lambert2'
        # if node don't exist return exception 
        m_selectionList.add( m_node_name )            
    except:
        return False
    # get first element in the selection list and connect with MObject 
    #
    m_selectionList.getDependNode( 0, m_node )  
    # connect MObject with function set
    # 
    m_node_fn.setObject( m_node )
    #            
    # float attribute
    # 
    fAttr = OpenMaya.MFnNumericAttribute()
    aSampleFloat  = OpenMaya.MObject()
    aSampleFloat = fAttr.create( "sampleFloat", "sf", 
                                 OpenMaya.MFnNumericData.kFloat, 0.0 )
    fAttr.setKeyable( True )
    fAttr.setStorable( True )
    fAttr.setDefault( 1.0 )
    #            
    # string attribute
    # 
    fAttr = OpenMaya.MFnTypedAttribute()
    aSampleTxt = OpenMaya.MObject()
    aSampleTxt = fAttr.create( "sampleTXT", "st", 
                               OpenMaya.MFnData.kString )
    fAttr.setKeyable( True )
    fAttr.setWritable( True )
    fAttr.setReadable( True )
    fAttr.setStorable( True )
    #            
    # boolean attribute
    # 
    fAttr = OpenMaya.MFnNumericAttribute()
    aSampleBool = OpenMaya.MObject()
    aSampleBool = fAttr.create( "sampleBOOL", "sb", 
                                OpenMaya.MFnNumericData.kBoolean, True )
    fAttr.setKeyable( True )
    fAttr.setStorable( True )
    fAttr.setReadable( True )
    fAttr.setWritable( True )
    #            
    # multi compound attribute
    # 
    fAttr = OpenMaya.MFnCompoundAttribute()
    aCompound = OpenMaya.MObject()
    aCompound = fAttr.create( "sampleCompound", "sc" )
    fAttr.addChild( aSampleBool )  # child 0
    fAttr.addChild( aSampleTxt )   # child 1
    fAttr.addChild( aSampleFloat ) # child 2
    fAttr.setArray( True ) # create 'multi' attr
    fAttr.setKeyable( True )
    fAttr.setWritable( True )
    fAttr.setReadable( True )
    fAttr.setStorable( True )
    try:
        # try to add attributes using function set
        m_node_fn.addAttribute( aCompound )
    except:
        return False
    return True

def printExtraAttrData( m_node_name ):
    """
    print's data stored in extra attributes 
    INPUT:  m_node_name - node name, like 'lambert1' 
    RETURN: True -  if well done, False - otherwise
    USAGE:  printExtraAttrData('lambert1')         
    """
    m_selectionList = OpenMaya.MSelectionList() # create selection list
    m_node = OpenMaya.MObject()                 # create MObject
    m_node_fn = OpenMaya.MFnDependencyNode()    # create a function set
    try:
        # add node with name 'lambert2'
        m_selectionList.add( m_node_name )            
    except:
        return False
    # get first element in the selection list and connect with MObject 
    m_selectionList.getDependNode( 0, m_node )  
    # connect MObject with function set 
    m_node_fn.setObject( m_node )
    # find attribute by name using function set class 
    #
    m_attr = m_node_fn.attribute('sampleCompound')
    # create MPlug object fo work with attribute
    # A plug is a point on a dependency node where a 
    # particular attribute can be connected
    m_attr_plug = OpenMaya.MPlug( m_node, m_attr )
    # create int array fo storing indexes of available items
    #
    m_ind = OpenMaya.MIntArray()
    m_attr_plug.getExistingArrayAttributeIndices(m_ind)
    try:
        for i in m_ind:
            print("IND %s BOOL %s STR %s FLOAT %s" 
                %( i,
                   m_attr_plug.elementByLogicalIndex(i).child(0).asBool(),
                   m_attr_plug.elementByLogicalIndex(i).child(1).asString(),
                   m_attr_plug.elementByLogicalIndex(i).child(2).asFloat() ) )
    except:
        return False
    return True 
    
def setExtraAttrValues( m_node_name, m_index, m_tuple ):
    """
    write data to the node 
    INPUT:  m_node_name - node name, like 'lambert1'
            m_index     - index of item where you wont to write
            m_tuple     - tuple, like: ( True , 'Test', 4.2 ) 
                          m_tuple[0] - True
                          m_tuple[1] - 'Test'
                          m_tuple[2] - 4.2                                                  
    RETURN: True -  if well done, False - otherwise
    USAGE:  setExtraAttrValues( 'lambert1', 1, ( False , 'Test', 4.2 )  )       
    """ 
    m_selectionList = OpenMaya.MSelectionList() 
    m_node = OpenMaya.MObject()                 
    m_node_fn = OpenMaya.MFnDependencyNode()    
    try:
        m_selectionList.add( m_node_name )            
        m_selectionList.getDependNode( 0, m_node )  
        m_node_fn.setObject( m_node )
        m_attr = m_node_fn.attribute('sampleCompound')
        m_attr_plug = OpenMaya.MPlug( m_node, m_attr )
        # convert m_index to integer
        #
        m_index = int(m_index)
        # write data stored in tuple to the node
        #
        m_attr_plug.elementByLogicalIndex(m_index).child(0).setBool( m_tuple[0] )
        m_attr_plug.elementByLogicalIndex(m_index).child(1).setString( m_tuple[1] )
        m_attr_plug.elementByLogicalIndex(m_index).child(2).setFloat( m_tuple[2] )         
    except:
        return False
    return True 


#########################################
http://evgeniyzaitsev.com/2015/11/16/get-all-extra-attributes-maya-python-api/


01
    import maya.cmds as cmds
02
    import maya.OpenMaya as OpenMaya
03
     
04
    def getMObjectFromSelection():
05
        m_selectionList = OpenMaya.MSelectionList()
06
        OpenMaya.MGlobal.getActiveSelectionList( m_selectionList )
07
        m_node = OpenMaya.MObject()
08
        try:                         
09
            m_selectionList.getDependNode( 0, m_node )
10
            if ( m_node.isNull() ): return None
11
        except:
12
            return None
13
        return m_node
14
         
15
    def getAllExtraAttributes():
16
        m_result = []
17
        m_obj         = getMObjectFromSelection()
18
        m_workMFnDep  = OpenMaya.MFnDependencyNode()
19
        m_workMDagMod = OpenMaya.MDagModifier()
20
        if ( m_obj ):
21
            m_objFn    = OpenMaya.MFnDependencyNode()
22
            m_objFn.setObject( m_obj ) # get function set from MObject
23
            m_objRef = m_workMFnDep.create( m_objFn.typeName() ) # Create reference MObject of the given type
24
            # -- get the list --   
25
            m_result = getAttrListDifference( m_obj,m_objRef )
26
            # --
27
            m_workMDagMod.deleteNode( m_objRef ) # set node to delete
28
            m_workMDagMod.doIt() # execute delete operation
29
        return m_result
30
             
31
    def getAttrListDifference( m_obj, m_objRef ):
32
        m_objFn    = OpenMaya.MFnDependencyNode()
33
        m_objRefFn = OpenMaya.MFnDependencyNode()
34
        m_objFn.setObject( m_obj )
35
        m_objRefFn.setObject( m_objRef )
36
        m_result = []
37
        if ( m_objFn.attributeCount() > m_objRefFn.attributeCount() ):
38
            for i in range( m_objRefFn.attributeCount(), m_objFn.attributeCount()  ):
39
                m_atrr = m_objFn.attribute(i)
40
                m_fnAttr = OpenMaya.MFnAttribute( m_atrr )
41
                m_result.append( m_fnAttr.name() )     
42
        return m_result
                
########################################
Get all attributes from the kFileTexture node Maya Python API

import maya.OpenMaya as OpenMaya

m_iterator = OpenMaya.MItDependencyNodes( OpenMaya.MFn.kFileTexture )
m_nodeFn   = OpenMaya.MFnDependencyNode()

while not m_iterator.isDone():
    m_object = m_iterator.thisNode()
    m_nodeFn.setObject( m_object )
    print( "  --- {0} --- ".format( m_nodeFn.name()) )
    for i in range( m_nodeFn.attributeCount() ):
        m_atrr   = m_nodeFn.attribute(i)
        m_fnAttr = OpenMaya.MFnAttribute( m_atrr )
        print( m_fnAttr.name() )
    m_iterator.next()
####################################################


import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

def getMObjectFromSelection():
    m_selectionList = OpenMaya.MSelectionList()
    OpenMaya.MGlobal.getActiveSelectionList( m_selectionList )
    m_node = OpenMaya.MObject() 
    try:                          
        m_selectionList.getDependNode( 0, m_node )
        if ( m_node.isNull() ): return None
    except:
        return None
    return m_node
    
def getAllExtraAttributes():
    m_result = []
    m_obj         = getMObjectFromSelection()
    m_workMFnDep  = OpenMaya.MFnDependencyNode()
    m_workMDagMod = OpenMaya.MDagModifier()
    if ( m_obj ):
        m_objFn    = OpenMaya.MFnDependencyNode()
        m_objFn.setObject( m_obj ) # get function set from MObject
        m_objRef = m_workMFnDep.create( m_objFn.typeName() ) # Create reference MObject of the given type
        # -- get the list --    
        m_result = getAttrListDifference( m_obj,m_objRef )
        # -- 
        m_workMDagMod.deleteNode( m_objRef ) # set node to delete 
        m_workMDagMod.doIt() # execute delete operation
    return m_result
        
def getAttrListDifference( m_obj, m_objRef ):
    m_objFn    = OpenMaya.MFnDependencyNode()
    m_objRefFn = OpenMaya.MFnDependencyNode()
    m_objFn.setObject( m_obj )
    m_objRefFn.setObject( m_objRef )
    m_result = []
    if ( m_objFn.attributeCount() > m_objRefFn.attributeCount() ):
        for i in range( m_objRefFn.attributeCount(), m_objFn.attributeCount()  ):
            m_atrr = m_objFn.attribute(i)
            m_fnAttr = OpenMaya.MFnAttribute( m_atrr )
            m_result.append( m_fnAttr.name() )      
    return m_result

#################################################


import maya.OpenMaya as OpenMaya
def getChildren( inObjName, inType=None ):
    '''
    Returns a list of all children objects of the passed in object. The search can
    be limited to a single object type. Otherwise the search is for all children.
    
    @param inObjName: String. Object to search for children.
    @param inType: MFn::Type. Type of child object to search for.
    @return List of Strings. Full path name of each child object.
    '''
    # Use the object's name to get it's MObject.
    selList = OpenMaya.MSelectionList()
    selList.add( inObjName )
    dagPath = OpenMaya.MDagPath()
    component = OpenMaya.MObject()
    selList.getDagPath( 0, dagPath, component )
    dagFn = OpenMaya.MFnDagNode( dagPath )

    # Get all the children.
    result = []
    for idx in xrange( dagPath.childCount() ):
        child_obj = dagFn.child( idx )
        if child_obj.apiType() != inType:
            child_dag_node = OpenMaya.MFnDagNode( child_obj )
            child_name = child_dag_node.fullPathName()
            result.extend( getChildren( child_dag_node.fullPathName(), inType ) )
            result.append( child_name )
        
    return result

################################################


import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
 
# Create the sphere.
obj_name = 'Ball'
cmds.polySphere( name=obj_name )
 
# Get the MDagPath of the object.
sel_list = OpenMaya.MSelectionList()
sel_list.add( obj_name )
dag = OpenMaya.MDagPath()
component = OpenMaya.MObject()
sel_list.getDagPath( 0, dag, component )
 
# Show that we have the trasnform node.
print dag.partialPathName()
 
# Extend the MDagPath to the shape node.
dag.extendToShapeDirectlyBelow( 0 )
 
# Show that we now have the shape node.
print dag.partialPathName()

#####################################

MPlugs Getting Values
import maya.OpenMaya as OM

def getPlugValue( inPlug ):
    """
    Gets the value of the given plug.
    
    @param inPlug: MPlug. The node plug.
    @return: The value of the passed in node plug.
    """
    pAttribute = inPlug.attribute()
    apiType = pAttribute.apiType()
    
    # Float Groups - rotate, translate, scale; Compounds
    if apiType in [ OM.MFn.kAttribute3Double, OM.MFn.kAttribute3Float, OM.MFn.kCompoundAttribute ]:
        
        result = []
        
        if inPlug.isCompound():
            
            for c in xrange( inPlug.numChildren() ):
                
                result.append( getPlugValue( inPlug.child( c ) ) )
                
            return result
    
    # Distance
    elif apiType in [ OM.MFn.kDoubleLinearAttribute, OM.MFn.kFloatLinearAttribute ]:
        
        return inPlug.asMDistance().asCentimeters()
    
    # Angle
    elif apiType in [ OM.MFn.kDoubleAngleAttribute, OM.MFn.kFloatAngleAttribute ]:
        
        return inPlug.asMAngle().asDegrees()
    
    # TYPED
    elif apiType == OM.MFn.kTypedAttribute:
        
        pType = OM.MFnTypedAttribute( pAttribute ).attrType()
        
        # Matrix
        if pType == OM.MFnData.kMatrix:
            
            return OM.MFnMatrixData( inPlug.asMObject() ).matrix()
        
        # String
        elif pType == OM.MFnData.kString:
            
            return inPlug.asString()
        
    # MATRIX
    elif apiType == OM.MFn.kMatrixAttribute:
        
        return OM.MFnMatrixData( inPlug.asMObject() ).matrix()
    
    # NUMBERS
    elif apiType == OM.MFn.kNumericAttribute:
        
        pType = OM.MFnNumericAttribute( pAttribute ).unitType()

        if pType == OM.MFnNumericData.kBoolean:
            
            return inPlug.asBool()
        
        elif pType in [ OM.MFnNumericData.kShort, OM.MFnNumericData.kInt, OM.MFnNumericData.kLong, OM.MFnNumericData.kByte ]:
            
            return inPlug.asInt()
        
        elif pType in [ OM.MFnNumericData.kFloat, OM.MFnNumericData.kDouble, OM.MFnNumericData.kAddr ]:
            
            return inPlug.asDouble()
        
    # Enum
    elif apiType == OM.MFn.kEnumAttribute:
        
        return inPlug.asInt()
    
#####################################
MPlugs Setting Values
import maya.OpenMaya as OM

def setPlugValue( inPlug, inValue ):
    """
    Sets the given plug's value to the passed in value.

    @param inPlug: _MPlug_. The node plug.
    @param inValue: _Type_. Any value of any data type.
    """
    plugAttribute = inPlug.attribute()
    apiType = plugAttribute.apiType()
    #print plugAttribute.apiTypeStr()
    
    # Float Groups - rotate, translate, scale
    if apiType in [ OM.MFn.kAttribute3Double, OM.MFn.kAttribute3Float ]:
        
        result = []
        if inPlug.isCompound():
            
            if isinstance( inValue, list ):
                
                for c in xrange( inPlug.numChildren() ):
                    
                    result.append( setPlugValue( inPlug.child( c ), inValue[ c ] ) )
                    
                return result
            
            elif type( inValue ) == OM.MEulerRotation:
                
                setPlugValue( inPlug.child( 0 ), inValue.x )
                setPlugValue( inPlug.child( 1 ), inValue.y )
                setPlugValue( inPlug.child( 2 ), inValue.z )
                
            else:
                
                OM.MGlobal.displayError( '{0} :: Passed in value ( {1} ) is {2}. Needs to be type list.'.format( inPlug.info(), inValue, type( inValue ) ) )
    
    # Distance
    elif apiType in [ OM.MFn.kDoubleLinearAttribute, OM.MFn.kFloatLinearAttribute ]:
        
        if isinstance( inValue, float ):
            
            value =  OM.MDistance( inValue, OM.MDistance.kCentimeters )
            inPlug.setMDistance( value )
            
        else:
            
            OM.MGlobal.displayError( '{0} :: Passed in value ( {1} ) is {2}. Needs to be type float.'.format( inPlug.info(), inValue, type( inValue ) ) )
    
    # Angle
    elif apiType in [ OM.MFn.kDoubleAngleAttribute, OM.MFn.kFloatAngleAttribute ]:
        
        if isinstance( inValue, float ):
            
            value = OM.MAngle( inValue, OM.MAngle.kDegrees )
            inPlug.setMAngle( value )
            
        else:
            
            OM.MGlobal.displayError( '{0} :: Passed in value ( {1} ) is {2}. Needs to be type float.'.format( inPlug.info(), inValue, type( inValue ) ) )
            
    # Typed - matrix WE DON'T HANDLE THIS CASE YET!!!!!!!!!
    elif apiType == OM.MFn.kTypedAttribute:
        
        pType = OM.MFnTypedAttribute( plugAttribute ).attrType()

        if pType == OM.MFnData.kMatrix:
            
            if isinstance( inValue, OM.MPlug ):
                
                pass
            
            else:
                
                plugNode = inPlug.node()
                
                MFnTrans = OM.MFnTransform( plugNode )
                
                sourceMatrix = OM.MTransformationMatrix( inValue )#.asMatrix()
                MFnTrans.set( sourceMatrix )
        
        # String
        elif pType == OM.MFnData.kString:
            
            value = inValue
            inPlug.setString( value )
    
    # MATRIX
    elif apiType == OM.MFn.kMatrixAttribute:
        
        if isinstance( inValue, OM.MPlug ):
            
            # inValue must be a MPlug!
            sourceValueAsMObject = OM.MFnMatrixData( inValue.asMObject() ).object()
            inPlug.setMObject( sourceValueAsMObject )
            
        else:
            
            OM.MGlobal.displayError( 'Value object is not an MPlug. To set a MMatrix value, both passed in variables must be MPlugs.' )
    
    # Numbers
    elif apiType == OM.MFn.kNumericAttribute:
        
        pType = OM.MFnNumericAttribute( plugAttribute ).unitType()

        if pType == OM.MFnNumericData.kBoolean:
            
            if isinstance( inValue, bool ):
                
                inPlug.setBool( inValue )
                
            else:
                
                OM.MGlobal.displayError( '{0} :: Passed in value ( {1} ) is {2}. Needs to be type bool.'.format( inPlug.info(), inValue, type( inValue ) ) )
                
        elif pType in [ OM.MFnNumericData.kShort, OM.MFnNumericData.kInt, OM.MFnNumericData.kLong, OM.MFnNumericData.kByte ]:
            
            if isinstance( inValue, int ):
                
                inPlug.setInt( inValue )
            
            else:
                
                OM.MGlobal.displayError( '{0} :: Passed in value ( {1} ) is {2}. Needs to be type int.'.format( inPlug.info(), inValue, type( inValue ) ) )
        
        elif pType in [ OM.MFnNumericData.kFloat, OM.MFnNumericData.kDouble, OM.MFnNumericData.kAddr ]:
            
            if isinstance( inValue, float ):
                
                inPlug.setDouble( inValue )
           
            else:
                
                OM.MGlobal.displayError( '{0} :: Passed in value ( {1} ) is {2}. Needs to be type float.'.format( inPlug.info(), inValue, type( inValue ) ) )
                
    # Enums
    elif apiType == OM.MFn.kEnumAttribute:

        inPlug.setInt( inValue )
#####################################    
MPlugs_Array Plug
import maya.OpenMaya as OpenMaya

mdg_mod = OpenMaya.MDGModifier()
node = mdg_mod.createNode( 'network' )   
mdg_mod.renameNode( node, 'testNode' )
mdg_mod.doIt()

rotation_offset_x_attr = OpenMaya.MFnUnitAttribute() 
rotation_offset_x_obj = rotation_offset_x_attr.create( 'rotationOffsetX', 'rotationOffsetX', OpenMaya.MFnUnitAttribute.kAngle, 0.1 )

rotation_offset_y_attr = OpenMaya.MFnUnitAttribute() 
rotation_offset_y_obj = rotation_offset_y_attr.create( 'rotationOffsetY', 'rotationOffsetY', OpenMaya.MFnUnitAttribute.kAngle, 0.2 )

rotation_offset_z_attr = OpenMaya.MFnUnitAttribute() 
rotation_offset_z_obj = rotation_offset_z_attr.create( 'rotationOffsetZ', 'rotationOffsetZ', OpenMaya.MFnUnitAttribute.kAngle, 0.3 )

rotation_offset = OpenMaya.MFnNumericAttribute()
array_obj = rotation_offset.create( 'rotationOffset', 'rotationOffset', rotation_offset_x_obj, rotation_offset_y_obj, rotation_offset_z_obj )
rotation_offset.setStorable(True)
rotation_offset.setWritable(True)
rotation_offset.setChannelBox(True)

#####################################    
MPlugsCompound Plugs
import maya.OpenMaya as OpenMaya

mdg_mod = OpenMaya.MDGModifier()
node = mdg_mod.createNode( 'network' )   
mdg_mod.renameNode( node, 'testNode' )
mdg_mod.doIt()

type_attr = OpenMaya.MFnTypedAttribute()
string_plug = type_attr.create( 'stringPlug', 'sp', OpenMaya.MFnData.kString )

num_attr = OpenMaya.MFnNumericAttribute()
num_plug = num_attr.create( 'numPlug', 'np', OpenMaya.MFnNumericData.kFloat )

comp_attr = OpenMaya.MFnCompoundAttribute()
comp_plug = comp_attr.create( 'testPlug', 'testPlug' )
comp_attr.setArray( True )
comp_attr.addChild( string_plug )
comp_attr.addChild( num_plug )

mdg_mod = OpenMaya.MDGModifier()
mdg_mod.addAttribute( node, comp_plug )
mdg_mod.doIt()
#####################################    


OpenMaya utilities


def getNodeFromName(in_name):  
    selector = MSelectionList()  
    MGlobal.getSelectionListByName(in_name, selector)  
    node = MObject()  
    selector.getDependNode(0, node)  
    return node  
  
  
def getDependNodeFromName(in_name):  
    return MFnDependencyNode(getNodeFromName(in_name))  
  
  
def getDagPathFromName(in_name):  
    selector = MSelectionList()  
    MGlobal.getSelectionListByName(in_name,selector)  
    path = MDagPath()  
    selector.getDagPath(0, path)  
    return path  
    
    


def findMPlug(in_node, in_attribute):  
    ''''' 
    @param in_node_name: string, unique name of the node, 
    meaning the full path if multiple nodes of this name exist 
    @param in_attribute_name: string, attribute to find, 
    should exist or you'll get errors 
    '''  
    node = getNodeFromName(in_node)  
    return MPlug(node, MFnDependencyNode(node).attribute(in_attribute))  
  
  
def getPlugValue(in_plug):  
    ''''' 
    @param in_plug: MPlug, to get value from 
    '''  
    plugs = []  
    if in_plug.isCompound():  
        for i in in_plug.numChildren():  
            plugs.append( in_plug.child(i) )  
    elif in_plug.isArray():  
        for i in in_plug.numElements():  
            plugs.append( in_plug.getElementByPhysicalIndex(i) )  
    else:  
        plugs.append(in_plug)  
      
    out = [] #compound list of all data in the plug or its child plugs  
    for plug in plugs:  
        attr = plug.attribute()  
        if attr.hasFn(MFn.kNumericAttribute):  
            type = MFnNumericAttribute(attr).unitType()  
            if type in (MFnNumericData.kBoolean, MFnNumericData.kByte):  
                out.append(plug.asBool())  
            elif type == MFnNumericData.kChar:  
                out.append(plug.asChar())  
            elif type == MFnNumericData.kShort:  
                out.append(plug.asShort())  
            elif type in (MFnNumericData.kInt, MFnNumericData.kLong):  
                out.append(plug.asInt())  
            elif type == MFnNumericData.kFloat:  
                out.append(plug.asFloat())  
            elif type == MFnNumericData.kDouble:  
                out.append(plug.asDouble())  
        elif attr.hasFn(MFn.kUnitAttribute):  
            type = MFnUnitAttribute(attr).unitType()  
            if type == MFnUnitAttribute.kAngle:  
                out.append(plug.asMAngle())  
            elif type == MFnUnitAttribute.kDistance:  
                out.append(plug.asMDistance())  
            elif type == MFnUnitAttribute.kTime:  
                out.append(plug.asMTime())  
        elif attr.hasFn(MFn.kTypedAttribute):  
            type = MFnTypedAttribute(attr).attrType()  
            if type == MFnData.kString:  
                out.append(plug.asString())  
        else:  
            #last resort for unimplemented data types  
            out.append(plug.asMObject())  
    return out  



def getAttrFn(in_attrobj):  
    ''''' 
    @param in_attrobj: MObject that has the MFnAttribute functionset 
    '''  
    if in_attrobj.hasFn(MFn.kCompoundAttribute):  
        return MFnCompoundAttribute  
    elif in_attrobj.hasFn(MFn.kEnumAttribute):  
        return MFnEnumAttribute  
    elif in_attrobj.hasFn(MFn.kGenericAttribute):  
        return MFnGenericAttribute  
    elif in_attrobj.hasFn(MFn.kLightDataAttribute):  
        return MFnLightDataAttribute  
    elif in_attrobj.hasFn(MFn.kMatrixAttribute):  
        return MFnMatrixAttribute  
    elif in_attrobj.hasFn(MFn.kMessageAttribute):  
        return MFnMessageAttribute  
    elif in_attrobj.hasFn(MFn.kNumericAttribute):  
        return MFnNumericAttribute  
    elif in_attrobj.hasFn(MFn.kTypedAttribute):  
        return MFnTypedAttribute  
    elif in_attrobj.hasFn(MFn.kUnitAttribute):  
        return MFnUnitAttribute  
    return MFnAttribute  
  
  
def assignMFnAttribute(in_node_name, in_attribute_name):  
    ''''' 
    @param in_node_name: string, unique name of the node, 
    meaning the full path if multiple nodes of this name exist 
    @param in_attribute_name: attribute to find, should exist 
    or you'll get errors 
    '''  
    attr = getDependNodeFromName(in_node_name).attribute(in_attribute_name)  
    return getAttrFn(attr)(attr)      




import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
 
def selectByType( inTraversal=OpenMaya.MItDag.kDepthFirst, inType=None ):
    '''
    Select all nodes of the given type.
    
    @inTraversal: MItDag::TraversalType. Valid options are...
            kInvalidType - 
            kDepthFirst - 
            kBreadthFirst - 
    @inType: MFn::Type. Read the Maya documentation to get a list of valid
            node types.
    '''
    if inType:
        selList = OpenMaya.MSelectionList()
        dagIterator = OpenMaya.MItDag( inTraversal, inType )
        while not dagIterator.isDone():
            selList.add( dagIterator.fullPathName() )
            dagIterator.next()
        if not selList.isEmpty():
            OpenMaya.MGlobal.setActiveSelectionList( selList )
        else:
            OpenMaya.MGlobal.displayInfo( 'No object(s) of type [{0}] exist in this scene.'.format( inType ) )
    else:
        raise RuntimeError( 'inType is None.' )
 
cmds.polySphere( name='pSphere1' )
 
selectByType( inTraversal=OpenMaya.MItDag.kDepthFirst, inType=OpenMaya.MFn.kMesh )

###########################################
User Defined Colors

import maya.OpenMaya as OpenMaya

def setUserDefinedColor( inColorID, inColor ):
    '''
    Set user defined colors. Assumes RGB.
    
    @inColorID: Int. 1-9. ID number of the userDefined color.
    @inColor: List of Floats. RGB value.
    '''    
    userString = 'userDefined{0}'.format( inColorID )
    melCommand = 'displayRGBColor \"{0}\" {1} {2} {3}'.format( userString,
                                                               inColor[0],
                                                               inColor[1],
                                                               inColor[2] )
    OpenMaya.MGlobal.executeCommand( melCommand )
    
    

def getUserDefinedColors( inType=1 ):
    '''
    Gets the current user defined colors.
    
    @inType: Int. 1 is RGB. 2 is HSV.
    @return: List of Lists. User defined colors 1-8.
    '''
    userColors = []
    for color in xrange( 1, 9 ):
        userString = 'userDefined{0}'.format( color )
        if inType == 1:
            melCommand = 'displayRGBColor \"{0}\" -query'.format( userString )
        elif inType == 2:
            melCommand = 'displayRGBColor \"{0}\" -query -hueSaturationValue'.format( userString )
        result = OpenMaya.MDoubleArray()
        OpenMaya.MGlobal.executeCommand( melCommand, result ) 
        userColors.append( result )
    return userColors



def convertRGB( inType=1, inRGB=[] ):
    '''
    Converts and RGB value between 0-1 and 0-255.
    
    @param inType: Int. 1 or 2.
        1, converts 0-1 values to 0-255.
        2, converts 0-255 values to 0-1.
    @param inRGB: List of Floats. RGB value.
    @param return: List of Floats. Converted RGB value. 
    '''
    result = []
    if inType == 1:
        for channel in inRGB:
            result.append( channel * 255 )
    elif inType == 2:
        for channel in inRGB:
            result.append( channel / 255 )
    return result    


#----------------------------------------------------------------------------------
#   SCRIPT          vtxNormalsToSoftHardEdges.py
#   AUTHOR          Zaitsev Evgeniy
#                   ev.zaitsev@gmail.com
#
#                   import vtxNormalsToSoftHardEdges; vtxNormalsToSoftHardEdges.convertNormals();
#----------------------------------------------------------------------------------

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

class convertNormals( object ):
    def __init__( self ):
        self.convertSelected()

    def convertSelected( self ):
        print(" -------------------- ")
        m_list = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList( m_list )
        m_listIt = OpenMaya.MItSelectionList( m_list ) 
        m_listback = []
        while not m_listIt.isDone():
            self.m_path  = OpenMaya.MDagPath()
            m_listIt.getDagPath( self.m_path )
            if ( self.m_path.hasFn( OpenMaya.MFn.kMesh ) ):
                print( "Soft/Hard set to mesh {}".format( self.m_path.fullPathName() ) )
                self.setSoftHard()
                m_listback.append( self.m_path.fullPathName() )
            m_listIt.next()
        cmds.select( clear = True )
        for m_obj in m_listback:
            cmds.select( m_obj, add = True )
        print(" -------------------- ")

    def setSoftHard( self ):
        # calculate Hard Edges
        m_hardEdges = []
        m_itEdgeIt     = OpenMaya.MItMeshEdge( self.m_path ) 
        self.m_fnMesh = OpenMaya.MFnMesh( self.m_path )
        while not m_itEdgeIt.isDone():
            m_facesArray = OpenMaya.MIntArray()
            m_edgeId = m_itEdgeIt.index()
            m_itEdgeIt.getConnectedFaces(m_facesArray)  
            m_start, m_end = self.getEdgeVertices( m_edgeId )
            m_state = self.isEdgeSmooth( m_edgeId, m_start, m_end, m_facesArray )
            if ( False == m_state ):
                m_hardEdges.append( m_edgeId )
            #print( m_edgeId, m_state, m_start, m_end, m_facesArray )
            m_itEdgeIt.next()
        # select and set Hard Edges 
        m_aMember           = ''
        m_lastIndices       = [ -1, -1 ]
        m_haveEdge          = False
        for m_edgeId in m_hardEdges:
            if ( -1 == m_lastIndices[0] ):
                m_lastIndices[0] = m_edgeId
                m_lastIndices[1] = m_edgeId
            else:
                m_currentIndex = m_edgeId
                if ( m_currentIndex > m_lastIndices[1] + 1 ):
                    m_aMember += '{0}.e[{1}:{2}] '.format( self.m_path.fullPathName(), m_lastIndices[0], m_lastIndices[1] )
                    m_lastIndices[0] = m_currentIndex
                    m_lastIndices[1] = m_currentIndex 
                else:
                    m_lastIndices[1] = m_currentIndex
            m_haveEdge = True
        if ( m_haveEdge ):
            m_aMember += '{0}.e[{1}:{2}] '.format( self.m_path.fullPathName(), m_lastIndices[0], m_lastIndices[1] )
        m_resultString = ""
        m_resultString += "select -r {};\n".format( self.m_path.fullPathName())
        m_resultString += "polyNormalPerVertex -ufn true;\n";
        m_resultString += "polySoftEdge -a 180 -ch 1;\n";
        m_resultString += "select -r {0};\n".format( m_aMember )
        m_resultString += "polySoftEdge -a 0 -ch 1;\n"
        m_resultString += "select -cl;"
        #print(m_resultString)
        OpenMaya.MGlobal.executeCommand( m_resultString )
    
    def getEdgeVertices( self, m_edgeId ):
        m_util = OpenMaya.MScriptUtil() 
        m_util.createFromList([0, 0], 2)
        m_ptr = m_util.asInt2Ptr()
        self.m_fnMesh.getEdgeVertices( m_edgeId, m_ptr )
        m_start = m_util.getInt2ArrayItem( m_ptr,0,0 )
        m_end = m_util.getInt2ArrayItem( m_ptr,0,1 )
        return m_start, m_end
        
    def isEdgeSmooth( self, m_edgeId, m_start, m_end, m_facesArray ):
        m_state = True
        m_normalStartArr = OpenMaya.MVectorArray()
        m_normalEndArr   = OpenMaya.MVectorArray()
        for m_faceId in m_facesArray:
            m_normalStart = OpenMaya.MVector()
            m_normalEnd   = OpenMaya.MVector()
            self.m_fnMesh.getFaceVertexNormal( m_faceId, m_start, m_normalStart, OpenMaya.MFn.kWorld )
            self.m_fnMesh.getFaceVertexNormal( m_faceId, m_end, m_normalEnd, OpenMaya.MFn.kWorld )
            m_normalStartArr.append( m_normalStart )
            m_normalEndArr.append(m_normalEnd)
        m_normalStart1 = m_normalStartArr[0]
        for i in range( m_normalStartArr.length() ):
            m_normalStart2 = m_normalStartArr[i]
            if ( m_normalStart1 != m_normalStart2 ):
                m_state = False
            m_normalStart1 = m_normalStart2
        m_normalEnd1 = m_normalEndArr[0]
        for i in range( m_normalEndArr.length() ):
            m_normalEnd2 = m_normalEndArr[i]
            if ( m_normalEnd1 != m_normalEnd2 ):
                m_state = False
            m_normalEnd1 = m_normalEnd2
        return m_state

