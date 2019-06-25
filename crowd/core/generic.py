import logging
import json

from pymel import core


def get_skeleton_type():
    return 'joint'


def get_joint_str_type():
    data = {
        'side': {
            0: 'Center',
            1: 'Left',
            2: 'Right',
            3: 'None'},
        'type': {
            18: 'Other'}
    }
    print '\n#result\n', json.dumps(data, indent=4)
    return data


def get_joint_types(node):
    pynode = core.PyNode(node)
    if pynode.type() != get_skeleton_type():
        logging.warning('wrong node type!...')
        return None, None, None
    side = pynode.getAttr('side')
    joint_type = pynode.getAttr('type')
    other_type = pynode.getAttr('otherType')
    return side, joint_type, other_type


def get_joint_label(node):
    pynode = core.PyNode(node)
    if pynode.type() != get_skeleton_type():
        logging.warning('wrong node type!...')
        return None
    other_type = pynode.getAttr('otherType')
    return other_type


def disable_attributes(node, attributs=None):
    if not attributs:
        attributs = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
    for each_attr in attributs:
        node.attr(each_attr).setLocked(True)
        node.attr(each_attr).setKeyable(False)


def search_data(key, input_data):
    result = None
    for label, node in input_data.items():
        if label != key:
            continue
        result = node
        return result
    return result


def find_fk_skeletons(skeletons, data):
    fk_skeletons = {}
    for k, v in skeletons.items():
        for each in v:
            if each not in data:
                continue
            fk_skeletons.setdefault(each, {})
            fk_skeletons[each].setdefault(k, []).append(v[each])
    return fk_skeletons


def find_ik_skeletons(skeletons, data):
    ik_skeletons = {}
    for each in data:
        side_skeletons = {}
        for index in range(1, 3):
            side_skeletons.setdefault(index, {})
            for each_joint in data[each]['joints']:
                skeleton = search_data(each_joint, skeletons[index])
                side_skeletons[index].setdefault('joints', []).append(skeleton)
        ik_skeletons.setdefault(each, side_skeletons)
    return ik_skeletons


def get_skeletons(root, skeletons):
    current_data = {}
    for k, v in skeletons.items():
        if root != k.name():
            continue
        current_data = {k: v}
        break
    joints = []
    for k, v in current_data.items():
        joints.append(k)
        joints.extend(v)
    data = {}
    for each_skeletons in joints:
        side = each_skeletons.getAttr('side')
        joint_type = each_skeletons.getAttr('type')
        if joint_type != 18:
            continue
        other_type = each_skeletons.getAttr('otherType')
        data.setdefault(side, {})
        data[side].update({other_type.encode(): each_skeletons})
    return data


def get_root_children():
    roots = get_root_joints()
    result = {}
    for each_root in roots:
        print '\t', each_root
        children = get_children(each_root)
        result.setdefault(each_root, list(children))

    return result


def get_root_joints():
    joints = core.ls(type='joint')
    root_joints = []
    for each_joint in joints:
        other_type = each_joint.getAttr('otherType')
        if other_type != 'world':
            continue
        root_joints.append(each_joint)
    return root_joints


def get_children(root):
    stack = set()
    nodes = root.getChildren()
    children = []
    while nodes:
        node = nodes.pop()
        if node.type() != 'joint':
            continue
        if node in stack:
            continue
        children = node.getChildren()
        stack.add(node)
        nodes.extend(children)
    return stack


def get_hierarchy(root, types=None):
    if isinstance(root, str):
        root = core.PyNode(root)
    nodes = []
    seen = set()
    stack = [root]
    index = 0
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        if types:
            for each_type in types:
                if node.type() != each_type:
                    continue
                nodes.append(node)
                break
        else:
            nodes.append(node)
        stack.extend(node.getChildren())
        seen.add(node)
        index += 1
    return nodes
