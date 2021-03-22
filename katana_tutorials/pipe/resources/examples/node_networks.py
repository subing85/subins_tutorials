from katana import NodegraphAPI


def example():
    knodes = NodegraphAPI.GetAllSelectedNodes()
    if knodes:
        print knodes[0].getType()    
    root_node = NodegraphAPI.GetRootNode()   
    
    # alembic node 1
    batman_abc = NodegraphAPI.CreateNode('Alembic_In', parent=root_node)
    batman_abc.setName('batman_abc')
    name_parameter = batman_abc.getParameter('name')
    name_parameter.setValue('/root/world/character', 1.0)
    name_parameter.setUseNodeDefault(False)
    abc_paramter = batman_abc.getParameter('abcAsset')
    abc_paramter.setValue('/venture/shows/katana_tutorials/tmp/batman.abc', 1.0)
    abc_paramter.setUseNodeDefault(False)
    
    # katana primitive - plane
    primitive_plane = NodegraphAPI.CreateNode('PrimitiveCreate', parent=root_node)
    NodegraphAPI.SetNodePosition(primitive_plane, [200, 0])
    primitive_plane.setName('katana_plane')
    name_parameter = primitive_plane.getParameter('name')
    name_parameter.setValue('/root/world/set/ground', 1.0)
    name_parameter.setUseNodeDefault(False)
    type_parameter = primitive_plane.getParameter('type')
    type_parameter.setValue('plane', 1.0)
    type_parameter.setUseNodeDefault(False)
    scale_paramter = primitive_plane.getParameter('transform.scale')
    xyz = {'x': 50, 'y': 1, 'z': 50}
    for k, v in xyz.items():
        scale_paramter.getChild(k).setValue(v, 1.0)
        scale_paramter.getChild(k).setUseNodeDefault(False)
    
    # alembic camera
    camera_abc = NodegraphAPI.CreateNode('Alembic_In', parent=root_node)
    NodegraphAPI.SetNodePosition(camera_abc, [400, 0])
    camera_abc.setName('camera_abc')
    name_parameter = camera_abc.getParameter('name')
    name_parameter.setValue('/root/world/camera', 1.0)
    name_parameter.setUseNodeDefault(False)
    abc_paramter = camera_abc.getParameter('abcAsset')
    abc_paramter.setValue('/venture/shows/katana_tutorials/tmp/camera.abc', 1.0)
    abc_paramter.setUseNodeDefault(False)
    
    # katana primitive - camera
    katana_camera = NodegraphAPI.CreateNode('CameraCreate', parent=root_node)
    NodegraphAPI.SetNodePosition(katana_camera, [600, 0])
    katana_camera.setName('katana_camera')
    name_parameter = katana_camera.getParameter('name')
    name_parameter.setValue('/root/world/camera/katana_camera', 1.0)
    name_parameter.setUseNodeDefault(False)
    
    xyz = {
        'translate': {
            'x': 0.80,
            'y': 4.61,
            'z': 7.45
            },
        'rotate':{
            'x':-9.74,
            'y': 4.58,
            'z': 5.98
            },
        }
    
    for k, v in xyz.items():
        for axis, value in v.items():
            axis_parameter = katana_camera.getParameter('transform.%s.%s' % (k, axis))
            axis_parameter.setValue(value, 1.0)
            axis_parameter.setUseNodeDefault(False)
    
    # merge node
    merge = NodegraphAPI.CreateNode('Merge', parent=root_node)
    NodegraphAPI.SetNodePosition(merge, [300, -100])
    
    # connections
    batman_input = merge.addInputPort('batman_input')
    batman_input.connect(batman_abc.getOutputPort('out'))
    
    plane_input = merge.addInputPort('plane_input')
    plane_input.connect(primitive_plane.getOutputPort('out'))
    
    camera_input = merge.addInputPort('camera_input')
    camera_input.connect(camera_abc.getOutputPort('out'))
    
    katana_camera_input = merge.addInputPort('katana_camera_input')
    katana_camera_input.connect(katana_camera.getOutputPort('out'))
    
    print 'done!...'

  
