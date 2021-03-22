KEY = 'toolkit'
NAME = 'Texture Manager'
ORDER = 2
ENABLE = True
ICON = 'texture_manager.png'
LAST_MODIFIED = 'Jun 20, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'Manage the source images(search and replace)'


def execute():
    from tools import texture_manager
    texture_manager.show_window(standalone=False)
