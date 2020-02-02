NAME = 'Set Bounding Box'
ORDER = 3
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Set the all view to Bounding Box!...'
SEPARATOR = False


def execute():
    from studio_usd_pipe.api import studioMaya
    reload(studioMaya)
    sm = studioMaya.Maya()
    sm.set_bounding_box()
