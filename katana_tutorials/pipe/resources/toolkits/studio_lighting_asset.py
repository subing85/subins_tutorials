KEY = 'toolkit'
NAME = 'Lighting Asset Node'
ORDER = 9
ENABLE = True
ICON = 'lighting_asset_node.png'
LAST_MODIFIED = 'Jun 26, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'custom studio Lighting asset node'


def execute():
    from resources.studio_nodes import lighting_asset_node
    reload(lighting_asset_node)
    lighting_asset_node.create()   
