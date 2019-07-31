NAME = 'Import To All Selected Polygons'
ORDER = 5
VALID = True
LAST_MODIFIED = 'July 28, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To import to all the selected uv sets!...'


def execute():
    from pymel import core
    replay = core.fileDialog2(
        dir=core.workspace(q=True, dir=True),
        ds=2,
        ff="Uv Set Ascii (*.uv)",
        fm=1,
        okc='Import',
        cap=NAME
    )
    if not replay:
        return None
    import_path = replay[0]
    core.studioUV(typ='import', s='selected', rp=True, dir=import_path)
    return import_path
