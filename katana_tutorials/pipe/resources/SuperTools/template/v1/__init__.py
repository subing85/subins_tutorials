# more details
# https://learn.foundry.com/katana/Content/ug/groups_macros_super_tools/writing_super_tool.html


from Node import TemplateNode


def GetEditor():
    from Editor import TemplateEditor
    return TemplateEditor

