from pymel import core

meshs = core.ls(type='mesh')

for mesh in meshs:
    print mesh.name()
    
print '\nDone.................!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'