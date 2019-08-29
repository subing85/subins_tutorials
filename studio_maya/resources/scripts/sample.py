from pymel import core

meshs = core.ls(type='mesh')
print "\nhttp://www.subins-toolkits.com", '\n', '-'*41 
print '\nScene meshs'
for mesh in meshs:
    print '\t', mesh.name()    
print '\nDone...'