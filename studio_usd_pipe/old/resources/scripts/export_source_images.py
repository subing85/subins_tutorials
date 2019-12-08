import sys

from studio_usd_pipe.core import smaya
from studio_usd_pipe.core import initialize


def export_source_images(source_file, dirname_to, stamped_time):
    from maya import standalone
    standalone.initialize(name='python')
    from maya import OpenMaya
    initialize.set_plugins()
    from studio_usd_pipe.core import export
    file_io = OpenMaya.MFileIO()
    file_io.open(source_file, None, True, OpenMaya.MFileIO.kLoadDefault, True)
    export.source_images(dirname_to, stamped_time=stamped_time)
    smaya.save_file(source_file, stamped_time=stamped_time)
    standalone.uninitialize(name='python')


arguments = initialize.sys_argv_to_dict(sys.argv[2:])
export_source_images(
    arguments['args'][0],
    arguments['args'][1],
    float(arguments['args'][2])
    )
