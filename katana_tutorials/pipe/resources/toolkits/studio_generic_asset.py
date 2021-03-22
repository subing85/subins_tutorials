KEY = 'toolkit'
NAME = 'Asset Node'
ORDER = 3
ENABLE = True
ICON = 'generic_asset_node.png'
LAST_MODIFIED = 'Jun 22, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'custom studio asset node'


def execute():
    from resources.studio_nodes import generic_asset_node
    reload(generic_asset_node)
    generic_asset_node.create()   
    
    

