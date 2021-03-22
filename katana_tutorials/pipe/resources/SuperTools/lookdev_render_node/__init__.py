# more details
# https://learn.foundry.com/katana/Content/ug/groups_macros_super_tools/writing_super_tool.html

# lookdev render node super tool

import v1

NODE_TYPE = 'studio_lookdev_render'

arguments = (
    'SuperTool',
    2,
    NODE_TYPE,  # type of the node
    (v1.LookdevRenderNode, v1.GetEditor)
    )

PluginRegistry = [arguments]

