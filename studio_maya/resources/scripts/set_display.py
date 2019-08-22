'''
:description: 
    to set the all modelplanel (display)to nurbsCurves, nurbsSurfaces and polymeshes
'''


from maya import cmds

panels   = cmds.getPanel(type='modelPanel') 
     
for panel in panels :
    cmds.modelEditor(panel, e=1, allObjects=0)
                                                 
for panel in panels :
    cmds.modelEditor(panel, e=1, nurbsCurves=1)
    cmds.modelEditor(panel, e=1, nurbsSurfaces=1)
    cmds.modelEditor(panel, e=1, polymeshes=1)
    
print 'Total panels', len(panels)
print '\t', panels
print 'All panels display set into only the nurbsCurves, nurbsSurfaces and polymeshes!...'
