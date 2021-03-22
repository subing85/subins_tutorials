KEY = 'toolkit'
NAME = 'Lookdev Bake Node'
ORDER = 5
ENABLE = True
ICON = 'lookdev_bake_node.png'
LAST_MODIFIED = 'Jun 25, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'custom studio lookdev bake node'


def execute():
    from resources.studio_nodes import lookdev_bake_node
    reload(lookdev_bake_node)
    lookdev_bake_node.create()    

    

