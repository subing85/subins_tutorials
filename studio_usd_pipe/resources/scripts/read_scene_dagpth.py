import sys


from studio_usd_pipe.core import initialize
from studio_usd_pipe.core import smaya


def export_source_images(source_file):
    from maya import standalone
    standalone.initialize(name='python')
    from maya import OpenMaya
    initialize.set_plugins()
    file_io = OpenMaya.MFileIO()
    file_io.open(source_file, None, True, OpenMaya.MFileIO.kLoadDefault, True)
    dagpath_nodes = smaya.get_scene_nodes()
    standalone.uninitialize(name='python')
    print dagpath_nodes
    return dagpath_nodes


arguments = initialize.sys_argv_to_dict(sys.argv[2:])
export_source_images(
    arguments['args'][0],
)
