import logging
from pymel import core
from maya import OpenMaya


def get_root_skeletons():
    default_nodes = ['persp', 'top', 'front', 'side']
    maya_nodes = core.ls(assemblies=True)
    nodes = [each.name().encode()
             for each in maya_nodes if each.name() not in default_nodes]
    if len(nodes) > 1:
        logging.warning('#valueError: more than one hierarchy found!..')
        return None, 'more than one hierarchy found!..'
    if len(nodes) == 0:
        logging.warning('#valueError: not found any hierarchy!..')
        return None, 'not found any hierarchy!..'
    return nodes, 'good hierarchy!..'


def get_skeleton_inputs(joints):
    data = {}
    sides = {0: 'center', 1: 'left', 2: 'right', 3: 'none'}
    for each in joints:
        parent = each.getParent()
        if parent:
            parent = parent.name().encode()
        core.parent(each, w=True)
        xyz = core.xform(each, q=True, ws=True, t=True)
        xyz = [round(xyz[0], 2), round(xyz[1], 2), round(xyz[2], 2)]
        radius = each.getRadius()
        side = each.getAttr('side')
        joint_type = each.getAttr('type')
        other_type = each.getAttr('otherType')
        rot_order = each.getRotationOrder()
        joint_orient = each.getAttr('jointOrient')
        joint_orient = [round(joint_orient.x, 2), round(
            joint_orient.y, 2), round(joint_orient.z, 2)]
        p_anglex = each.getAttr('preferredAngleX')
        p_angley = each.getAttr('preferredAngleY')
        p_anglez = each.getAttr('preferredAngleZ')
        rotation = each.getRotation()
        rotation = [round(rotation[0], 2), round(
            rotation[1], 2), round(rotation[2], 2)]
        values = {
            'translate': xyz,
            'radius': radius,
            'side': side,
            'type': joint_type,
            'otherType': other_type.encode(),
            'rotateOrder': rot_order.index,
            'jointOrient': joint_orient,
            'preferredAngle': [p_anglex, p_angley, p_anglez],
            'rotate': rotation,
            'parent': parent
        }
        data[each.name().encode()] = values
        each.setParent(parent)
    return data


def create_skeleton(tag, inputs, position=None, parent=None):
    if not position:
        position = [0, 0, 0]
    parent_data = {}
    for name, attributes in inputs.items():
        OpenMaya.MGlobal.clearSelectionList()
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('joint')
        node_name = name
        if core.ls('{}*'.format(name)):
            node_name = '{}{}'.format(name, len(core.ls('{}*'.format(name))))
        mfn_dag_node.setName(node_name)
        mdag_path = OpenMaya.MDagPath()
        mfn_dag_node.getPath(mdag_path)
        add_tag(mdag_path.node(), tag=tag)
        joint_dag_path = OpenMaya.MDagPath()
        mfn_dag_node.getPath(joint_dag_path)
        parent_data.setdefault(name, joint_dag_path)
        for attribute, values in attributes.items():
            if 'parent' == attribute:
                continue
            m_plug = mfn_dag_node.findPlug(attribute)
            node = core.PyNode(m_plug)
            try:
                node.set(values)
            except:
                print 'error\t', attribute

    for k, v in parent_data.items():
        root = parent_data[k]
        if not inputs[k]['parent']:
            continue
        parent = parent_data[inputs[k]['parent']]
        core.PyNode(root).setParent(core.PyNode(parent))

    any_node = core.PyNode(parent_data.keys()[0])
    root_dag_path = parent_data[any_node.root().name()]

    mFnTransform = OpenMaya.MFnTransform(root_dag_path)
    mvector = OpenMaya.MVector(position[0], position[1], position[2])
    mFnTransform.setTranslation(mvector, OpenMaya.MSpace.kWorld)

    OpenMaya.MGlobal.clearSelectionList()
    return root_dag_path, parent_data


def add_tag(mobject, tag=None):
    mfn_attribute = OpenMaya.MFnTypedAttribute()
    skeleton_attribute = mfn_attribute.create(
        'crowd_type', "crdt", OpenMaya.MFnData.kString)
    mfn_attribute.setKeyable(False)
    mfn_attribute.setWritable(False)
    mfn_attribute.setReadable(False)
    mfn_attribute.setStorable(False)
    mfn_attribute.setHidden(False)
    mfn_attribute.setChannelBox(False)
    mfn_dependency_node = OpenMaya.MFnDependencyNode()
    mfn_dependency_node.setObject(mobject)
    mfn_dependency_node.addAttribute(skeleton_attribute)
    if tag:
        plug = mfn_dependency_node.findPlug('crowd_type')
        plug.setString(tag)


'''
from crowd.api import crowdSkeleton
reload(crowdSkeleton)
crowd_skeleton = crowdSkeleton.Connect()
root_node, result = crowd_skeleton.create('biped')

from crowd.core import skeleton

joints = core.ls(sl=1)

data = skeleton.get_skeleton_inputs(joints)
from crowd.core import readWrite
reload(readWrite)
rw = readWrite.ReadWrite(    
    fm='json',
    pa='/venture/subins_tutorials/crowd/resource/skeletons',
    na='biped',
    ty='skeleton',
    tg='biped')
rw.write(data, force=True) 
'''
