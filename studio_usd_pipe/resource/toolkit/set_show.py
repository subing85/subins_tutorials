NAME = 'Set Show'
ORDER = 1
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'set the maya project to respective shows!...'
SEPARATOR = True
ICON = 'set_show.png'


def execute():
    from studio_usd_pipe.utils.smaya import show
    show.set()
