import maya.OpenMaya as om


def get_selected_obj_names():
    """
    List selections in the current scene.

    :return: `list`,    # ex: [u'|pCube1', u'|pSphere1'] #
    """
    obj_names = list()
    selection_list = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection_list)

    obj_count = selection_list.length()
    sels_iter = om.MItSelectionList(selection_list)
    for i in range(obj_count):
        dag_path = om.MDagPath()
        sels_iter.getDagPath(dag_path)
        obj_names.append(dag_path.fullPathName())
        sels_iter.next()
    return obj_names


def get_dag_path_list(obj_name, all_descendents=True):
    """
    List dag path for given input object.

    Ex:
        ----+ pCube1
            |
            +---- pCube2

        #   -----   #
        childeren = get_dag_path_list(obj_name='pCube1')
        for child in children:
            print child.fullPathName()

        #   Reslut  #
        |pCube1|pCubeShape1
        |pCube1|pCube2|pCubeShape2
        |pCube1|pCube2

    :param obj_name: `str`,     Ex: obj_name = 'pCube1'
    :return: `list`
    """

    selection_list = om.MSelectionList()
    try:
        selection_list.add(obj_name)
    except RuntimeError:
        return

    dag_path = om.MDagPath()
    selection_list.getDagPath(0, dag_path)
    results = list()

    if not all_descendents:
        results.append(dag_path)
        return results

    for i in range(dag_path.childCount()):
        child = dag_path.child(i)
        child_dag_path = dag_path.getAPathTo(child)
        results.extend(get_dag_path_list(obj_name=child_dag_path))
        results.append(child_dag_path)

    return results


def setToIMathArray(type_traits, *in_list):
    """
    Set to imath array.

    :Param iTPTraits: alembic abc type traits.
                      (can look at Alembic/Abc/TypedPropertyTraits.h)
                      Ex: Int32TPTraits, P3fTPTraits,...
    :Param iList:
    :Return: imath array object
    :Rtype: imath.V3fArray
    """
    array = type_traits.arrayType(len(in_list))
    for i in range(len(in_list)):
        array[i] = in_list[i]
    return array

