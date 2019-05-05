from pymel import core
from maya import OpenMaya


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
    return data


def create_skeleton(inputs):
    parent_data = {}
    for name, attributes in inputs.items():
        OpenMaya.MGlobal.clearSelectionList()
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('joint')
        mfn_dag_node.setName(name)
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
    OpenMaya.MGlobal.clearSelectionList()
    return parent_data


def collect_puppet_skeleton(tag, root):
    
    ik_skeletons = [
        ['pelvis', 'knee', 'ankle'], 
        ['shoulder', 'elbow, wrist']
        ]
    fk_skeletons = ''

    pass


def get_root_children():
    roots = get_root_joints()
    result = {}
    for each_root in roots:
        children = get_children(each_root)
        result.setdefault(each_root, list(children))
    return result


def get_root_joints():
    joints = core.ls(type='joint')
    root_joints = []
    for each_joint in joints:
        other_type = each_joint.getAttr('otherType')
        if other_type != 'root':
            continue
        root_joints.append(each_joint)
    return root_joints


def get_children(root):
    stack = set()
    nodes = root.getChildren()
    children = []
    while nodes:
        node = nodes.pop()
        if node in stack:
            continue
        children = node.getChildren()
        stack.add(node)
        nodes.extend(children)
    return stack
