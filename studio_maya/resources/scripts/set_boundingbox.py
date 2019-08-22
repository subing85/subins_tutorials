'''
:description: 
    to set viewport to bounding box
'''


from maya import cmds

panels   = cmds.getPanel(type='modelPanel') 
                                                 
for panel in panels :
    cmds.modelEditor(panel, e=1, displayAppearance='boundingBox')

print 'Total panels', len(panels)
print '\t', panels
print 'All panels display set into \"BoundingBox\"'
