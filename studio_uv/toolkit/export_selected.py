NAME = 'Export Selected'
ORDER = 1
VALID = True
LAST_MODIFIED = 'July 28, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To export the selected uv sets!...'


def execute():
    from pymel import core
    replay = core.fileDialog2(
        dir=core.workspace(q=True, dir=True),
        ds=2,
        ff="Uv Set Ascii (*.uv)",
        fm=0,
        okc='Export',
        cap=NAME
    )
    if not replay:
        return None    
    export_path = replay[0]
    if not replay[0].endswith('.uv'):
        export_path = '%s.uv' % replay[0]
    core.studioUV(typ='export', s='selected', dir=export_path)
    return export_path
