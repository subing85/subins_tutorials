NAME = 'Set Show'
ORDER = 1
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'set the maya project to respective shows!...'
SEPARATOR = True

def execute():
    from studio_usd_pipe.utils.smaya import show
    reload(show)
    show.set()