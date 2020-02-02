NAME = 'Set Viewport'
ORDER = 2
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Set the currnet view to single perspective view!...'
SEPARATOR = False


def execute():
    from studio_usd_pipe.api import studioMaya
    reload(studioMaya)
    sm = studioMaya.Maya()
    sm.set_perspective_view()
