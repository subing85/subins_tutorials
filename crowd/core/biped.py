import json

from pprint import pprint

from pymel import core

from crowd.core import generic
from crowd.core import controls

reload(generic)
reload(controls)


def create_puppet(root, input_data):
    skeletons = generic.get_root_children()
    scene_skeletons = generic.get_skeletons(root, skeletons)
    # 0 = center joints, 1 = left joints, 2 = right joints

    create_fk(scene_skeletons, input_data['fk'])
    create_ik(scene_skeletons, input_data['ik'])


def create_fk(scene_skeletons, input_fk_data):
    fk_skeletons = generic.find_fk_skeletons(
        scene_skeletons, input_fk_data, string=False)
    ctrl_type = controls.control_types()
    drivers = {}
    fk_group_name = generic.set_node_name('fk_ctrl_group')
    driver_group = core.group(n=fk_group_name, em=True)
    for index, content in fk_skeletons.items():
        control_name = generic.set_node_name('{}_{}_ctrl'.format(
            ctrl_type[content['side']], content['label']))
        orientation = [1, 0, 0]
        if content['label'] == 'world':
            orientation = [0, 1, 0]
        shape, group = controls.create(
            control_name,
            shape=content['control'],
            raduis=content['radius'],
            orientation=orientation
        )
        controls.snap(content['joint'], group)
        core.parentConstraint(
            shape,
            content['joint'],
            w=True,
            n='%s_parent_constraint' % content['label']
        )
        group.setParent(driver_group)
        attributs = ['tx', 'ty', 'tz', 'sx', 'sy', 'sz', 'v']
        if content['label'] == 'root' or content['label'] == 'world':
            attributs = ['sx', 'sy', 'sz', 'v']
        generic.disable_attributes(shape, attributs=attributs)
        # print content
        parent_data = generic.search_joint(scene_skeletons, content['parent'])
        if not parent_data:
            continue
        core.parentConstraint(
            parent_data.keys()[0],
            group,
            mo=True,
            w=True,
            n='%s_parent_constraint' % group
        )


def create_ik(scene_skeletons, input_ik_data):
    ik_skeletons = generic.find_ik_skeletons(
        scene_skeletons, input_ik_data, string=False)    
    
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
