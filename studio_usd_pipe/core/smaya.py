import os
import shutil


def has_exists(node):
    from maya import OpenMaya
    mit_dependency_nodes = OpenMaya.MItDependencyNodes()
    mobjects = OpenMaya.MObjectArray()
    while not mit_dependency_nodes.isDone():
        mobject = mit_dependency_nodes.item()
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        if mfn_dependency_node.name() == node:
            return True
        mit_dependency_nodes.next()
    return False


def get_nodes(node_type):
    from maya import OpenMaya
    mit_dependency_nodes = OpenMaya.MItDependencyNodes()
    mobjects = OpenMaya.MObjectArray()
    while not mit_dependency_nodes.isDone():
        mobject = mit_dependency_nodes.item()
        if mobject.hasFn(node_type):
            mobjects.append(mobject)
        mit_dependency_nodes.next()
    return mobjects


def get_scene_nodes():
    from maya import OpenMaya
    default_nodes = ['persp', 'top', 'front', 'side']
    mobjects = []
    mit_dependency_nodes = OpenMaya.MItDependencyNodes()
    while not mit_dependency_nodes.isDone():
        mobject = mit_dependency_nodes.item()
        if mobject.hasFn(OpenMaya.MFn.kTransform):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
            if mfn_dependency_node.name() not in default_nodes:
                mobjects.append(mfn_dependency_node.name().encode())
        mit_dependency_nodes.next()
    return mobjects


def get_string_attribute_values(mobjects, attribute):
    from maya import OpenMaya
    data = {}
    for index in range(mobjects.length()):
        mfn_Dependency_node = OpenMaya.MFnDependencyNode(mobjects[index])
        mplug = mfn_Dependency_node.findPlug(attribute)
        data.setdefault(mplug, mplug.asString())
    return data


def save_file(source_file, stamped_time):
    from maya import OpenMaya
    file_io = OpenMaya.MFileIO()
    # file_io.open(source_file)
    file_type = file_io.fileType()
    file_io.saveAs(source_file, file_type.encode(), True)
    os.utime(source_file, (stamped_time, stamped_time))


def remove_file(path):
    if not os.path.isfile(path):
        return
    os.chmod(path, 0777)
    try:
        os.remove(path)
    except Exception as OSError:
        print OSError
