import os
import logging

from pymel import core

from crowd import resource
from crowd.core import cdata
from crowd.core import controls
from crowd.core import generic
from crowd.core import skeleton
from crowd.core import readWrite

reload(generic)
reload(readWrite)
reload(skeleton)
reload(resource)
reload(controls)


def create(root=None):
    if not root:
        nodes, message = skeleton.get_root_skeletons()
        if not nodes:
            return 'failed', nodes, message
        root = nodes[0]
    input = get_input('biped')
    create_puppet(root, input)


def get_root_skeletons():
    return skeleton.get_root_skeletons()


def get_input(tag):
    rw = readWrite.Connect()
    rw.file_path = os.path.join(
        resource.getInputPath(), 'puppet', '%s.json' % tag)
    data = rw.read(all=False)
    return data


def create_puppet(root, inputs):
    '''
        :example
            from crowd.core import biped
            roots = biped.get_root_skeletons()
            input = biped.get_input('biped')
            biped.create_puppet(roots[0][0], input)   
    '''
    
    
    
    print '\troot \t',  root

    if not isinstance(root, str):
        root = str(root)

    skeletons = generic.get_root_children()
    scene_skeletons = generic.get_skeletons(root, skeletons)

    suffix = ''

    fk_skeletons = generic.find_fk_skeletons(scene_skeletons, inputs['fk'])
    fk_node = create_fk(fk_skeletons, inputs['fk'])
    ik_skeletons = generic.find_ik_skeletons(scene_skeletons, inputs['ik'])
    ik_nodes = create_ik(ik_skeletons, inputs['ik'])
    puppet = core.group(n='puppet', em=True)
    controls = core.group(n='controls', em=True)

    world_ctrl = controls.create_shape(
        'world_ctrl', shape='cricle', orientation=[0, 1, 0], raduis=4.0)
    generic.disable_attributes(world_ctrl, attributs=['v'])
    ik = core.group(n='ik', em=True)
    joint = core.group(n='joints', em=True)
    controls.setParent(puppet)
    world_ctrl.setParent(controls)
    ik.setParent(puppet)
    joint.setParent(puppet)
    ik_nodes[0].setParent(controls)
    ik_nodes[1].setParent(ik)
    fk_node.setParent(controls)
    core.PyNode(root).setParent(joint)

    for each in [ik_nodes[0], fk_node, joint]:
        core.parentConstraint(
            world_ctrl, each, w=True, n='%s_parent_constraint' % world_ctrl)
        core.scaleConstraint(
            world_ctrl, each, o=[1, 1, 1], w=True, n='%s_scale_constraint' % world_ctrl)


def create_fk(skeletons, data):
    ctrl_parent = core.group(n='fk_ctrl_group', em=True)
    fk_data = cdata.sorted_order_data(data)
    print fk_data
    controls = {}
    for each_fk in fk_data:
        for k, v in skeletons[each_fk].items():
            for each_skel in v:
                current_data = data[each_fk]
                if not current_data['control']:
                    continue
                control_name = '{}_{}_ctrl'.format(
                    control.control_types()[k], each_fk)
                shape, group = control.create(
                    control_name, shape=current_data['control'], raduis=current_data['radius'])
                translate = core.xform(each_skel, q=True, ws=True, t=True)
                roatation = core.xform(
                    each_skel, q=True, a=True, ws=True, ro=True)
                core.xform(group, ws=True, t=translate)
                core.xform(group, ro=roatation)
                core.parentConstraint(
                    shape, each_skel, w=True, n='%s_parent_constraint' % each_skel)
                controls.setdefault(each_fk, []).append([shape, group])
                group.setParent(ctrl_parent)
                attributs = ['tx', 'ty', 'tz', 'sx', 'sy', 'sz', 'v']
                if each_fk == 'root' or each_fk == 'world':
                    attributs = ['sx', 'sy', 'sz', 'v']
                generic.disable_attributes(
                    shape, attributs=attributs)

    # fk control constrains
    for each_fk in fk_data:
        current_data = data[each_fk]
        if current_data['parent'] not in controls:
            continue
        parents = controls[current_data['parent']]
        chidren = controls[each_fk]
        for index in range(len(chidren)):
            parent = parents[0][0]
            child = chidren[index][1]
            core.parentConstraint(
                parent, child, mo=True, w=1, n='%s_parent_constraint' % child)
    return ctrl_parent


def create_ik(skeletons, data):
    ctrl_parent = core.group(n='ik_ctrl_group', em=True)
    ik_parent = core.group(n='ik_handle_group', em=True)
    ik_parent.setAttr('v', 0)
    for k, v in skeletons.items():
        for index, content in v.items():
            side = control.control_types()[index]
            ik_setup(side, data[k], content['joints'], ctrl_parent, ik_parent)
    return ctrl_parent, ik_parent


def ik_setup(side, data, joints, ctrl_parent, ik_parent):
    prefix = '%s_%s' % (side, data['joints'][-1])
    ik_handle = core.ikHandle(
        n='%s_ik_handle' % (prefix),
        sj=joints[0],
        ee=joints[-1],
        s='sticy',
        sol='ikRPsolver')
    ik_handle[1].rename('%s_ik_effector' % (prefix))
    control_name = '%s_ik_ctrl' % (prefix)
    shape, group = control.create(
        control_name, shape=data['control'], raduis=data['radius'])
    translate = core.xform(ik_handle[0], q=True, ws=True, t=True)
    core.xform(group, ws=True, t=translate)
    core.xform(group, ro=[0, 0, 0])
    core.parentConstraint(
        shape, ik_handle[0], w=1, n='%s_parent_constraint' % (prefix))
    shape.addAttr('twist', at='double', dv=0, k=True)
    shape.attr('twist').connect(ik_handle[0].attr('twist'))
    generic.disable_attributes(shape, attributs=['sx', 'sy', 'sz', 'v'])
    generic.disable_attributes(group, attributs=None)
    group.setParent(ctrl_parent)
    ik_handle[0].setParent(ik_parent)
