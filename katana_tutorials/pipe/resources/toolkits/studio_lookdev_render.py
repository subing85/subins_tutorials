KEY = 'toolkit'
NAME = 'Lookdev Render Node'
ORDER = 6
ENABLE = True
ICON = 'lookdev_render_node.png'
LAST_MODIFIED = 'Jun 25, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'custom studio lookdev render node (super-tool)'


def execute():
    from Katana import NodegraphAPI
    root = NodegraphAPI.GetRootNode()
    NodegraphAPI.CreateNode('studio_lookdev_render', parent=root) 

    

