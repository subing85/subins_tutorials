'''
scene_preview.py 0.0.1 
Date: August 05, 2019
Last modified: August 05, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    to set the scene panels display to bounding box
'''


from maya import cmds

panels = cmds.getPanel(type='modelPanel')

for panel in panels:
    cmds.modelEditor(panel, e=1, displayAppearance='boundingBox')

print "\nhttp://www.subins-toolkits.com", '\n', '-'*41 
print 'Total panels', len(panels)
print panels
print 'All panels display set into "BoundingBox"'
