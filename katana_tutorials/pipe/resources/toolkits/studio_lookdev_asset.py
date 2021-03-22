KEY = 'toolkit'
NAME = 'Lookdev Asset Node'
ORDER = 4
ENABLE = True
ICON = 'lookdev_asset_node.png'
LAST_MODIFIED = 'Jun 22, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'custom studio lookdev asset node'


def execute():
    from resources.studio_nodes import lookdev_asset_node
    reload(lookdev_asset_node)
    lookdev_asset_node.create()   
    
    

