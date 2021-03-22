KEY = 'toolkit'
NAME = 'Lighting Render Node'
ORDER = 10
ENABLE = True
ICON = 'lighting_render_node.png'
LAST_MODIFIED = 'Jun 25, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'custom studio lighting render node (super-tool)'


def execute():
    from Katana import NodegraphAPI
    root = NodegraphAPI.GetRootNode()
    NodegraphAPI.CreateNode('studio_lighting_render', parent=root) 

    

