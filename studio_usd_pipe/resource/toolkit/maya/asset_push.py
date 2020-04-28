NAME = 'Asset Push/Publish'
ORDER = 4
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Asset publish such as model, uv, surface, puppet!...'
SEPARATOR = True
ICON = 'asset_push.png'


def execute():
    from studio_usd_pipe.gui import asset_push
    reload(asset_push)
    asset_push.show_window(standalone=False)
