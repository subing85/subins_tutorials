NAME = 'Asset Push/Publish'
ORDER = 4
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Asset publish such as model, uv, surface, puppet!...'
SEPARATOR = True
ICON = 'asset_publish.png'


def execute():
    from studio_usd_pipe.gui import asset_publish
    reload(asset_publish)
    asset_publish.show_window(standalone=False)
