NAME = 'Create Asset USD'
ORDER = 6
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Create USD with complete assets!...'
SEPARATOR = True
ICON = 'asset_pushusd.png'


def execute():
    from studio_usd_pipe.gui import asset_pushusd
    reload(asset_pushusd)
    asset_pushusd.show_window(standalone=False)