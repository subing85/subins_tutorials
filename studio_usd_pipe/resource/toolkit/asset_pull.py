NAME = 'Asset Pull'
ORDER = 5
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Pull asset to scene such as model, uv, surface, puppet!...'
SEPARATOR = False
ICON = 'asset_pull.png'


def execute():
    from studio_usd_pipe.gui import asset_pull
    reload(asset_pull)
    asset_pull.show_window(standalone=False)
