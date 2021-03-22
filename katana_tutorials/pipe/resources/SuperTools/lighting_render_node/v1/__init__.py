# more details
# https://learn.foundry.com/katana/Content/ug/groups_macros_super_tools/writing_super_tool.html


from Node import LightingRenderNode


def GetEditor():
    from Editor import LightingRenderEditor
    return LightingRenderEditor

